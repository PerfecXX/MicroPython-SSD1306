# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

# OLED Interface 
oled = SSD1306_I2C(128,64,oled_Pin)

# Draw Horizontal Line with Pixel
for x in range(0,60):
    oled.pixel(x,30,1)

# Draw Vertical Line with Pixel
for y in range(0,60):
    oled.pixel(30,y,1)
  
oled.show()
