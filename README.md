# microscope_controller
I use this repository to present to you a project of mine. Goal is to DIY a working eletrone microscope just like Ben Krasnow did some years ago but simplified. You will find the source code for the controller here. 

The idea is to use an old oscilloscope to focus an electrone beam on the speciment. The electrones knocked out are collected by a photomultiplier which converts them into electrical signals. These signals are shown on a screen on their corresponding position. Scanning an rectangular area results in the whole image being produced.

The controller consists of an ESP32 which is connected to an ili9341 touchscreen and 2 stepper motors. For the ili9341 I use the library by rdagger: https://github.com/rdagger/micropython-ili9341 and for the stepper motors the library by zhcong: https://github.com/zhcong/ULN2003-for-ESP32.

## Schematic
In this project I used the ESP32-WROOM-32 board. There are several devices connected to the ESP. Down below you will find a schematic of all the connected pins.
![GitHub Logo](/images/schematic.PNG)

### ESP32
I choose the ESP32 for this project because it has many GPIO Pins and is relatively powerful and cheap. A very helpful companion was: https://unsinnsbasis.de/wp-content/uploads/2020/11/ESP32_Pin-Belegung.pdf.

### Ili9341 & Xpt2046
The Ili9341 is the interface for the user. It features a touchscreen which I completely controll via the library provided by rdagger https://github.com/rdagger/micropython-ili9341.

### 28BYJ-48 & ULN2003
The 28BYJ-48 is a very cheap but precise option when it comes to stepper motors. In my project I used them to precisely controll the electrone beam by turning the potentiometers of the oscilloscope precisely. I did this because the DA-Converter of the ESP32 were not nearly precise or quick enough for this task and controlling the beam this way was much more convenient than controlling it electronically. I used the library by zhcong: https://github.com/zhcong/ULN2003-for-ESP32.

## Parts List
* ESP32-WROOM-32: https://www.amazon.com/dp/B08246MCL5/
* Ili9341 Board: https://www.amazon.com/-/de/dp/B087C3PP9G/
* 28BYJ-48 & ULN2003: https://www.amazon.com/dp/B086D5SXPV/
* Oscilloscope: https://www.conrad.de/de/p/analog-oszilloskop-voltcraft-ao-610-10-mhz-1-kanal-122413.html
* Photomultiplier: Hamamatsu R928
* Vacuum Pump: -

## See also:
* Ben Krasnow Blog: https://benkrasnow.blogspot.com/2011/03/diy-scanning-electron-microscope.html
* Everhardt-Thornley-Detector: https://en.wikipedia.org/wiki/Everhart-Thornley_detector
