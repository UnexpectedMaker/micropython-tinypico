# This example requires the micropython_dotstar library
# https://github.com/mattytrentini/micropython-dotstar

from machine import SPI, Pin
import tinypico as TinyPICO
from micropython_dotstar import DotStar
import time, random

# Configure SPI for controlling the DotStar
spi = SPI(sck=Pin( TinyPICO.DOTSTAR_CLK ), mosi=Pin( TinyPICO.DOTSTAR_DATA ), miso=Pin( TinyPICO.SPI_MISO) ) 
# Create a DotStar instance
dotstar = DotStar(spi, 1, brightness = 0.5 ) # Just one DotStar, half brightness
# Turn the power to the DotStar on
TinyPICO.dotstar_power( True )

# Say hello
print("Hello from TinyPICO!")
# Show some info on boot 
print("Battery Voltage is {}V".format( TinyPICO.battery_voltage() ) )
print("Battery Charge State is {}".format( TinyPICO.battery_charging() ) )

# Flicker random colours on the Dotstar
while True:
    dotstar[0] = ( random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 0.5) # Random colours!
    time.sleep(0.2)