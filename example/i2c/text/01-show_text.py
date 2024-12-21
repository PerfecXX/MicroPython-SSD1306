# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

# Pin Setup
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Clear Screen
oled.fill(0)
oled.show()

# Text Display (Text,x,y,color)
oled.text("Hello Wolrd!",0,0,1)
oled.show()
