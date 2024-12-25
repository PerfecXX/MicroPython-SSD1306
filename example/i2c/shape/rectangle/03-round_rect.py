# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin, SoftI2C

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22), sda=Pin(21))

# OLED Interface
oled = SSD1306_I2C(128, 64, oled_Pin)

# Draw a rectangle with rounded corners
oled.round_rect(10, 10, 60, 40, 1, filled=False, radius=10)
oled.show()
