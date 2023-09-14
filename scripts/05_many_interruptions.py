import machine

led_1 = machine.Pin("LED", machine.Pin.OUT)
led_2 = machine.Pin(10, machine.Pin.OUT)

button_a = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

led_1_state = False
led_2_state = False

def button_irq_handler(pin):

    global led_1_state
    global led_2_state

    if pin == button_a:
        if led_1_state == True:
            led_1_state = False
        else:
            led_1_state = True
    
    elif pin == button_b:
        if led_2_state == True:
            led_2_state = False
        else:
            led_2_state = True        

button_a.irq(trigger=machine.Pin.IRQ_RISING,
             handler=button_irq_handler)
button_b.irq(trigger=machine.Pin.IRQ_RISING,
             handler=button_irq_handler)

while True:
    led_1.value(led_1_state)
    led_2.value(led_2_state)