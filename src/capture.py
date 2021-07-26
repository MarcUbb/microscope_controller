import constants
import ili9341
import control
import time
import screens
import random

def electronics_test(display):
    """
    test both stepper motors and photomultiplier

    Args:
        display (ili9341.Display object): specifies the display on which the progress bar is shown

    Variables: 
        x (int): stores random number of steps to be taken by stepper motor (necessary to go back to starting position after test is finsished)
        y (int): same as "x" but for 2nd stepper motor
        i (int): percentage of progress
        z (int): stores the test value from photomultiplier

    Returns: -
    """
    x = random.randint(0, constants.HEIGHT - 2 )
    y = random.randint(0, constants.HEIGHT - 2 )

    i = 0
    while i < 101:
        # stepper motor rotates max amount of steps (resolution of image)
        if i == 10:
            constants.ESP32_3.step(constants.HEIGHT - 2, direction = 1)

        # stepper motor moves back to random position
        if i == 20:
            constants.ESP32_3.step(x, direction = -1)

        # same as before but for 2nd stepper motor
        if i == 30:
            constants.ESP32_4.step(constants.HEIGHT - 2, direction = 1)

        if i == 40:
            constants.ESP32_4.step(y, direction = -1)

        # sample value is read from photomultiplier
        if i == 50:
            z = control.photo_mul_read()
            if type(z) == int:
                pass
            else:
                raise Exception("Photomultiplier error!")

        # both motors move back to starting position
        if i == 60:
            constants.ESP32_3.step((constants.HEIGHT - 2) - x, direction = -1)

        if i == 70:
            constants.ESP32_4.step((constants.HEIGHT - 2) - y, direction = -1)

        screens.draw_test_progress(display, i)
        time.sleep(1)
        i += 10
    return



def capture(display):
    """
    controls motors, reads sensor and writes data to capture image

    Args:
        display (ili9341.Display object): specifies the display on which the image is shown

    Variables: 
        f (_io.BufferedWriter): holds file object in which the image is written in csv format
        x (int): stores x coordinate of image
        dir (int): stores direction
        y (int):
        value (int): 


    Returns: -
    """
    f = open('image.csv', 'w')
    x = 0
    dir = 1

    # loop for x stepper motor
    while x < constants.HEIGHT - 2:
        y = 0

        # loop for y stepper motor
        while y < constants.HEIGHT - 2:
            
            constants.ESP32_4.step(1, dir)
            # ADC reading of photomultiplier
            value = control.photo_mul_read()
            
            """
            for quicker imaging the electrone beam goes back an forth so when the 
            beam goes back in y direction the pixel on the opposite side is drawn to
            """
            if dir == 1:
                screens.draw_value(display, x, y, value)
            else:
                screens.draw_value(display, x, constants.HEIGHT - 2 - y, value)
                
                
            y += 1

            # the values are written to the file in csv format which means there is no "," at the end of each line
            if y < constants.HEIGHT - 2:
                f.write(str(value) + ",")
            else:
                f.write(str(value))
            
        # the electrone beam is pointed to the starting position if the imaging process is aborted
        if constants.ABORT_CAPTURE == True:
            constants.ESP32_3.step(x, direction = -1)
            
            if dir == 1:
                constants.ESP32_4.step(y, direction = -1)
            else:
                constants.ESP32_4.step(constants.HEIGHT - 2 - y, direction = 1)
                
            f.close()
            return(1)
        
        # the direction is changed after each row
        if dir == 1:
            dir = -1
        else:
            dir = 1

        constants.ESP32_3.step(1, direction = 1)

        # each row is marked with a new line in the file
        f.write('\n')
        x += 1

    # electrone beam going back to starting position if imaging process is not aborted
    constants.ESP32_3.step(constants.HEIGHT - 2, dir * (-1))

    f.close()
    return