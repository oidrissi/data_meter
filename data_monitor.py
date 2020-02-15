import time
from tkinter import *
import psutil
import socket


def data(start_val):
    result = 0

    while True:
        current_val = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        result = current_val - start_val + result
        start_val = current_val
        time.sleep(1)
        if is_connected():
            print (str(convert_to_mo(result)))
            return (str(convert_to_mo(result)))
            #timing = time_counter() + timing
        else:
            break  

def main():
    kiss = data(0)
    display_label['text'] = kiss + ' || Mo Consumed '
    display_label.pack ()
    app.after(1000, main)
        
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

def send_stat(value):
    print ("%f" % convert_to_mo(value), "Mo consumed || ", "%f" % (1000 - convert_to_mo(value)), "Mo left")

def time_counter():
    start = time.time()
    time.sleep(0.5)
    elapsed = time.time()
    return (elapsed - start)

app = Tk()
app.title("Data Consumption Monitor")
app.geometry('380x60')
app.configure(background = 'black')
frame = Frame(app, relief= SUNKEN)
display_label = Label(frame, font = 'montserrat 20', bg = 'black', fg = '#20C20E')
frame.pack(side = RIGHT)
main()
app.mainloop()