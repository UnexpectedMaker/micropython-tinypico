from machine import SPI, Pin
import tinypico as TinyPICO
from micropython_dotstar import DotStar
import time
import random

spi = SPI(sck=Pin( TinyPICO.DOTSTAR_CLK ), mosi=Pin( TinyPICO.DOTSTAR_DATA ), miso=Pin( TinyPICO.SPI_MISO) ) # Configure SPI 
dotstar = DotStar(spi, 1) # Just one DotStar
TinyPICO.dotstar_power( True ) # Set dotstar power to on

# Show some info on boot 
print("Hello from TinyPICO!")
print("Battery Voltage is " + str( TinyPICO.battery_voltage() ) + "V")
print("Battery Charge State is " + str( TinyPICO.battery_charging() ) )

# flicker random colours on the Dotstar
while True:
    time.sleep(0.25)
    dotstar[0] = ( random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 0.5) # Random


