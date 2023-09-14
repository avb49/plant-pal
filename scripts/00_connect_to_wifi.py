# connects Pico to WiFi

import network
import time

WIFI_SSID = ""
WIFI_PASSWORD = ""

def connect_to_wifi():

    print("Connecting to wifi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    while not is_network_connection():
        pass

def is_network_connection() -> bool:

    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        # print("Network configuration:", wlan.ifconfig())
        return True
    else:
        return False
        
while True:

    if not is_network_connection():
        connect_to_wifi()
    print("Connected to the network!")
    time.sleep(5)