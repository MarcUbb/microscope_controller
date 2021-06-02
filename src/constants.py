import ili9341
import xglcd_font
import machine

# colors as ili9341.color565 object
WHITE = ili9341.color565(255,255,255)
BLACK = ili9341.color565(0,0,0)

# size of the screen
HEIGHT = 240
WIDTH = 319

# font for interface
FONT = xglcd_font.XglcdFont("standard_font5x7.c", 5,7, letter_count=223) # ("Neato5x7.c", 5,7, letter_count=223)

# zoom level (can be adjusted in menu)
ZOOM = 1

# state of the interface (controlled in touch.py and implemented in main.py)
STATE = "MENU"

# keeps track of the last screen state to prevent update each frame and overwriting of interface
PAST_STATE = "" 

# keeps track of electronics test progress to visualize as rogress bar
TEST_PROGRESS = 0

# tells capture methode in capture.py if the action was aborted (by clicking the "abbrechen" - button)
ABORT_CAPTURE = False

# Pins on ESP32
# ili9341 pins
RST = machine.Pin(17)
CS_SCREEN = machine.Pin(16)
CLK_SCREEN = machine.Pin(14)
MOSI_SCREEN = machine.Pin(13)
DC = machine.Pin(4)

# xpt2046 pins
IRQ = machine.Pin(0)
CS_TOUCH = machine.Pin(5)
CLK_TOUCH = machine.Pin(18)
MOSI_TOUCH = machine.Pin(23)
MISO_TOUCH = machine.Pin(19)

# analog output pins (for deflector plates)
# x plates GPIO25
ESP32_3 = machine.PWM(machine.Pin(25))
ESP32_3.freq(50)
# y plates GPIO26
ESP32_4 = machine.PWM(machine.Pin(26)) 
ESP32_4.freq(50)
# photomultiplier input
PHOTO_MUL = machine.ADC(machine.Pin(36)) 