# External module imports
import RPi.GPIO as GPIO
import time

buttonPin = 17  # GPIO 17 using BCM mode (Board pin 11)
oldBtnState = True
newButtonState = True

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
print("Sample code to detect a button press on GPIO {0}".format(buttonPin))

GPIO.setup(buttonPin, GPIO.IN)
time.sleep(0.4)

#print initial button state
newButtonState = GPIO.input(buttonPin);
if newButtonState:
    print ("Button is Pressed")
else:
    print ("Button is Released")

try:
    while 1:
        newButtonState = GPIO.input(buttonPin); # Read current button state
        if oldBtnState != newButtonState:       # Button state change detected
            if newButtonState:                  # Print current button state
                print ("Button is Pressed")
            else:
                print ("Button is Released")

        # save current button state for further comparison
        oldBtnState = newButtonState;
        time.sleep(0.2)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly
    print ("Exiting")
    GPIO.cleanup() # cleanup all GPIO
