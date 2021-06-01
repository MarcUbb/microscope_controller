# microscope_controller
In this repository you find the source code for the controller of an electrone microscope. The controller consists of an ESP32 which is connected to an ili9341 touchscreen. I use a library by rdagger2 (under "library" directory) who you can also find on GitHub to controll the screen and touchcontroller.

## ESP32
In this project I used the ESP32-WROOM-32 board. There are several devices connected to the ESP. Down below you will find a schematic and a list of all the connected pins.

### Schematic

### List

ESP32|Ili9341|Xpt2046|Ys-4Relay|Photomultiplier|Cathode-Ray-Tube|5v-PSU
-----|-------|-------|---------|---------------|----------------|------
3V3||||||
EN||||||
GND||||||
5V||||||
GPIO 0||||||
GPIO 1||||||
GPIO 2||||||
GPIO 3||||||
GPIO 4||||||
GPIO 5||||||
GPIO 6||||||
GPIO 7||||||
GPIO 8||||||
GPIO 9||||||
GPIO 10||||||
GPIO 11||||||
GPIO 12||||||
GPIO 13||||||
GPIO 14||||||
GPIO 15||||||
GPIO 16||||||
GPIO 17||||||
GPIO 18||||||
GPIO 19||||||
GPIO 21||||||
GPIO 22||||||
GPIO 23||||||
GPIO 25||||||
GPIO 26||||||
GPIO 27||||||
GPIO 32||||||
GPIO 33||||||
GPIO 34||||||
GPIO 35||||||
GPIO 36||||||
GPIO 39||||||


## Ili9341&Xpt2046
The Ili9341 is the interface for the user. It features a touchscreen which I controller via the library provided by rdagger https://github.com/rdagger/micropython-ili9341.

## Parts List
* ESP32-WROOM-32: https://www.amazon.de/gp/product/B074RGW2VQ/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1
* Ili9341 Board:https://www.amazon.de/gp/product/B017FZTIO6/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
* YS-4Relay: https://www.ebay.de/itm/273521283119
* Oscilloscope: https://www.conrad.de/de/p/analog-oszilloskop-voltcraft-ao-610-10-mhz-1-kanal-122413.html
* Photomultiplier: M10FS300
* Vacuum Pump: -

## Requirements
* Micropython flashed to an Microcontroller
* Matplotlib and tkinter installed on your Python
* 3.3v Relais
