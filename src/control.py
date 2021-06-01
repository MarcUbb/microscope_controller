import machine
import constants

def esp32_1_on():
    constants.ESP32_1.value(1)
    return

def esp32_1_off():
    constants.ESP32_1.value(0)
    return

def esp32_2_on():
    constants.ESP32_2.value(1)
    return

def esp32_2_off():
    constants.ESP32_2.value(0)
    return

def esp32_3(value): # value must be between 0 and 255
    constants.ESP32_3.write(value)
    return

def esp32_4(value): # value must be between 0 and 255
    constants.ESP32_4.write(value)
    return

def esp32_5_on():
    constants.ESP32_5.value(1)
    return

def esp32_5_off():
    constants.ESP32_5.value(0)
    return

def esp32_6_on():
    constants.ESP32_6.value(1)
    return

def esp32_6_off():
    constants.ESP32_7.value(0)
    return

def photo_mul_read():
    return(constants.PHOTO_MUL.read())

def supply_init():
    esp32_1_off()
    esp32_2_off()
    esp32_3(0)
    esp32_4(0)


def stop(): # puts all the outputs on safe values and resets MC
    constants.STATE = "MENU"
    constants.PAST_STATE = ""
    constants.TEST_PROGRESS = 0
    constants.ABORT_CAPTURE = False
    constants.ZOOM = 1
    supply_init()
    machine.reset()