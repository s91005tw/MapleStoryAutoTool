import socket

import win32gui
import win32con
#import win32com.client
import time
import keyboard

hwnd = win32gui.FindWindow(None, 'MapleStory')
print(hwnd)

HOST = '192.168.100.6'
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
win32gui.SetForegroundWindow(hwnd)

# while True:
#     event=keyboard.read_event()
#     print(event.name , event.scan_code)
#     s.send(event.scan_code.to_bytes(2, 'big') )
#     if event.scan_code == 1:
#         break

# from pynput.keyboard import Key, Listener
# def on_press(key):
#     print('{0} pressed'.format(key))
#     print(key)
#     #print(int(str(Key.esc)))
#     #s.send(key.decode())

# def on_release(key):
#     #print('{0} release'.format(key))
#     if key == Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with Listener(on_press=on_press,
#               on_release=on_release) as listener:
#     listener.join()
KEY_DOWN = 'down'
KEY_UP = 'up'


print("record keyboard")

recorded_events = keyboard.record("f1")
#keyboard.play(recorded_events)

while True:
    skiptime = 0
    for i in recorded_events:
        print(i.event_type, i.scan_code, i.time, i.scan_code.to_bytes(2, 'big') )
        if(i.event_type ==KEY_DOWN):
            s.send(i.scan_code.to_bytes(2, 'little'))
            s.send(b'0')
            if(skiptime == 0):
                skiptime = i.time

            time.sleep(i.time - skiptime)
            skiptime = i.time
    time.sleep(1)





s.send(b'Z')
s.send(b'Z')
s.send(b'Z')
s.send(b'Z')
s.send(b'Z')