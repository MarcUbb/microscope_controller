import machine 
import time

ESP32_1 = machine.Pin(32, machine.Pin.OUT) # anode, faraday cage, photomultiplier
ESP32_2 = machine.Pin(33, machine.Pin.OUT) # cathode

i = 0

while i < 5:
    ESP32_1.value(1)
    time.sleep(0.5)
    ESP32_2.value(1)
    time.sleep(0.5)
    ESP32_1.value(0)
    time.sleep(0.5)
    ESP32_2.value(0)
    time.sleep(0.5)
    i += 1