import adafruit_max31855
from busio import SPI
from digitalio import DigitalInOut
import board
import time

LOG_FILE = "temperature_log.txt"

spi = SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = DigitalInOut(board.D5)
sensor = adafruit_max31855.MAX31855(spi, cs)

def log_temperature():
    timestamp = time.time()
    temperature = sensor.temperature
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp},{temperature}\n")

def clean_old_records():
    current_time = time.time()
    with open(LOG_FILE, "r") as file:
        lines = file.readlines()
    with open(LOG_FILE, "w") as file:
        for line in lines:
            ts, _ = line.strip().split(",")
            if current_time - float(ts) <= 60:
                file.write(line)

if __name__ == "__main__":
    log_temperature()
    clean_old_records()
