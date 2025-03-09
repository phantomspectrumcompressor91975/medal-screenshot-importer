import win32gui
import win32con
import win32api
import win32process
import ctypes
from time import sleep


with open("windowTitle.txt", "r", encoding="utf-8") as wt:
    windowTitle = wt.read()
    wt.close()


def overwrite(hwnd):
    if not hwnd:
        print("Window not found!")
        exit()
    
    


GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
def getWindowTitleByHandle(hwnd):
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value

def compare(thing): return len(thing.lower().split(windowTitle.lower())) > 1

while True:
    hwnd = win32gui.GetForegroundWindow()
    title = getWindowTitleByHandle(hwnd)
    if compare(title):
        overwrite(hwnd)
        break
    else:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        try:
            hndl = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, pid)
        except: pass
        else:
            path = str(win32process.GetModuleFileNameEx(hndl, 0))
            if compare(path):
                overwrite(hwnd)
                break
    
    sleep(0.2)
    continue