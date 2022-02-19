import time
from tkinter import *
import psutil
import socket
from requests import get
from datetime import datetime

start_val = 0

def set_data_to_consume():
    print("How Much Data Do you Have Left? (In Go)")
    requested_data = input()
    return (requested_data)

def set_days_left():
    print("How Many Days Left Till next Subscription?")
    days_until_renewal = input()
    return (days_until_renewal)

def data(start_val):
    #returns the data consumed while connected
    result = 0

    while True:
        current_val = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        result = current_val - start_val + result
        return (convert_to_mo(result))

def get_ext_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ('My public IP address is: {}'.format(ip))

def checkIfMidnight():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    return (seconds_since_midnight == 0)

def convert_to_mo(value):
    #1 octet = 1 byte = 8 bits // 1024 bytes = 8192 bits = 1 kb;
    return value/1000000

ip = get_ext_ip()
max_data = float(set_data_to_consume()) * 1000 + data(start_val)
# days_left = int(set_days_left())

def main():
    kiss = data(start_val)
    left = max_data - kiss
    #  + '\n' + (str(days_left)) + ' days left until next subscription'
    display_label['text'] = str(kiss) + ' || Mo Consumed ' + '\n' + (str(ip)) + '\n' + (str(left)) + ' || Mo Left '
    display_label.pack()
    app.after(5, main)

app = Tk()
app.title("Data Consumption Monitor")
app.geometry(f'{250}x{40}+{-15}+{698}')
app.configure(background = 'black')
frame = Frame(app)
display_label = Label(frame, font = 'Terminal 6', bg = 'black', fg = '#20C20E')
frame.pack(anchor = CENTER)
main()
app.attributes('-topmost',True)
app.mainloop()