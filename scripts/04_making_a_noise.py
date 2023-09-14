# use 2 buttons to drive a buzzer (noise) using interrupts
from machine import Pin, PWM

# how long the signal is on compared to off
DUTY_CYCLE = 0.75
MAX_BIT_VALUE = 655535

button_1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(1, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(15))

# PWM output (Pulse Width Modulation)
buzzer.duty_u16(int(DUTY_CYCLE*MAX_BIT_VALUE))
# frequency in hertz
frequency = 1000

def button_irq_handler(pin):
    global frequency
    if pin == button_1:
        if frequency < 2000:
            frequency += 50
    elif pin == button_2:
        if frequency > 100:
            frequency -= 50

# set up IRQ (interrupt)
button_1.irq(trigger=Pin.IRQ_RISING,
             handler=button_irq_handler)
button_2.irq(trigger=Pin.IRQ_RISING,
             handler=button_irq_handler)

while True:
    buzzer.freq(frequency)