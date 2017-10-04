### Blink LED with Raspberry Pi GPIO

Blinking an LED connected to Raspberry Pi is one of the most basic experiments in the world of physical computing. This involves switching a GPIO pin high and low.

Here is a quick guide to blink an LED with Raspberry Pi.

#### Hardware

Wire up the circuit as shown below.

Connect the anode to a GPIO 4 (Board pin number 7).

Connect the cathode to ground via a resistor (470 Ohms)

Switching the GPIO pin to high turns on the LED and switching it to low turns the LED off. This switching of GPIO pins is done through software.

![Schematic](../../Images/basic-LED_bb.png)



#### Software

In Python there are some good libraries available for controlling GPIO. The most popular libraries for Raspberry Pi are:
* RPi.GPIO
* gpizero

RPi.GPIO abstracts a lot of GPIO handling functionality.

gpiozero is the latest library and packs much functionality for common interfacing tasks with Raspberry Pi GPIO pins.

For example, the LED blinking code when using RPi.GPIO needs calls to switch ON and OFF the LED with a delay function. In gpiozero, there is a blink function, so you can get the same output in just one line of code.

The code included here uses RPi.GPIO. More code samples will be added later using the gpiozero library.

The sample programs available for LED are:
1. [blink-LED-rpi-gpio.py](blink-LED-rpi-gpio.py)


###### Notes
**How to identify the anode and cathode of LED**

There are two different ways to identify anode and cathode of LED.

1. Based on lead length

Usually the anode is longer lead of the LED and cathode is the shorter lead. However, you can't rely on this always. If the leads are cut for e.g. this method doesn't give correct answer. The best way therefore is to use a multi-meter as described below.

2. Using Multi-meter

- Put the multi-meter in diode testing mode
- Connect the leads of multi-meter to the LED.
- The LED will light up only if the positive lead of multi-meter gets connected to anode and negative lead to cathode.
- Beware that when testing LED in this way, the intensity of LED light is quite low so you need to observe it in little darkness by covering it with your hands.

 For additional information about LED, have a look at this file [LED-Info.md](LED-Info.md).
