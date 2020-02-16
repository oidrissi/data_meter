import time
import threading
from tkinter import *
import psutil
import socket
from ctypes import windll, Structure, c_long, byref

class POINT(Structure):
    #Structure to store x and y position of cursor
    _fields_ = [("x", c_long), ("y", c_long)]

timer = None

def data(start_val):
    #returns the data consumed while connected
    start_val = 0
    result = 0
    global timer

    while True:
        current_val = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        result = current_val - start_val + result
        start_val = current_val
        timer = threading.Timer(1.0, data)
        timer.start()
        if is_connected():
            return (str(convert_to_mo(result)))
        else:    
            break

def idle_data(start_val):
    #returns the data consumed while afk
    result = 0
    global timer

    if idle():
        while idle():
            current_val = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            result = current_val - start_val + result
            start_val = current_val
            timer = threading.Timer(1.0, idle_data)
            timer.start()
            if is_connected():
                    return (str(convert_to_mo(result)))
            else:
                break
    else:
        return None


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


def idle():
    global timer
    pos = queryMousePosition()
    timer = threading.Timer(3.0, idle)
    timer.start()
    pos2 = queryMousePosition()
    timer.cancel()
    if pos == pos2:
        return True

def main():
    kiss = data(0)
    #face = idle_data(0)
    display_label['text'] = str(kiss) + ' || Mo Consumed '
    #sec_label['text'] = str(face) + ' || While Idle'
    display_label.pack()
    #sec_label.pack()
    app.after(5, main)
        
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def convert_to_mo(value):
    #1 octet = 1 byte = 8 bits // 1024 bytes = 8192 bits = 1 kb;
    return value/1000000

#def send_stat(value):
#    print ("%f" % convert_to_mo(value), "Mo consumed || ", "%f" % (1000 - convert_to_mo(value)), "Mo left")


app = Tk()
app.title("Data Consumption Monitor")
app.geometry('420x300')
app.configure(background = 'black')
frame = Frame(app)
display_label = Label(frame, font = 'montserrat 20', bg = 'black', fg = '#20C20E')
sec_label = Label(frame, font = 'montserrat 20', bg = 'black', fg = '#20C20E')
frame.pack(side = RIGHT)
main()
app.mainloop()