import socket

import win32gui
import win32con
import win32com.client


import keyboard


hwnd = win32gui.FindWindow(None, 'MapleStory')
print(hwnd)

HOST = '192.168.100.6'
PORT = 8088






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
win32gui.SetForegroundWindow(hwnd)

while True:
    event=keyboard.read_event()
    print(event.name , event.scan_code)
    s.send(event.scan_code.to_bytes(2, 'big') )
    if event.scan_code == 1:
        break


# from pynput.keyboard import Key, Listener
# def on_press(key):
#     print('{0} pressed'.format(key))
#     s.send(key.key_to_scan_codes)
# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with Listener(on_press=on_press,
#               on_release=on_release) as listener:
#     listener.join()

# import keyboard  # using module keyboard
# recorded_events = keyboard.record("space")
# keyboard.play(recorded_events)

# print(recorded_events)




