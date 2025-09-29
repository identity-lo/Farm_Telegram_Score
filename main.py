import pygetwindow as gw 
import time 
import pyautogui as ag 
import random as rm
import pyperclip

TIMEOUT = 20
WINDOWSLEEP = 5
WINDOWTITLE = "مهد کودک"
MESSAGE = [
    "مرگ بر آمریکا" , "مرگ بر اسرائیل", "مرگ بر شاه" , "یا حسین",
    
]

result_func = None

def check_title():
    result_func = gw.getWindowsWithTitle(WINDOWTITLE)[0]
    if result_func : 
        result_func.activate()
        return True
    return False
    
def send_message():
    get_message = rm.choice(MESSAGE)
    pyperclip.copy(get_message)
    ag.hotkey("ctrl" , "v")
    ag.press("enter")

def app():
    
    current_run = False
    
    while True:
        try:
            if check_title():
                if not current_run:
                    print("i found window !")
                    time.sleep(WINDOWSLEEP)
                    current_run = True
                send_message()
                time.sleep(TIMEOUT)
            else:
                assert "telegram not opend !"
                time.sleep(WINDOWSLEEP)
                continue
        except KeyboardInterrupt :
            print("bye !:))") 
            break  
        

if "__main__" == __name__:
    app()


    
        