import uos
import utime


def save_image(): # saves image
    uos.rename("image.csv", "image_" + str(utime.time()) + ".csv")