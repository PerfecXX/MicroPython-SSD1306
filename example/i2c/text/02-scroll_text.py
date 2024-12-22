# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

# OLED Interface 
oled = SSD1306_I2C(128,64,oled_Pin)

# Screen Invert
oled.invert(1)

# Variable 
x_pos = 0
y_pos = 30

while True:
    # Show Text 
    oled.text("Hello!",x_pos,y_pos,1)
    oled.show()
    sleep(0.1)
    # Clear Text
    oled.fill(0)
    oled.show()
    
    # Check Text Position
    if x_pos > 125:
        x_pos = 0
    else:
        x_pos = x_pos+1
