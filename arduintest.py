import serial
from time import sleep
import sys

import win32gui
import win32con

import win32com.client

hwnd = win32gui.FindWindow(None, 'MapleStory')
print(hwnd)


win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
win32gui.SetForegroundWindow(hwnd)


COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES, bytesize=8, parity='N', stopbits=1, timeout=1)

try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        choice = input('按1開燈、按2關燈、按e關閉程式  ').lower()

        if choice == '1':
            print('傳送開燈指令')
            hwnd = win32gui.FindWindow(None, 'MapleStory')
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(hwnd)
            sleep(0.1)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
            ser.write(b'1\n')  # 訊息必須是位元組類型
            sleep(0.5)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈

        elif choice == '2':
            print('傳送關燈指令')
            ser.write(b'2\n')
            hwnd = win32gui.FindWindow(None, 'MapleStory')
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            # 窗口需要最大化且在后台，不能最小化
            # ctypes.windll.user32.ShowWindow(hwnd, 3)
            win32gui.SetForegroundWindow(hwnd)
            sleep(0.1)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
            sleep(0.5)
        elif choice == 'e':
            ser.close()
            print('再見！')
            sys.exit()
        else:
            print('指令錯誤…')

        while ser.in_waiting:
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            print('控制板回應：', mcu_feedback)

except KeyboardInterrupt:
    ser.close()
    print('再見！')