# TinyPICO MicroPython Support Library
# 2019 Seon Rozenblum, Matt Trentini
#
# Project home:
#   https://github.com/unexpectedmaker/tinypico-library
#
# 2019-Mar-12 - v0.1 - Initial implementation

# Import required libraries 
from micropython import const
from machine import Pin, SPI, ADC

# Pin assingmenta

# Battery
BAT_VOLTAGE = const(35)
BAT_CHARGE = const(34)

# APA102 Dotstar pins for production boards
DOTSTAR_CLK = const(12)
DOTSTAR_DATA = const(2)
DOTSTAR_PWR = const(13)

# SPI
SPI_MOSI = const(23)
SPI_CLK = const(18)
SPI_MISO = const(19)

#I2C
I2C_SDA = const(21)
I2C_SCL = const(22)

#DAC
DAC1 = const(25)
DAC2 = const(26)

# Helper functions

# Get a *rough* estimate of the current battery voltage
def battery_voltage():
    adc = ADC( Pin( BAT_VOLTAGE ) )         # Assign the ADC pin to read
    measuredvbat = adc.read()               # Read the value
    measuredvbat /= 4095                    # divide by 4095 as we are using the default ADC voltage range of 0-1V
    measuredvbat *= 3.7                     # Multiply by 3.7V, our reference voltage
    return measuredvbat

# Return the current charge state of the battery - we need to read the value multiple times
# to eliminate false negatives due to the charge IC not knowing the difference between no battery
# and a full battery not charging - This is why the charge LED flashes
def battery_charging():
    measuredVal = 0                         # start our reading at 0
    io = Pin( BAT_CHARGE, Pin.IN )          # Assign the pin to read
  
    for y in range(0, 10):                  # loop through 10 times adding the read values together to ensure no false positives    
        measuredVal += io.value()

    return ( measuredVal == 0 )             # return True if the value is 0

# Power is controlled by a PNP transistor, so low is ON and high is OFF
# We also need to set the DOTSTAR clock and data pins to be inputs to prevent power leakage when power is off
# This might be fixed in the Software SPI implementation at a future date
def dotstar_power( state ):
    Pin( DOTSTAR_PWR ).value( not state )   # Set the power pin to the inverse of state 

    if state :                              # If power is on, set CLK and DATA to be outputs
        Pin( DOTSTAR_CLK, Pin.OUT )
        Pin( DOTSTAR_DATA, Pin.OUT )
    else:                                   # If power is on, set CLK and DATA to be inputs
        Pin( DOTSTAR_CLK, Pin.IN )
        Pin( DOTSTAR_DATA, Pin.IN )