import adafruit_max31855

from busio import SPI
from digitalio import DigitalInOut
import board
spi = SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = DigitalInOut(board.D5)

sensor = adafruit_max31855.MAX31855(spi, cs)
print(sensor.temperature)
