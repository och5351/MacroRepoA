import pyautogui as p
import time as t
import threading
from PIL import ImageGrab as imgGrab

def mouseInit(): # 마우스 중앙 초기화
    monitorSize = p.size() # 해상도 추출
    p.moveTo(monitorSize[0] / 2, monitorSize[1] / 2, duration=0.1) # 해상도 x,y /2 위치 이동
    # p.click(x=monitorSize[0] / 2, y=monitorSize[1] / 2,clicks=2, button='left')
    # screen = imgGrab.grab() # 색상 추출
    # print(screen.getpixel(p.position()))

if __name__ == '__main__':
    mouseInit()
    t.sleep(0.2)
    p.click(button='left')
    hp = p.locateCenterOnScreen('HP.PNG', confidence=0.9)
    p.moveTo(x=hp[0]+160,y=hp[1],duration=0.1)
    screen = imgGrab.grab()  # 색상 추출
    print(screen.getpixel(p.position()))

