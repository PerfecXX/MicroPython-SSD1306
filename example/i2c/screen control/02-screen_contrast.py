from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep

# Initialize I2C and the OLED display
i2c = SoftI2C(scl=Pin(22), sda=Pin(21)) 
oled_width = 128  
oled_height = 64  
oled = SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # Show test text
    oled.text("Test Contrast",15,0)
    
    # Contrast Level Adjusment
    for contrast_level in range(0,255):
        
        oled.contrast(contrast_level)
        
        # Show Contrast Level
        oled.text("LV:{}".format(contrast_level),50,40,1)
        oled.show()
        oled.text("LV:{}".format(contrast_level),50,40,0)
