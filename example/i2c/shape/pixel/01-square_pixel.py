# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

# OLED Interface 
oled = SSD1306_I2C(128,64,oled_Pin)

# Draw Square with Pixel
for x in range(0,20):
    for y in range(0,20):
        oled.pixel(x,y,1)
oled.show()
