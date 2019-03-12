# TinyPICO MicroPython Support Library
# 2019 Seon Rozenblum
#
# Project home:
#   https://github.com/unexpectedmaker/tinypico-library
#
# 2019-Mar-12 - v0.1 - Initial implementation


from micropython import const
from machine import Pin, SPI, ADC

# Battery
BAT_VOLTAGE = const(34)
BAT_CHARGE = const(35)

# These are for the current revision Sample, but wil be changing for the production board
# APA102 Dotstar pins
DOTSTAR_CLK = const(12)
DOTSTAR_DATA = const(13)
DOTSTAR_PWR = const(2)

# SPI
SPI_MOSI = const(23)
SPI_CLK = const(18)
SPI_MISO = const(19)

#I2C
I2C_SDA = const(21)
I2C_SCL = const(22)

# Helper functions

# Get a *rough* estimate of the current battwery voltage - not accurate, but better than nothing
def battery_voltage():

    adc = ADC( Pin( BAT_VOLTAGE ) )     # Assign the ADC pin to read
    measuredvbat = adc.read()           # Read the value
    measuredvbat /= 4095                # devide by 4095 as we are using voltage range of 0-1
    measuredvbat *= 3.7                 # Multiply by 3.7V, our reference voltage

    return measuredvbat

# Return the current charge sdtate of the battery - we need to read the value multiple times
# to eliminate false negatives due to the charge IC not knowing the difference between no battery
# and a full battery not charging - This is why the charge LED flashes
def battery_charging():
    measuredVal = 0                     # start our rrading at 0
    adc = ADC( Pin( BAT_CHARGE ) )      # Assign the ADC pin to read
  
    for y in range(0, 10):              # loop through 10 times adding the read values together to ensure no false positives
        measuredVal += adc.read()

    return ( measuredVal == 0 )         # return True if the value is 0 

# This works, but in the current revision samples, it will be overridden if you tell the Dotstar to display any color, as it will be powered by parasitic leakage from the CLK and DATA pins.
# This is fixed in the production boards
def dotstar_power( state ):
    Pin( DOTSTAR_PWR ).value( state )

