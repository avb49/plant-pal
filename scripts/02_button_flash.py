# flash the on-board LED when the button is pressed
from machine import Pin

led = Pin("LED", Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_DOWN)

while True:
    led.value(button.value())