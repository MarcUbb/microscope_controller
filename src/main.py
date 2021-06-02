import time
import constants
import screens
import touch
import storage
import control
import capture


# sets outputs of microcontroller to safe values
control.supply_init()

# initiates devices
display = screens.init_screen()
touchscreen = touch.init_touch()

  
# checks the value of the constants.STATE variable and performs actions accordingly
while True:

    time.sleep(0.1)

    print(constants.STATE) # for debugging

    """
    The if-statements check if the state is their state, but only perform actions if the 
    past state was not the same state, thereby preventing performing action every cycle.

    After the action was performed the past state variable is set to the same state so that 
    next time the loop cycles the if-statement is called but the action is not performed.

    For a more detailes description of the states, please take a look at touch.py or at the 
    state diagramm. The following commentary will only explain the actions performed!
    """

    if constants.STATE == "MENU":
        if constants.PAST_STATE != "MENU":
            # draws interface of menu screen
            screens.draw_menu(display)
        constants.PAST_STATE = "MENU"


    elif constants.STATE == "ZOOM_UPDATE":
        # changes the state back to HOME to cause the interface to update with the new zoom value
        constants.STATE = "MENU"
        constants.PAST_STATE = "ZOOM_UPDATE"


    elif constants.STATE == "VACUUM_REQUEST":
        if constants.PAST_STATE != "VACUUM_REQUEST":
            # draws the request on the screen
            screens.draw_vacuum_request(display)
        constants.PAST_STATE = "VACUUM_REQUEST"

    elif constants.STATE == "DARKENING_REQUEST":
        if constants.PAST_STATE != "DARKENING_REQUEST":
            # draws the request on the screen
            screens.draw_darkening_request(display)
        constants.PAST_STATE = "DARKENING_REQUEST"

    elif constants.STATE == "TEST_ELECTRONICS_REQUEST":
        if constants.PAST_STATE != "TEST_ELECTRONICS_REQUEST":
            # draws the request on the screen
            screens.draw_electronics_test_request(display)
        constants.PAST_STATE = "TEST_ELECTRONICS_REQUEST"

    elif constants.STATE == "TESTING_ELECTRONICS":
        # draws the progress bar
        screens.draw_testing_electronics(display)
        # performs the electronics test (shows progress on screen)
        capture.electronics_test(display)
        # changes state to capturing after finishing the electronics test
        constants.STATE = "CAPTURING"
        # doesnt need to change the past state since the statement will only be run once at the time

    elif constants.STATE == "CAPTURING":
        # draws capturing interface
        screens.draw_capturing(display)
        # performs imaging
        aborted = capture.capture(display)
        # if imaging function returns 0 (meaning it finished imaging and was not aborted) the state is changed so the image can be saved
        if aborted == 0:
            constants.STATE = "CAPTURED"
        # if however the "abbrechen" - button was pressed while imaging, the capture function is aborted and returns 1
        elif aborted == 1:
            constants.ABORT_CAPTURE = False
            constants.STATE = "MENU"
        # adjusting past state is not necessary since capturing is only run once

    elif constants.STATE == "CAPTURED":
        if constants.PAST_STATE != "CAPTURED":
            # adds "save" - button to interface
            screens.draw_captured(display)
        constants.PAST_STATE = "CAPTURED"

    elif constants.STATE == "SAVE":
        # moves image to sd card
        storage.save_image()
        #changes state back to captured to make sure the interface still works
        constants.STATE = "CAPTURED"
