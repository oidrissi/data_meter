import time
import threading
from tkinter import *
import psutil
import socket
from requests import get

start_val = 0

def set_data_to_consume():
    print("How Much Data Do you Have left?")
    requested_data = input()
    return (requested_data)

def data(start_val):
    #returns the data consumed while connected
    result = 0

    while True:
        current_val = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        result = current_val - start_val + result
        return (str(convert_to_mo(result)))

def get_ext_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ('My public IP address is: {}'.format(ip))

ip = get_ext_ip()
max_data = set_data_to_consume()
data_left = +
def main():
    kiss = data(start_val)
    display_label['text'] = kiss + ' || Mo Consumed ' + '\n' + (str(ip))
    display_label.pack()
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

app = Tk()
app.title("Data Consumption Monitor")
app.geometry('420x69')
app.configure(background = 'black')
frame = Frame(app)
display_label = Label(frame, font = 'Terminal 15', bg = 'black', fg = '#20C20E')
frame.pack(anchor = CENTER)
main()
app.attributes('-topmost',True)
app.mainloop()