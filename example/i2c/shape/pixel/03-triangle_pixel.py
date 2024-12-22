# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin, SoftI2C

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22), sda=Pin(21))

# OLED Interface
oled = SSD1306_I2C(128, 64, oled_Pin)

# Clear the display
oled.fill(0)

# Define triangle vertices
x0, y0 = 10, 10  # Point A
x1, y1 = 60, 50  # Point B
x2, y2 = 110, 20  # Point C

# Line AB
dx = abs(x1 - x0)
dy = abs(y1 - y0)
sx = 1 if x0 < x1 else -1
sy = 1 if y0 < y1 else -1
err = dx - dy
while True:
    oled.pixel(x0, y0, 1)
    if x0 == x1 and y0 == y1:
        break
    e2 = err * 2
    if e2 > -dy:
        err -= dy
        x0 += sx
    if e2 < dx:
        err += dx
        y0 += sy

# Line BC
x0, y0 = x1, y1
x1, y1 = x2, y2
dx = abs(x1 - x0)
dy = abs(y1 - y0)
sx = 1 if x0 < x1 else -1
sy = 1 if y0 < y1 else -1
err = dx - dy
while True:
    oled.pixel(x0, y0, 1)
    if x0 == x1 and y0 == y1:
        break
    e2 = err * 2
    if e2 > -dy:
        err -= dy
        x0 += sx
    if e2 < dx:
        err += dx
        y0 += sy

# Line CA
x0, y0 = x2, y2
x1, y1 = 10, 10
dx = abs(x1 - x0)
dy = abs(y1 - y0)
sx = 1 if x0 < x1 else -1
sy = 1 if y0 < y1 else -1
err = dx - dy
while True:
    oled.pixel(x0, y0, 1)
    if x0 == x1 and y0 == y1:
        break
    e2 = err * 2
    if e2 > -dy:
        err -= dy
        x0 += sx
    if e2 < dx:
        err += dx
        y0 += sy

# Update the display
oled.show()

