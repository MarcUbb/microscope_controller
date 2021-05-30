import machine
import constants
import uos
import utime

"""
def init_sd():
    sd_card = machine.SDCard(sck=constants.CLK_SD, miso=constants.MISO_SD, mosi=constants.MOSI_SD, cs=constants.CS_SD)
    return(sd_card)"""


def save_image(): # saves image
    uos.rename("image.csv", "image_" + str(utime.time()) + ".csv")