# Import Library
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep

# Initialize I2C and the OLED display
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128  
oled_height = 64  
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Clear Screen
oled.fill(0)

# Points for diamond (a rotated square)
points = [(64, 10), (84, 32), (64, 54), (44, 32)]  # Diamond shape
oled.polygon(points, color=1, fill=False)  # Draw diamond outline
oled.show()

sleep(1)

oled.polygon(points, color=1, fill=True)  # Draw fiiled diamond
oled.show()
