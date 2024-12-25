# Import Library
from micropython import const
import framebuf
import math

__version__ = '1.0.2'
__author__ = 'Teeraphat Kullanankanjana'

# Register definitions
SET_DISP = const(0xae)
SET_MEM_ADDR = const(0x20)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xa0)
SET_MUX_RATIO = const(0xa8)
SET_COM_OUT_DIR = const(0xc0)
SET_DISP_OFFSET = const(0xd3)
SET_COM_PIN_CFG = const(0xda)
SET_DISP_CLK_DIV = const(0xd5)
SET_PRECHARGE = const(0xd9)
SET_VCOM_DESEL = const(0xdb)
SET_ENTIRE_ON = const(0xa4)
SET_NORM_INV = const(0xa6)
SET_CHARGE_PUMP = const(0x8d)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)
SET_CONTRAST = const(0x81)

class SSD1306:
    def __init__(self, width, height, external_vcc):
        """
        Initialize the SSD1306 display object.

        Parameters:
            width (int): Width of the display.
            height (int): Height of the display.
            external_vcc (bool): Whether the display uses external VCC (default is False).
        """
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = height // 8
        self.buffer = bytearray(self.pages * self.width)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)

        # Graphics functions with docstrings
        self.fill = self.framebuf.fill
        """Fill the entire display with the specified color (0 for off, 1 for on)."""
        
        self.pixel = self.framebuf.pixel
        """
        Set or get the pixel at the specified position.
        
        Parameters:
            x (int): X coordinate of the pixel.
            y (int): Y coordinate of the pixel.
            color (int): The color to set (0 for off, 1 for on). If not provided, it returns the pixel value.
        
        Returns:
            int: The current pixel value (0 or 1).
        """

        self.hline = self.framebuf.hline
        """
        Draw a horizontal line from (x, y) with the given length and color.

        Parameters:
            x (int): Starting x coordinate of the line.
            y (int): Y coordinate of the line.
            length (int): The length of the line.
            color (int): The color of the line (0 for off, 1 for on).
        """

        self.vline = self.framebuf.vline
        """
        Draw a vertical line from (x, y) with the given length and color.

        Parameters:
            x (int): X coordinate of the line.
            y (int): Starting y coordinate of the line.
            length (int): The length of the line.
            color (int): The color of the line (0 for off, 1 for on).
        """
        
        self.line = self.framebuf.line
        """
        Draw a line between two points with the specified color.

        Parameters:
            x0 (int): Starting x coordinate of the line.
            y0 (int): Starting y coordinate of the line.
            x1 (int): Ending x coordinate of the line.
            y1 (int): Ending y coordinate of the line.
            color (int): The color of the line (0 for off, 1 for on).
        """
        
        self.rect = self.framebuf.rect
        """
        Draw a rectangle with the specified position, size, and color.

        Parameters:
            x (int): X coordinate of the top-left corner of the rectangle.
            y (int): Y coordinate of the top-left corner of the rectangle.
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            color (int): The color of the rectangle (0 for off, 1 for on).
        """
        
        self.fill_rect = self.framebuf.fill_rect
        """
        Fill a rectangle with the specified position, size, and color.

        Parameters:
            x (int): X coordinate of the top-left corner of the rectangle.
            y (int): Y coordinate of the top-left corner of the rectangle.
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            color (int): The color of the rectangle (0 for off, 1 for on).
        """
        
        self.text = self.framebuf.text
        """
        Draw text at the specified position with the specified color.

        Parameters:
            string (str): The text string to draw.
            x (int): X coordinate where the text should start.
            y (int): Y coordinate where the text should start.
            color (int): The color of the text (0 for off, 1 for on).
        """
        
        self.scroll = self.framebuf.scroll
        """
        Scroll the display content by the specified number of pixels in the x and y directions.

        Parameters:
            dx (int): The number of pixels to scroll in the x direction (positive to scroll right).
            dy (int): The number of pixels to scroll in the y direction (positive to scroll down).
        """
        
        self.blit = self.framebuf.blit
        """
        Copy a portion of another frame buffer to the display.

        Parameters:
            buffer (framebuf.FrameBuffer): The source frame buffer to copy from.
            x (int): X coordinate of where to place the top-left corner of the blitted image.
            y (int): Y coordinate of where to place the top-left corner of the blitted image.
        """

        self.init_display()

    def init_display(self):
        """
        Initialize the display settings and configuration.
        """
        for cmd in (
            SET_DISP | 0x00,  # Display off
            SET_MEM_ADDR, 0x00,  # Horizontal addressing mode
            SET_DISP_START_LINE | 0x00,  # Start line at 0
            SET_SEG_REMAP | 0x01,  # Column address 127 mapped to SEG0
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08,  # Scan direction COM[N] to COM0
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x02 if self.height == 32 else 0x12,
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0x22 if self.external_vcc else 0xf1,
            SET_VCOM_DESEL, 0x30,  # 0.83 * Vcc
            SET_CONTRAST, 0xff,  # Maximum contrast
            SET_ENTIRE_ON,  # Output follows RAM content
            SET_NORM_INV,  # Not inverted
            SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14,  # Charge pump
            SET_DISP | 0x01  # Display on
        ):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        """
        Power off the display.
        """
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        """
        Power on the display.
        """
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        """
        Set the display contrast.

        Parameters:
            contrast (int): The contrast value (0-255).
        """
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        """
        Invert the display.

        Parameters:
            invert (bool): Whether to invert the display (True or False).
        """
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def rotate(self, rotate):
        """
        Rotate the display.

        Parameters:
            rotate (bool): Whether to rotate the display (True or False).
        """
        self.write_cmd(SET_COM_OUT_DIR | ((rotate & 1) << 3))
        self.write_cmd(SET_SEG_REMAP | (rotate & 1))

    def show(self):
        """
        Update the display with the current buffer content.
        """
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:  # 64-pixel wide displays are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)
    
    def triangle(self, x0, y0, x1, y1, x2, y2, color, fill=False):
        """
        Draw a triangle defined by three points with the specified color.

        Parameters:
            x0, y0 (int): Coordinates of the first vertex.
            x1, y1 (int): Coordinates of the second vertex.
            x2, y2 (int): Coordinates of the third vertex.
            color (int): The color of the triangle (0 for off, 1 for on).
            fill (bool): Whether to fill the triangle (default is False, i.e., outline only).
        """
        if fill:
            # Fill the triangle using a simple scan-line fill algorithm
            # Find the bounding box of the triangle
            min_x = min(x0, x1, x2)
            max_x = max(x0, x1, x2)
            min_y = min(y0, y1, y2)
            max_y = max(y0, y1, y2)

            for y in range(min_y, max_y + 1):
                # Find the x-coordinates where the scan line crosses the edges of the triangle
                crossings = []
                if (y0 <= y <= y1) or (y1 <= y <= y0):
                    crossings.append(self._get_intersection(x0, y0, x1, y1, y))
                if (y1 <= y <= y2) or (y2 <= y <= y1):
                    crossings.append(self._get_intersection(x1, y1, x2, y2, y))
                if (y0 <= y <= y2) or (y2 <= y <= y0):
                    crossings.append(self._get_intersection(x0, y0, x2, y2, y))

                # Sort the x-coordinates and fill between the intersections
                crossings.sort()
                for x in range(crossings[0], crossings[1] + 1):
                    self.pixel(x, y, color)
        else:
            # Draw the outline of the triangle
            self.line(x0, y0, x1, y1, color)
            self.line(x1, y1, x2, y2, color)
            self.line(x2, y2, x0, y0, color)
            
    def _get_intersection(self, x0, y0, x1, y1, y):
        """
        Helper function to find the intersection point between a line and a horizontal scanline at a given y-coordinate.

        Parameters:
            x0, y0 (int): The first point of the line.
            x1, y1 (int): The second point of the line.
            y (int): The y-coordinate of the horizontal line.

        Returns:
            int: The x-coordinate where the line intersects the scanline.
        """
        if y1 == y0:  # Horizontal line
            return min(x0, x1)
        # Linear interpolation to find the x-coordinate of the intersection
        return int(x0 + (x1 - x0) * (y - y0) / (y1 - y0))
    
    def circle(self, cx, cy, r, color, fill=False):
        """
        Draw a circle defined by center (cx, cy) and radius r with the specified color.

        Parameters:
            cx, cy (int): The center coordinates of the circle.
            r (int): The radius of the circle.
            color (int): The color of the circle (0 for off, 1 for on).
            fill (bool): Whether to fill the circle (default is False, i.e., outline only).
        """
        if fill:
            # Fill the circle
            for y in range(cy - r, cy + r + 1):
                dx = int((r ** 2 - (y - cy) ** 2) ** 0.5)
                for x in range(cx - dx, cx + dx + 1):
                    self.pixel(x, y, color)
        else:
            # Outline the circle (Bresenham's Circle Algorithm)
            x = 0
            y = r
            p = 3 - 2 * r

            while x <= y:
                # Draw the eight symmetrical points
                self.pixel(cx + x, cy + y, color)
                self.pixel(cx - x, cy + y, color)
                self.pixel(cx + x, cy - y, color)
                self.pixel(cx - x, cy - y, color)
                self.pixel(cx + y, cy + x, color)
                self.pixel(cx - y, cy + x, color)
                self.pixel(cx + y, cy - x, color)
                self.pixel(cx - y, cy - x, color)

                # Update the decision parameter
                if p < 0:
                    p = p + 4 * x + 6
                else:
                    p = p + 4 * (x - y) + 10
                    y -= 1
                x += 1
    
    def polygon(self, points, color, fill=False):
        """
        Draw a polygon defined by a list of points (x, y) with the specified color.

        Parameters:
            points (list of tuples): List of (x, y) tuples representing the vertices of the polygon.
            color (int): The color of the polygon (0 for off, 1 for on).
            fill (bool): Whether to fill the polygon (default is False, i.e., outline only).
        """
        num_points = len(points)

        # Draw the outline of the polygon (connect consecutive points)
        for i in range(num_points):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % num_points]  # Wrap around to the first point
            self.line(x0, y0, x1, y1, color)

        if fill:
            # Fill the polygon using the scanline algorithm
            # Find the minimum and maximum Y values in the polygon
            min_y = min(points, key=lambda p: p[1])[1]
            max_y = max(points, key=lambda p: p[1])[1]

            # For each Y level, find the intersection points
            for y in range(min_y, max_y + 1):
                intersections = []
                for i in range(num_points):
                    x0, y0 = points[i]
                    x1, y1 = points[(i + 1) % num_points]  # Wrap around to the first point

                    # Check if the horizontal line at Y intersects the line segment
                    if (y0 <= y < y1) or (y1 <= y < y0):  # Check if the horizontal line crosses the segment
                        # Find the intersection point using the equation of the line
                        x_intersection = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
                        intersections.append(int(x_intersection))

                # Sort the intersection points
                intersections.sort()

                # Fill between pairs of intersection points
                for i in range(0, len(intersections), 2):
                    x_start = intersections[i]
                    x_end = intersections[i + 1]
                    # Draw the horizontal line between the intersection points
                    for x in range(x_start, x_end + 1):
                        self.pixel(x, y, color)
    
    def parallelogram(self, x1, y1, x2, y2, dx1, dy1, dx2, dy2, color, fill=False):
        """
        Draw a parallelogram defined by two base points and two direction vectors.

        Parameters:
            x1, y1 (int): Coordinates of the first base point.
            x2, y2 (int): Coordinates of the second base point.
            dx1, dy1 (int): Direction vector for the first side.
            dx2, dy2 (int): Direction vector for the second side.
            color (int): The color of the parallelogram (0 for off, 1 for on).
            fill (bool): Whether to fill the parallelogram (default is False).
        """
        # Calculate the four vertices of the parallelogram
        x3, y3 = x1 + dx1, y1 + dy1
        x4, y4 = x2 + dx2, y2 + dy2

        # Draw the outline of the parallelogram (4 sides)
        self.line(x1, y1, x2, y2, color)  # First side
        self.line(x2, y2, x4, y4, color)  # Second side
        self.line(x4, y4, x3, y3, color)  # Third side
        self.line(x3, y3, x1, y1, color)  # Fourth side

        if fill:
            # Fill the parallelogram using a scanline algorithm
            # Find the bounding box of the parallelogram
            min_y = min(y1, y2, y3, y4)
            max_y = max(y1, y2, y3, y4)

            for y in range(min_y, max_y + 1):
                intersections = []

                # Find intersections with the parallelogram's edges
                self._find_intersections(x1, y1, x2, y2, y, intersections)
                self._find_intersections(x2, y2, x4, y4, y, intersections)
                self._find_intersections(x4, y4, x3, y3, y, intersections)
                self._find_intersections(x3, y3, x1, y1, y, intersections)

                # Remove duplicate intersections
                intersections = list(set(intersections))

                # Sort the intersection points
                intersections.sort()

                # Fill between pairs of intersection points
                for i in range(0, len(intersections), 2):
                    if i + 1 < len(intersections):  # Ensure there is a pair
                        x_start = intersections[i]
                        x_end = intersections[i + 1]
                        # Draw the horizontal line between the intersection points
                        for x in range(x_start, x_end + 1):
                            self.pixel(x, y, color)

    
    def trapezium(self, x1, y1, x2, y2, x3, y3, x4, y4, color, fill=False):
        """
        Draw a trapezium defined by four points.

        Parameters:
            x1, y1 (int): Coordinates of the top-left point.
            x2, y2 (int): Coordinates of the top-right point.
            x3, y3 (int): Coordinates of the bottom-right point.
            x4, y4 (int): Coordinates of the bottom-left point.
            color (int): The color of the trapezium (0 for off, 1 for on).
            fill (bool): Whether to fill the trapezium (default is False).
        """
        # Draw the outline of the trapezium (4 sides)
        self.line(x1, y1, x2, y2, color)  # Top side
        self.line(x2, y2, x3, y3, color)  # Right side
        self.line(x3, y3, x4, y4, color)  # Bottom side
        self.line(x4, y4, x1, y1, color)  # Left side

        if fill:
            # Fill the trapezium using a scanline algorithm
            min_y = min(y1, y2, y3, y4)
            max_y = max(y1, y2, y3, y4)

            for y in range(min_y, max_y + 1):
                intersections = []

                # Find intersections with the trapezium's edges
                self._find_intersections(x1, y1, x2, y2, x3, y3, y, intersections)
                self._find_intersections(x2, y2, x3, y3, x4, y4, y, intersections)
                self._find_intersections(x3, y3, x4, y4, x1, y1, y, intersections)
                self._find_intersections(x4, y4, x1, y1, x2, y2, y, intersections)

                # Sort the intersection points
                intersections.sort()

                # Fill between pairs of intersection points
                for i in range(0, len(intersections), 2):
                    x_start = intersections[i]
                    x_end = intersections[i + 1]
                    # Draw the horizontal line between the intersection points
                    for x in range(x_start, x_end + 1):
                        self.pixel(x, y, color)
    
    def ellipse(self, cx, cy, rx, ry, color, fill=False):
        """
        Draw an ellipse defined by center (cx, cy) and radii rx (horizontal) and ry (vertical) with the specified color.

        Parameters:
            cx, cy (int): The center coordinates of the ellipse.
            rx (int): The horizontal radius of the ellipse.
            ry (int): The vertical radius of the ellipse.
            color (int): The color of the ellipse (0 for off, 1 for on).
            fill (bool): Whether to fill the ellipse (default is False, i.e., outline only).
        """
        if fill:
            # Fill the ellipse using the parametric equation
            for y in range(cy - ry, cy + ry + 1):
                dx = int(rx * (1 - ((y - cy) ** 2 / ry ** 2)) ** 0.5)
                for x in range(cx - dx, cx + dx + 1):
                    self.pixel(x, y, color)
        else:
            # Outline the ellipse (using a midpoint ellipse algorithm)
            x = 0
            y = ry
            p1 = ry * ry - rx * rx * ry + 0.25 * rx * rx
            dx = 2 * ry * ry * x
            dy = 2 * rx * rx * y

            # Region 1 (Above the center)
            while dx < dy:
                self.pixel(cx + x, cy + y, color)
                self.pixel(cx - x, cy + y, color)
                self.pixel(cx + x, cy - y, color)
                self.pixel(cx - x, cy - y, color)
                
                x += 1
                dx += 2 * ry * ry
                if p1 < 0:
                    p1 += dx + ry * ry
                else:
                    y -= 1
                    dy -= 2 * rx * rx
                    p1 += dx - dy + ry * ry
            
            # Region 2 (Below the center)
            p2 = ry * ry * (x + 0.5) ** 2 + rx * rx * (y - 1) ** 2 - rx * rx * ry * ry
            while y >= 0:
                self.pixel(cx + x, cy + y, color)
                self.pixel(cx - x, cy + y, color)
                self.pixel(cx + x, cy - y, color)
                self.pixel(cx - x, cy - y, color)
                
                y -= 1
                dy -= 2 * rx * rx
                if p2 > 0:
                    p2 += rx * rx - dy
                else:
                    x += 1
                    dx += 2 * ry * ry
                    p2 += dx - dy + rx * rx

    
    def _find_intersections(self, x1, y1, x2, y2, dx, dy, y, intersections):
        """
        Find the intersection of the line (x1, y1) -> (x2, y2) with the horizontal line at y.
        
        Parameters:
            x1, y1 (int): Start coordinates of the line segment.
            x2, y2 (int): End coordinates of the line segment.
            dx, dy (int): Direction vector of the line segment.
            y (int): The Y-coordinate of the horizontal line.
            intersections (list): List to store the X-coordinate of the intersection.
        """
        if (y1 <= y < y2) or (y2 <= y < y1):  # Check if the horizontal line crosses the segment
            x_intersection = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            intersections.append(int(x_intersection))
            
    def round_rect(self, x, y, w, h, color, filled=False, radius=0):
        """
        Draw a rectangle with optional rounded corners.

        Parameters:
            x, y (int): The starting coordinates of the rectangle.
            w, h (int): The width and height of the rectangle.
            color (int): The color of the rectangle (0 for off, 1 for on).
            filled (bool): Whether the rectangle should be filled (default is False).
            radius (int): The radius for rounded corners (default is 0 for sharp corners).
        """
        if radius > 0:
            # Draw the rounded corners using arcs
            self.arc(x + radius, y + radius, radius, 180, 270, color)  # top-left
            self.arc(x + w - radius - 1, y + radius, radius, 270, 360, color)  # top-right
            self.arc(x + radius, y + h - radius - 1, radius, 90, 180, color)  # bottom-left
            self.arc(x + w - radius - 1, y + h - radius - 1, radius, 0, 90, color)  # bottom-right

        # Draw the four straight sides (with or without filling)
        if filled:
            self.fill_rect(x + radius, y, w - 2 * radius, h, color)  # top
            self.fill_rect(x + radius, y + h - 1, w - 2 * radius, -h + 2 * radius, color)  # bottom
            self.fill_rect(x, y + radius, w, h - 2 * radius, color)  # left
            self.fill_rect(x + w - 1, y + radius, -w + 2 * radius, h - 2 * radius, color)  # right
        else:
            # Draw the outline of the rectangle (with rounded corners)
            self.line(x + radius, y, x + w - radius - 1, y, color)  # top
            self.line(x + radius, y + h - 1, x + w - radius - 1, y + h - 1, color)  # bottom
            self.line(x, y + radius, x, y + h - radius - 1, color)  # left
            self.line(x + w - 1, y + radius, x + w - 1, y + h - radius - 1, color)  # right

    def arc(self, cx, cy, r, start_angle, end_angle, color):
        """
        Draw an arc (part of a circle) for rounded corners.

        Parameters:
            cx, cy (int): The center coordinates of the arc.
            r (int): The radius of the arc.
            start_angle, end_angle (int): The start and end angles in degrees.
            color (int): The color of the arc (0 for off, 1 for on).
        """
        start_angle = math.radians(start_angle)  # Convert to radians
        end_angle = math.radians(end_angle)

        step = 1 / r  # Control the smoothness of the curve
        for angle in range(int(start_angle * 180 / math.pi), int(end_angle * 180 / math.pi)):
            angle_rad = angle * math.pi / 180
            x = int(cx + r * math.cos(angle_rad))
            y = int(cy + r * math.sin(angle_rad))
            self.pixel(x, y, color)

    # Abstract methods for communication to be implemented in subclasses
    def write_cmd(self, cmd):
        raise NotImplementedError

    def write_data(self, buf):
        raise NotImplementedError


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        """
        Initialize the SSD1306 I2C display object.

        Parameters:
            width (int): Width of the display.
            height (int): Height of the display.
            i2c (I2C): The I2C bus object.
            addr (int): The I2C address of the display (default is 0x3c).
            external_vcc (bool): Whether the display uses external VCC (default is False).
        """
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        """
        Write a command to the display over I2C.

        Parameters:
            cmd (int): The command to send.
        """
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        """
        Write data to the display over I2C.

        Parameters:
            buf (bytearray): The data to send to the display.
        """
        self.i2c.writeto_mem(self.addr, 0x40, buf)


class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs, external_vcc=False):
        """
        Initialize the SSD1306 SPI display object.

        Parameters:
            width (int): Width of the display.
            height (int): Height of the display.
            spi (SPI): The SPI bus object.
            dc (Pin): Data/command pin.
            res (Pin): Reset pin.
            cs (Pin): Chip select pin.
            external_vcc (bool): Whether the display uses external VCC (default is False).
        """
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs
        self.rate = 10 * 1024 * 1024
        dc.init(dc.OUT, value=0)
        res.init(res.OUT, value=0)
        cs.init(cs.OUT, value=1)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        """
        Write a command to the display over SPI.

        Parameters:
            cmd (int): The command to send.
        """
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs.high()
        self.dc.low()
        self.cs.low()
        self.spi.write(bytearray([cmd]))
        self.cs.high()

    def write_data(self, buf):
        """
        Write data to the display over SPI.

        Parameters:
            buf (bytearray): The data to send to the display.
        """
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs.high()
        self.dc.high()
        self.cs.low()
        self.spi.write(buf)
        self.cs.high()
