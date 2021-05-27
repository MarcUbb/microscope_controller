import machine
import constants


def init_sd():
    sd_card = machine.SDCard(sck=constants.CLK_SD, miso=constants.MISO_SD, mosi=constants.MOSI_SD, cs=constants.CS_SD, freq=20000000)
    return(sd_card)


def save_image(): # saves image
    pass