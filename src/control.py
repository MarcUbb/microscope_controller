import machine
import constants


def photo_mul_read():
    return(constants.PHOTO_MUL.read())

def supply_init():
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