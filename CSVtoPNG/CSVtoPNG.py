import matplotlib.pyplot as plt
import csv
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import webbrowser
import os
import shutil


csv_path = ""
png_path = ""
default_path = os.getcwd() + "\image.png"

window = Tk()
image_label = Label(window, width = 640, height = 480)


def application():
    global window
    global image_label
    window.geometry("640x500")
    p1 = PhotoImage(file = "icon.png")
    window.iconphoto(False, p1)
    window.title("CSV to PNG converter")
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Open", command = browse_files)
    filemenu.add_command(label = "Save as...", command = save_file, state = DISABLED)

    menubar.add_cascade(label = "File", menu = filemenu)

    helpmenu = Menu(menubar, tearoff = 0)
    helpmenu.add_command(label = "About...", command=open_github)
    menubar.add_cascade(label = "Help", menu = helpmenu)

    
    image_label.pack()
    
    
    window.config(menu = menubar)
    window.mainloop()


def open_github():
    webbrowser.open("https://github.com/MarcUbb/microscope_controller")

def load_image():
    global csv_path
    global window
    global image_label
    global default_path

    image = []

    with open(csv_path, newline='\n') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        
        for line in data:
            image.append(line)

    i = 0
    while i < len(image):
        j = 0
        while j < len(image[0]):
            image[i][j] = int(image[i][j])
            j += 1
        i += 1
    
    plt.imshow(image, cmap= "Greys")
    plt.savefig(default_path)

  
    img = PhotoImage(file = default_path)
    image_label.configure(image = img)
    image_label.image = img


def save_image():
    global default_path
    global png_path

    png_path = str(png_path)
    png_path = png_path[25:-29]

    shutil.move(default_path, png_path)


def browse_files():
    filepath = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV File","*.csv*"),("all files","*.*")))
    global csv_path 
    csv_path = filepath

    global load_image

    load_image()

def save_file():
    filepath = asksaveasfile(initialfile = "Untitled.png", defaultextension = ".png",filetypes = [("All Files","*.*")])
    global png_path
    png_path = filepath

    global save_image
    save_image()


def main():
    application()


if __name__ == "__main__":
    main()