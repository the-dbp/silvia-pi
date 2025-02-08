import time
import RPi.GPIO as GPIO

brew_gpio = 17  # Replace with actual GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(brew_gpio, GPIO.OUT)

for i in range(10):
    GPIO.output(brew_gpio, 0)
    time.sleep(5)
    GPIO.output(brew_gpio, 1)
    time.sleep(10)

for i in range(2):
    GPIO.output(brew_gpio, 0)
    time.sleep(1)
    GPIO.output(brew_gpio, 1)
    time.sleep(1)

GPIO.cleanup()
