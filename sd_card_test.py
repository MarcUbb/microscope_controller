import machine
import os
import sdcard

SD_SCK = machine.Pin(18)
SD_CS = machine.Pin(12)
SD_MOSI = machine.Pin(23)
SD_MISO = machine.Pin(19)
print("bruh")
spisd = machine.SPI(-1, miso=SD_MISO, mosi = SD_MOSI, sck = SD_SCK)
print("bruh")
sd = sdcard.SDCard(spisd, SD_CS)

print("Root directory:{}".format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")
print("Root directory:{}".format(os.listdir()))
os.chdir("sd")
print("SD Card contains:{}".format(os.listdir()))