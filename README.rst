MicroPython TinyPICO
====================

TinyPICO MicroPython Helper Library

This library adds some helper functions and useful pin assignments to making coding with TinyPICO & MicroPython easier

Pin Assignments
---------------
.. code-block:: python

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
..

Helper functions
----------------
.. code-block:: python

    # Return a *rough* estimate of the current battery voltage
    def battery_voltage():

    # Return the current charge state of the battery
    def battery_charging():

    # Power is controlled by a PNP transistor, so low is ON and high is OFF
    def dotstar_power( state ):

..

Example Usage
-------------
.. code-block:: python

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
..
