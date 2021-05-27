import machine
import ili9341
import xglcd_font
import constants


def init_screen():
    """
    initiates the display and returns it
    
    Args: - 
    
    Variables:
        spi (machine.SPI object): specifies the SPI line for the display
        display (ili9341.Display object): specifies the Pin layout for the screen

    Returns:
        display (ili9341.Display object)
    """
    
    spi = machine.SPI(1, baudrate=40000000, sck = constants.CLK_SCREEN, mosi = constants.MOSI_SCREEN)
    display = ili9341.Display(spi, dc = constants.DC, cs = constants.CS_SCREEN, rst = constants.RST)
    return display



def clear_buttons(display):
    """
    clears the button labels to change the interface while keeping the imaging result on the screen
    
    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables: -

    Returns: -
    """
    display.fill_vrect(0,0,constants.HEIGHT, constants.WIDTH-constants.HEIGHT, constants.BLACK)



def draw_menu(display):
    """
    draws the menu interface

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables:
        i (int): counter from 0 to 3 to draw the 4 buttons

    Returns: -
    """
    clear_buttons(display)
    print(constants.ZOOM)
    display.draw_rectangle(0,0,constants.HEIGHT,constants.WIDTH,constants.WHITE)             
    display.draw_rectangle(0,constants.WIDTH-constants.HEIGHT,constants.HEIGHT,constants.HEIGHT,constants.WHITE)  
    for i in range(4):
        display.draw_rectangle(i*int(constants.HEIGHT/4),0,int(constants.HEIGHT/4), constants.WIDTH-constants.HEIGHT, constants.WHITE)   

    display.draw_text(20,50, "take", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(40,65, "image", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(85,60, "+", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(85,25, "-", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(145,75, "zoom: " + str(constants.ZOOM) + "x", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(205,55, "stop", constants.FONT, constants.WHITE, landscape=True)



def draw_vacuum_request(display):
    """
    draws a request to make sure a vacuum is applied before taking the image

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables: -

    Returns: -
    """
    display.clear()
    display.draw_rectangle(0,0,constants.HEIGHT,constants.WIDTH,constants.WHITE)

    display.draw_rectangle(100,120, 30, 80, constants.WHITE)

    display.draw_text(60, 300, "Make sure the chamber is vacuumed!", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(110,190, "confirm", constants.FONT, constants.WHITE, landscape=True)



def draw_darkening_request(display):
    """
    draws a request to make sure the chamber is darkened before taking the image

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables: -

    Returns: -
    """
    display.clear()
    display.draw_rectangle(0,0,constants.HEIGHT,constants.WIDTH,constants.WHITE)

    display.draw_rectangle(100,120, 30, 80, constants.WHITE)

    display.draw_text(60, 310, "Make sure the chamber is darkened!", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(110,190, "confirm", constants.FONT, constants.WHITE, landscape=True)



def draw_electronics_test_request(display):
    """
    draws a request to ask whether an electronics test should be conducted before imaging

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables: -

    Returns: -
    """
    display.clear()
    display.draw_rectangle(0,0,constants.HEIGHT,constants.WIDTH,constants.WHITE)

    display.draw_rectangle(100,130, 30, 30, constants.WHITE)
    display.draw_rectangle(100,170, 30, 30, constants.WHITE)

    display.draw_text(60, 260, "Do you want to conduct an electronics test?", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(110,195, "yes", constants.FONT, constants.WHITE, landscape=True)
    display.draw_text(110,155, "no", constants.FONT, constants.WHITE, landscape=True)



def draw_testing_electronics(display):
    """
    draws the interface which is shown during the electronics test (includes "Notaus" button)

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables:
        i (int): counts from 0 to 3 to draw the 4 button frames

    Returns: -
    """
    display.clear()
    display.draw_rectangle(0,0,constants.HEIGHT,constants.WIDTH,constants.WHITE)
    display.draw_rectangle(0,constants.WIDTH-constants.HEIGHT,constants.HEIGHT,constants.HEIGHT,constants.WHITE)  
    for i in range(4):
        display.draw_rectangle(i*int(constants.HEIGHT/4),0,int(constants.HEIGHT/4), constants.WIDTH-constants.HEIGHT, constants.WHITE)    
    display.draw_rectangle(100,120, 30, 100, constants.WHITE)
    display.draw_text(205,55, "stop", constants.FONT, constants.WHITE, landscape=True)



def draw_test_progress(display, progress):
    """
    draws a progress bar to show the progress of the electronics test

    Args:
        display (ili9341.Display object): specifies the display on which you work
        progress (int): specifies how much the electronics test progressed (from 0-100)

    Variables: -

    Returns: -
    """
    display.fill_hrect(100, 120, 30, progress, constants.WHITE)



def draw_capturing(display):
    """
    draws the interface which is shown during the capturing process ("abbrechen" button instead of zoom options)

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables: 
        i (int): counts from 0 to 3 to draw the 4 button frames

    Returns: -
    """
    display.clear()
    display.draw_rectangle(0,0,constants.HEIGHT,constants.WIDTH,constants.WHITE)              
    display.draw_rectangle(0,constants.WIDTH-constants.HEIGHT,constants.HEIGHT,constants.HEIGHT,constants.WHITE)  
    for i in range(4):
        display.draw_rectangle(i*int(constants.HEIGHT/4),0,int(constants.HEIGHT/4), constants.WIDTH-constants.HEIGHT, constants.WHITE)    

    display.draw_text(85,60, "abort", constants.FONT, constants.WHITE, landscape=True)
    
    display.draw_text(205,55, "stop", constants.FONT, constants.WHITE, landscape=True)



def draw_captured(display):
    """
    draws the "speichern" option which is only available after an image was successfully captured

    Args:
        display (ili9341.Display object): specifies the display on which you work

    Variables: -

    Returns: -
    """
    display.draw_text(145,75, "save", constants.FONT, constants.WHITE, landscape=True)



def draw_value(display, x, y, value):
    """
    interpolates reading of the photomultiplier and draws it as a shade of grey on its specific position on the screen

    Args:
        display (ili9341.Display object): specifies the display on which you work
        x (int): x - coordinate of pixel
        y (int): y - coordinate of pixel
        value (int): value of photomultiplier reading

    Variables: 
        shade (int): interpolated value of photomultiplier reading (value between 0 and 255)
        color (ili9341.color565 object): shade as a color object which can be shown on the screen
    
    Returns: -
    """
    shade = int(value/(4095/255))
    color = ili9341.color565(shade, shade, shade)
    display.draw_pixel(x+1,y+constants.WIDTH-constants.HEIGHT+1,color)