from machine import Pin
from network import WLAN, STA_IF
from urequests import post
from gc import mem_free, mem_alloc, collect
from time import sleep

def memory_usage_percentage():
    """Used for development purposes"""
    total_memory = mem_alloc() + mem_free()
    percentage_used = (mem_alloc() / total_memory) * 100
    return percentage_used

# WLAN credentials
WIFI_SSID = ""
WIFI_PASSWORD = ""
# Pushover credentials
APP_TOKEN = ""
USER_TOKEN = ""

sensor_a = Pin(17, Pin.IN, Pin.PULL_DOWN)
sensor_b = Pin(16, Pin.IN, Pin.PULL_DOWN)

pico_led = Pin("LED", Pin.OUT)
sensor_a_triggered = False
sensor_b_triggered = False
a_watered_flag = False
b_watered_flag = False

def flash_led():
    global pico_led
    repeat = 6    
    for _ in range(repeat):
        pico_led.toggle()
        sleep(1)

def connect_to_wifi(max_retries=5):
    print("Connecting to wifi...")
    wlan = WLAN(STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    # Start with a small delay and increase with each failed attempt
    delay = 1
    retries = 0
    while not is_network_connection() and retries < max_retries:
        sleep(delay)
        delay *= 2  # double the delay for the next iteration
        retries += 1

    if retries == max_retries:
        print("Failed to connect after multiple attempts.")
    else:
        print("Success: connected to wifi.")
        flash_led()

def is_network_connection() -> bool:
    wlan = WLAN(STA_IF)
    if wlan.isconnected():
        # print("Network configuration:", wlan.ifconfig())
        return True
    else:
        return False
        
def send_notification(app_token: str, user_key: str, message: str) -> None:
    """Sends notification to Pushover API"""
    url = "https://api.pushover.net/1/messages.json"
    headers = { "Content-type": "application/x-www-form-urlencoded" }

    # Manually build the data string
    data_str = '&'.join(['token=' + app_token, 'user=' + user_key, 'message=' + message])
    data_bytes = data_str.encode('utf-8')

    response = post(url, data=data_bytes, headers=headers)
    collect() # collect garbage after post request
    response.close()

def sensor_irq_handler(pin):
    """Unified interrupt handler for both rising and falling edges"""
    global sensor_a_triggered, a_watered_flag, sensor_b_triggered, b_watered_flag
    # Check if it's sensor_a
    if pin == sensor_a:
        if pin.value() == 1:  # Rising edge for sensor_a
            sensor_a_triggered = True
        else:  # Falling edge for sensor_a
            sensor_a_triggered = False
            a_watered_flag = True
    # Check if it's sensor_b (You can create separate flags for sensor_b if needed)
    elif pin == sensor_b:
        if pin.value() == 1:  # Rising edge for sensor_b
            sensor_b_triggered = True
        else:  # Falling edge for sensor_b
            sensor_b_triggered = False
            b_watered_flag = True

sensor_a.irq(
    trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
    handler=sensor_irq_handler
)

sensor_b.irq(
    trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
    handler=sensor_irq_handler
)


while True:

    if not is_network_connection():
        connect_to_wifi()

    if sensor_a_triggered:
        send_notification(
            app_token=APP_TOKEN,
            user_key=USER_TOKEN,
            message="Calathea needs watering"
        )
        sensor_a_triggered = False

    if a_watered_flag:
        send_notification(
            app_token=APP_TOKEN,
            user_key=USER_TOKEN,
            message="Calathea has been watered! :)"
        )
        a_watered_flag = False

    if sensor_b_triggered:
        send_notification(
            app_token=APP_TOKEN,
            user_key=USER_TOKEN,
            message="Fern needs watering"
        )
        sensor_b_triggered = False

    if b_watered_flag:
        send_notification(
            app_token=APP_TOKEN,
            user_key=USER_TOKEN,
            message="Fern has been watered! :)"
        )
        b_watered_flag = False

    sleep(2000) # sleep for 2000 seconds (c. 1/2 hour)