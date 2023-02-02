#test
#test2
#test3
import win32gui
import win32con

#hwnd = win32gui.FindWindow('MapleSroty.exe', None)
import tkinter as tk

window = tk.Tk()
window.title('GUI')
window.geometry('380x400')
window.resizable(False, False)
#window.iconbitmap('icon.ico')



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

toolpos = '+%d+%d' %((pos[1]+pos[2]), pos[1])
window.geometry(toolpos)

window.mainloop()