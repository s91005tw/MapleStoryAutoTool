#test
#test2
#test3
import win32gui
import win32con

#hwnd = win32gui.FindWindow('MapleSroty.exe', None)
import tkinter as tk
import ctypes

import win32api
import win32process
#import win32con
#import ctypes

from ctypes import wintypes as w

hwnd = win32gui.FindWindow(None, 'MapleStory')



pos = win32gui.GetWindowRect(hwnd)



#print(hwnd)
# hwnd = win32gui.FindWindow('xx.exe', None)
# 窗口需要正常大小且在后台，不能最小化
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
# 窗口需要最大化且在后台，不能最小化
# ctypes.windll.user32.ShowWindow(hwnd, 3)
win32gui.SetForegroundWindow(hwnd)


win32gui.SetWindowPos(hwnd, win32con.HWND_DESKTOP, 0,0,0,0, win32con.SWP_NOSIZE)   


print('MapleStory =', hwnd)

print('pos =', pos[0])
print('pos =', pos)

toolpos = '+%d+%d' %(pos[2], pos[1])

window = tk.Tk()
window.title('GUI')
window.geometry('380x400')
window.resizable(False, False)
#window.iconbitmap('icon.ico')


window.geometry(toolpos)




import ctypes as c
from ctypes import wintypes as w

pid = 23432  # Minesweeper

k32 = c.WinDLL('kernel32', use_last_error=True)

OpenProcess = k32.OpenProcess
OpenProcess.argtypes = w.DWORD,w.BOOL,w.DWORD
OpenProcess.restype = w.HANDLE

ReadProcessMemory = k32.ReadProcessMemory
ReadProcessMemory.argtypes = w.HANDLE,w.LPCVOID,w.LPVOID,c.c_size_t,c.POINTER(c.c_size_t)
ReadProcessMemory.restype = w.BOOL

CloseHandle = k32.CloseHandle
CloseHandle.argtypes = [w.HANDLE]
CloseHandle.restype = w.BOOL

processHandle = OpenProcess(0x10, False, pid)

addr = 0x146475F88  # Minesweeper.exe module base address
data = c.c_ulonglong()
bytesRead = c.c_ulonglong()
result = ReadProcessMemory(processHandle, addr, c.byref(data), c.sizeof(data), c.byref(bytesRead))
e = c.get_last_error()

print('result: {}, err code: {}, bytesRead: {}'.format(result,e,bytesRead.value))
print('data: {:016X}h'.format(data.value))


offsets = [0x23BC]


offsets.append(None)

for offset in offsets:
    # Read the memory of current address using ReadProcessMemory
    ###ctypes.windll.kernel32.ReadProcessMemory(h_process, current_address, ctypes.byref(data), ctypes.sizeof(data), ctypes.byref(bytesRead))
    #result = ReadProcessMemory(h_process, current_address, ctypes.byref(data), ctypes.sizeof(data), ctypes.byref(bytesRead))
    print(offset)
    result = ReadProcessMemory(processHandle, addr, c.byref(data), c.sizeof(data), c.byref(bytesRead))
    e = c.get_last_error()

    print('offser data: {:016X}h'.format(data.value))

    # If current offset is `None`, return the value of the last offset
    if offset:
        # Replace the address with the new data address
        current_address = data.value + offset
        print(current_address)


result = ReadProcessMemory(processHandle, current_address, c.byref(data), c.sizeof(data), c.byref(bytesRead))
e = c.get_last_error()
print("")
print('offser result: {}, err code: {}, bytesRead: {}'.format(result,e,bytesRead.value))
print('offser data: {:016X}h'.format(data.value))


CloseHandle(processHandle)



test = tk.Button(text="測試")
test.pack(side="top")

j = data.value

i = 'my label = %d' %(j)

label = tk.Label(text= i, font=("Arial", 14, "bold"), padx=5, pady=5, bg="red", fg="yellow")

label.pack()


window.mainloop()