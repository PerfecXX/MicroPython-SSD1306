# Import Library
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer,MONO_HLSB
# Import an image frame from file
from images import kmitl_logo,cu_logo

# Initialize I2C and the OLED display
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128  
oled_height = 64  
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Create a frame buffer
kmitl_fb = FrameBuffer(kmitl_logo, oled_width, oled_height,MONO_HLSB)
cu_fb = FrameBuffer(cu_logo, oled_width, oled_height,MONO_HLSB)

# Blit the image to the display and show it
oled.fill(0)
oled.blit(kmitl_fb, 0, 0)
oled.show()
