# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin, SoftI2C

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22), sda=Pin(21))

# OLED Interface
oled = SSD1306_I2C(128, 64, oled_Pin)

# Clear the display
oled.fill(0)

# Draw a horizontal line
#          x y  lenth color
oled.hline(0,30,100,1)
oled.show()
