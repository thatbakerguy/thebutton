#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

from thebutton import TheButton



# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# turn on the lcd and declare thebutton
thebutton=TheButton()
lcd.backlight(lcd.ON)


while True: 
	lcd.clear()
	lcd.message(thebutton.get_current_time()) 
	sleep(.5)
