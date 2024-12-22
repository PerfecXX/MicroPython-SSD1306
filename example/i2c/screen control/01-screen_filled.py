# Import Library
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep

# Initialize I2C and the OLED display
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128  
oled_height = 64  
oled = SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # fill screen to black
    oled.fill(0)
    oled.show()
    sleep(1)
    # fill screen to while
    oled.fill(1)
    oled.show()
    sleep(1)
