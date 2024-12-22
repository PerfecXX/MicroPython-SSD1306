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

# Smaller points for 5-pointed star
points = [
    (64, 10),  # Top point
    (70, 30),  # Outer right point
    (85, 30),  # Outer bottom-right point
    (75, 40),  # Inner right point
    (80, 60),  # Outer bottom-right point
    (64, 50),  # Inner bottom point
    (48, 60),  # Outer bottom-left point
    (50, 40),  # Inner left point
    (35, 30),  # Outer bottom-left point
    (50, 30),  # Outer left point
    (64, 10)   # Close to the first point
]

# Draw star outline
oled.polygon(points, color=1, fill=False)
oled.show()

sleep(1)

# Draw star outline
oled.polygon(points, color=1, fill=True)
oled.show()
