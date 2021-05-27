import constants
import ili9341
import control
import time
import screens

def electronics_test(display):
    control.esp32_1_on()
    i = 0
    while i < 101:
        screens.draw_test_progress(display, i)
        time.sleep(1)
        i += 10
    return

def capture(display): # uses methodes from control and sensor date to create via "draw value" functionan image on the screen, returns 2d array of values (represents image)
    f = open('image.csv', 'w')
    control.esp32_1_on()
    x = 0
    while x < constants.HEIGHT - 2:
        y = 0
        while y < constants.HEIGHT - 2:
            control.esp32_3(x)
            control.esp32_4(y)
            time.sleep(0.005)
            control.esp32_2_on()
            value = control.photo_mul_read()
            time.sleep(0.005)
            control.esp32_2_off()
            screens.draw_value(display, x, y, value)
            
            y += 1

            if y < constants.HEIGHT - 2:
                f.write(str(value) + ",")
            else:
                f.write(str(value)) # writes no "," if its the last value in the line
            
            if constants.ABORT_CAPTURE == True:
                f.close()
                return(1)


        f.write('\n')
        x += 1
    f.close()
    return(0)