# 1. 인스톨을 먼저 한다 pip install pyautogui
import pyautogui
import time

# time.sleep(2) #2초 대기 후 좌표 출력
# print(pyautogui.position())

#사용자 정보 입력
username = "zenki1025"
password = "dltjddn1"

#좌표설정
login_button1 = (1607,580)
login_button2 = (1232,438)
username_field = (1232,438)
login_button3 = (1244,494)
password_field = (1244,494)
login_button4 = (1395,594)

#로그인 버튼1 좌표
#사용자 이름 입력 필드 좌표
#비밀 번호 입력 필드 좌료
#로그인 버튼 좌표

def auto_login():
    time.sleep(2) #시작전 대기 2초

#로그인 창 열기
pyautogui.click(login_button1)

time.sleep(2) #시작전 대기 2초
#사용자 이름 입력
pyautogui.click(username_field)
pyautogui.write(username)

#비밀번호 입력
pyautogui.click(password_field)
pyautogui.write(password)

#로그인 버튼 클릭
pyautogui.click(login_button4)

#실행 및 함수 호출
if __name__ == "__main__":
    print("2초 후 자동 로그인 시작..")
    auto_login()




