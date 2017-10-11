import RPi.GPIO as GPIO
import time

ServoControlPin = 23

# Pulse width and duty cycle calculations:
# Duty cycle = (ON time / Total time) * 100

# For any angle, the calculations are done as below:
# Based on observation of a Servo motor, following data was recorded.
# For a particular angular movement, required ON period was observed.

# 0 degrees => 0.4 msec ON time (~ 2% Duty Cycle)
# 180 degrees => 2.26 msec ON time (~ 11.3% Duty Cycle)
# Motor was able to move shaft beyond 180 degrees with higher ON period.
# But beyond 180 degrees movement was ignored.
# With this data, per degree ON period or found as:
# (2.26 - 0.4) / 180 => 10.3 usec ON period per degree of angular rotation.
# 10.3 usec corresponds to duty cycle of 0.052%.
# Based on this the formula for ON period for any angle becomes:
# Duty cycle = (angle*0.052) + 2.
# Here 2% is the duty cycle required for 0 degrees position.
# 1/0.052 is approximately 19.2, so the formula can be simplified to:
# Duty cycle = (Angle/19) + 2

# Typical calculations based on Internet search results
# For 0 degrees: (0.5 / 20) * 100 = 2.5
# For 90 degrees:(1.5 / 20) * 100 = 7.5
# For 180 degrees:(2.5 / 20) * 100 = 12.5


def rotateServo(servoPin = ServoControlPin, angle=0):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin, GPIO.OUT)

# Configure PWM to generate 50Hz (A pulse every 20msec) frequency
# Returns an object. Call various methods on the object
    servoPWM = GPIO.PWM(servoPin, 50)

    try:
        dutyCycle = float((angle/19) + 2)
        #print (dutyCycle)
        servoPWM.start(dutyCycle)
        time.sleep(1) # sleep 1 second
        servoPWM.stop()
    except:
        servoPWM.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    while True:
        try:
            angle = int(input("Enter angle from 0 to 180 to rotate servo or Ctrl+C to quit\n"))
            if ((((angle)) >= 0 and ((angle)) <= 180) ):
                rotateServo(ServoControlPin, angle)
                print ("Servo rotation done")
                continue
            else:
                print ("Enter a value between 0 and 180 only")
                continue
        except ValueError:
            print ("Invalid input")
            continue
        except KeyboardInterrupt:
            print ("Exiting servo motor code")
            GPIO.cleanup()
            break
