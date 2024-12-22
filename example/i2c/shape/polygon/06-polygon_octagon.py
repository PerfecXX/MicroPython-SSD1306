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

# Points for octagon
points = [(40, 10), (60, 10), (70, 20), (70, 40), (60, 50), (40, 50), (30, 40), (30, 20)]  # Octagon with 8 points
oled.polygon(points, color=1, fill=False)  # Draw octagon outline
oled.show()

sleep(1)

# Points for octagon
points = [(40, 10), (60, 10), (70, 20), (70, 40), (60, 50), (40, 50), (30, 40), (30, 20)]  # Octagon with 8 points
oled.polygon(points, color=1, fill=True)  # Draw filled octagon
oled.show()
