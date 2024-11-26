# 1. 인스톨을 먼저 한다 pip install pynput
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def type_macro():
    # 키보드 매크로 함수
    # ms_delay(1000)(기계제어라서 그럼)
    time.sleep(2)
    keyboard.type("안녕하세요")#문자열 입력
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)#엔터 키 입력
    time.sleep(2)
    #Ctrl+C 입력
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')

#함수 호출 및 실행
if __name__ == "__main__":
    print("2초 후 매크로 실행.")
    type_macro()

