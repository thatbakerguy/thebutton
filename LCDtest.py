#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

from thebutton import TheButton



# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec

thebutton=TheButton()

count = 1
while (count < 100):
	lcd.backlight(lcd.ON) 
	lcd.clear()
	lcd.message(thebutton.get_current_time() ) #print count
	sleep(1)
	lcd.backlight(lcd.OFF)
	count = count+1
	sleep(1)
	print thebutton.get_current_time()
