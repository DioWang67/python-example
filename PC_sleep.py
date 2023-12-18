import ctypes
import platform
import time

def suspend_computer():
    system_platform = platform.system()

    if system_platform == "Windows":
        # 載入 powrprof.dll
        powrprof = ctypes.windll.LoadLibrary("powrprof.dll")
        
        # 呼叫 SetSuspendState 函數
        result = powrprof.SetSuspendState(0, 1, 0)
        
        if result == 0:
            print("電腦成功進入休眠狀態")
        else:
            print("電腦進入休眠狀態失敗")
    elif system_platform == "Linux":
        # 在 Linux 上，可以使用 os.system 調用 pm-suspend 命令
        os.system("sudo pm-suspend")
    else:
        print("不支持的操作系统")

# 呼叫函數來使計算機休眠
suspend_computer()

# 停頓一段時間，以便查看效果
time.sleep(5)
