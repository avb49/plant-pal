# use an interrupt to handle a button press
from machine import Pin

led = Pin("LED", Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_DOWN)
led_state = False

# IRQ (interrupt) handler
def button_irq_handler(pin):
    global led_state
    if led_state == True:
        led_state = False
    else:
        led_state = True

# set up IRQ
button.irq(trigger=Pin.IRQ_RISING,
           handler=button_irq_handler)

while True:
    led.value(led_state)