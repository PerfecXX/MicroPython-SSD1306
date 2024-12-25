# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin, SoftI2C

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22), sda=Pin(21))

# OLED Interface
oled = SSD1306_I2C(128, 64, oled_Pin)

#        x,y,r,start_angle,end_angle
oled.arc(64, 32, 20, 0, 180, 1)
oled.show()
