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

addr = 0x147F67278 # Minesweeper.exe module base address
data = c.c_ulonglong()
bytesRead = c.c_ulonglong()
result = ReadProcessMemory(processHandle, addr, c.byref(data), c.sizeof(data), c.byref(bytesRead))
e = c.get_last_error()

print('result: {}, err code: {}, bytesRead: {}'.format(result,e,bytesRead.value))
print('data: {:016X}h'.format(data.value))


offsets = [0x28, 0x19300]


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