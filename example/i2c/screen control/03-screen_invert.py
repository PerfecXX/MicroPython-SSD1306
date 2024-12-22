# Import Library
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep

# Initialize I2C and the OLED display
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128  
oled_height = 64  
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Show Test Text
oled.text("Screen Invert",15,0)
oled.show()

# invert screen color
while True:
    oled.invert(0)
    sleep(1)
    oled.invert(1)
    sleep(1)
