import machine
import xpt2046
import constants
import control


def touch(x,y):
    """
    gets called when touchcontroller creates an interrupt and changes the constants.STATE variable according to where the user touched the screen

    Args:
        x (int): x - coordinate of the touch
        y (int): y - coordinate of the touch

    Variables: -

    Returns: -
    """
    # state of initiation shows menu screen
    if constants.STATE == "MENU":

        # "bild aufnehmen" - button was pressed
        if x <= 55 and y >= 230:
            constants.STATE = "VACUUM_REQUEST"

        # "+" - button was pressed
        elif x <= 110 and x > 55 and y >= 230 and y < 280:
            if constants.ZOOM < 100000:
                constants.ZOOM = int(constants.ZOOM * 10)
            constants.STATE = "ZOOM_UPDATE"

        # "-" - button was pressed
        elif x <= 110 and x > 55 and y >=280:
            if constants.ZOOM > 1:
                constants.ZOOM = int(constants.ZOOM / 10)
            constants.STATE = "ZOOM_UPDATE"

        # "Notaus" - button was pressed
        elif x > 175 and y >= 230:
            constants.STATE = "STOP"
            control.stop()
        


    # shows vacuum request on screen
    elif constants.STATE == "VACUUM_REQUEST":
        # "bestätigen" - button was pressed
        if x > 100 and x < 140 and y > 110 and y < 210:
            constants.STATE = "DARKENING_REQUEST"



    # shows darkening request on screen
    elif constants.STATE == "DARKENING_REQUEST":
        # "bestätigen" - button was pressed
        if x > 100 and x < 140 and y > 110 and y < 210:
            constants.STATE = "TEST_ELECTRONICS_REQUEST"



    # shows electronics test request on screen
    elif constants.STATE == "TEST_ELECTRONICS_REQUEST":
        # "ja" - button was pressed
        if x > 100 and x < 140 and y > 120 and y < 150:
            constants.STATE = "TESTING_ELECTRONICS"

        # "nein" - button was pressed
        elif x > 100 and x < 140 and y >= 150 and y < 180:
            constants.STATE = "CAPTURING"



    # shows progress bar on screen
    elif constants.STATE == "TESTING_ELECTRONICS":
        # "Notaus" - button was pressed
        if x > 175 and y >= 230:
            constants.STATE = "STOP"
            control.stop()



    # shows screen during imaging
    elif constants.STATE == "CAPTURING":
        # "abbrechen" - button was pressed
        if x <= 110 and x > 55 and y >= 230:
            constants.ABORT_CAPTURE = True
            constants.STATE = "MENU"

        # "Notaus" - button was pressed
        elif x > 175 and y >= 230:
            constants.STATE = "STOP"
            control.stop()



    # shows screen after imaging (with saving option)
    elif constants.STATE == "CAPTURED":
        # "abbrechen" - button was pressed
        if x <= 110 and x > 55 and y >= 230:
            constants.STATE = "MENU"

        # "speichern" - button was pressed
        elif x > 110 and x <= 175 and y >= 230:
            constants.STATE = "SAVE"

        # "Notaus" - button was pressed
        elif x > 175 and y >= 230:
            constants.STATE = "STOP"
            control.stop()
        


def init_touch():
    """
    initiates the touchcontroller and returns it

    Args: -

    Variables:
        spi_touch (machine.SPI object): specifies the SPI line for the touchcontroller
        touchscontroller (xpt2046.Touch object): specifies the Pin layout and interrupt methode for the touchcontroller

    Returns:
        touchcontroller (xpt2046.Touch object)
    """
    spi_touch = machine.SPI(2, baudrate=1000000, sck=constants.CLK_TOUCH, mosi=constants.MOSI_TOUCH, miso=constants.MISO_TOUCH)
    touchcontroller = xpt2046.Touch(spi_touch, cs=constants.CS_TOUCH, int_pin=constants.IRQ, int_handler=touch)
    return(touchcontroller)

