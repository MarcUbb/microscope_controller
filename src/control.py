import machine
import constants


def photo_mul_read(): # reads photomultiplier
    return(constants.PHOTO_MUL.read())



def supply_init():
    pass



def stop(): # puts all the outputs on safe values and resets MC
    constants.STATE = "MENU"
    constants.PAST_STATE = ""
    constants.TEST_PROGRESS = 0
    constants.ABORT_CAPTURE = False
    constants.ZOOM = 1
    supply_init()
    machine.reset()