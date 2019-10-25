# py_ppXAFS_NW14A
a python script for data reduction for pump probe XAFS experiments in NW14A, PF-AR, KEK, Japan
The script was written in python2. Please install python2. I would recommend using anaconda2.
This script nees the following packages.
* numpy
* scipy
* pandas
* natsort
* pyside
If you install python2 from anaconda, you only install natsort and pyside.

If you use the script in windows, the appearance of the script would look weird...
If you want to change the appearance, please edit "UI_ppXAFS_dev.ui" with QtDesigner and make the ".ui" file to a python file with 'pyside-uic'.
pyside-uic 'UI file' -o 'python file'
#If you install pyside with anaconda2, you could not find pyside-uic...

When you install anaconda2, please use older archives. For example, Anaconda2-4.4-0 which was released in May 2017.

This was written for my own use. If you have problems, please let me know(yohei.uemura@gmail.com)
