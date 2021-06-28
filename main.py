import os
import pyodbc
import win32gui
from time import sleep
from inv import *
import win32gui
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class WindowCapture:
    hwnd = None
    path = None
    def __init__(self, window_name=None, path=None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                driverpath = "drivers\msodbcsql.msi"
                sqldriver = ( "ODBC Driver 17 for SQL Server")
                windowname = ("Microsoft ODBC Driver 17 for SQL Server Setup")
                dlist = pyodbc.drivers()
                if sqldriver in dlist:
                    print("Driver ok")
                    mainloop()
                elif sqldriver is not dlist:
                    os.startfile(driverpath)
windowname = ("Microsoft ODBC Driver 17 for SQL Server Setup")
wincap = WindowCapture(windowname)