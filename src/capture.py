import constants
import ili9341
import control
import time
import screens
import random

def electronics_test(display):
    control.esp32_1_on()
    
    x = random.randint(0, constants.HEIGHT - 2 )
    y = random.randint(0, constants.HEIGHT - 2 )

    i = 0
    while i < 101:
        if i == 10:
            constants.ESP32_3.step(constants.HEIGHT - 2, direction = 1)

        if i == 20:
            constants.ESP32_3.step(x, direction = -1)

        if i == 30:
            constants.ESP32_4.step(constants.HEIGHT - 2, direction = 1)

        if i == 40:
            constants.ESP32_4.step(y, direction = -1)

        if i == 50:
            z = control.photo_mul_read()
            if type(z) == int:
                pass
            else:
                raise Exception("Photomultiplier error!")

        if i == 60:
            constants.ESP32_3.step((constants.HEIGHT - 2) - x, direction = -1)

        if i == 70:
            constants.ESP32_4.step((constants.HEIGHT - 2) - y, direction = -1)

        screens.draw_test_progress(display, i)
        time.sleep(1)
        i += 10
    return

def capture(display): # uses methodes from control and sensor date to create via "draw value" functionan image on the screen, returns 2d array of values (represents image)
    f = open('image.csv', 'w')
    x = 0
    dir = 1

    while x < constants.HEIGHT - 2:
        y = 0

        while y < constants.HEIGHT - 2:
            
            constants.ESP32_3.step(1, dir)
            value = control.photo_mul_read()

            screens.draw_value(display, x, y, value)
            
            y += 1

            if y < constants.HEIGHT - 2:
                f.write(str(value) + ",")
            else:
                f.write(str(value)) # writes no "," if its the last value in the line
            
        if constants.ABORT_CAPTURE == True:
            f.close()
            return(1)
        
        if dir == 1:
            dir = -1
        else:
            dir = 1

        constants.ESP32_4.step(1, direction = 1)

        f.write('\n')
        x += 1

    constants.ESP32_4.step(constants.HEIGHT - 2, dir * (-1))

    f.close()
    return(0)