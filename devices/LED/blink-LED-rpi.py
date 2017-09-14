# Assumes that anode of LED is connected to the GPIO and cathode to ground
# Switching high the GPIO pin therefore turns on the LED and switching it low turns it off

# External module imports

# RPi.GPIO Abstracts GPIO handling
import RPi.GPIO as GPIO
# time library provides delay and other time related functions.
import time

# Using GPIO in BCM mode
GPIO.setmode(GPIO.BCM)
# 4 -> GPIO 4, board pin no. 7
ledPin = 4
#Configure as Output for LED control
GPIO.setup(ledPin, GPIO.OUT)

# Print text on terminal
print("Hello IoT World ! Blinking LED now. Press CTRL+C to exit")
try:
    while 1:
        print ("LED OFF");
        GPIO.output(ledPin, GPIO.LOW)   # Turn OFF
        time.sleep(1)                   # 1 second delay
        print ("LED ON");
        GPIO.output(ledPin, GPIO.HIGH)  # Turn ON
        time.sleep(1)                   # 1 second delay
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print ("Goodbye\n")
    GPIO.cleanup() # Release all GPIO pins for further use
