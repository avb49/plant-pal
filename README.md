## PlantPal - a plant moisture monitoring system

PlantPal is a smart plant monitoring solution that utilises the Raspberry Pi Pico to keep track of your plants' watering needs. With integrated moisture sensors, PlantPal will send real-time notifications when your plant is thirsty and even confirm when it's been watered.

This repo contains code to run on a Raspberry Pi Pico WH (w. WiFi capabilities) micro-controller. The repo also contains some other toy MicroPython scripts used during development in the folder 'scripts'. 

This project uses 2 moisture sensors to continuously monitor 2 plants. A notification is sent to the user's phone via the app Pushover when a plant requires watering.

The code which should be run on the Pico can be found in 'main.py'. WLAN and Pushover (or other notification API) credentials require modification.

## Images

<figure>
    <img src="/images/overview.jpg" alt="PlantPal system" width="200"/>
    <figcaption>PlantPal system</figcaption>
</figure>

<figure>
    <img src="/images/closeup.jpg" alt="Raspberry Pi Pico close-up (powered by a powerbank)" width="200"/>
    <figcaption>Raspberry Pi Pico close-up (powered by a powerbank)</figcaption>
</figure>

<figure>
    <img src="/images/notification.jpg" alt="Notifications received on iPhone" width="200"/>
    <figcaption>Notifications received on iPhone</figcaption>
</figure>

<figure>
    <img src="/images/sensor.jpg" alt="Close up of a moisture sensor" width="200"/>
    <figcaption>Close up of a moisture sensor</figcaption>
</figure>