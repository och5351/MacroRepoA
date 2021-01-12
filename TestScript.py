import pyautogui as p
import time as t
import threading
from PIL import ImageGrab as imgGrab

# print(p.position()) # mouse position
# print(p.size()) # 화면 해상도
# print(p.onScreen(1910,1070)) # x,y 좌표 해상도 안에 들어있는지 확인
# p.moveTo(1000,1000,duration=0.3) # 마우스 이동
# p.moveRel(100, 100, duration=0.3) # 현재 위치에서 X, Y 만큼 마우스 이동
# p.dragTo(100, 100, duration=0.5) # 현재 위치에서 X, Y 로 마우스 드래그
# p.dragRel(100, 100, duration=0.5) # 현재 위치에서 X, Y 만큼 이동한 위치로 초 동안 드래그
# p.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

clickChecker = False

def mouseInit(): # 마우스 중앙 초기화
    monitorSize = p.size() # 해상도 추출
    p.moveTo(monitorSize[0] / 2, monitorSize[1] / 2, duration=0.1) # 해상도 x,y /2 위치 이동
    # p.click(x=monitorSize[0] / 2, y=monitorSize[1] / 2,clicks=2, button='left')
    # screen = imgGrab.grab() # 색상 추출
    # print(screen.getpixel(p.position()))

def targetChecker():
    mon = p.locateCenterOnScreen('mon.PNG',confidence=0.9)
    if not mon:
        t.sleep(0.2)
        p.keyDown('ctrl')
        t.sleep(0.2)
        p.keyDown('1')
        p.sleep(0.2)
        p.keyUp('ctrl')
        t.sleep(0.2)
        p.keyUp('14')
        t.sleep(4)
    p.hotkey('tab')
    try:
        target = p.locateCenterOnScreen('target.PNG', confidence=0.9)  # 이미지를 통한 좌표 탐색
        if target:
            attack()
        else:
            p.keyDown('d')
            t.sleep(0.5)
            p.keyUp('d')
    except:
        #p.hotkey('d')
        targetChecker()

def attack():
    t.sleep(0.2)
    p.hotkey('7')
    t.sleep(3.3)
    p.hotkey('6')
    t.sleep(0.6)
    p.hotkey('5')
    t.sleep(0.6)
    p.hotkey('4')
    t.sleep(1.2)
    p.hotkey('9')
    t.sleep(0.6)
    p.hotkey('3')
    t.sleep(3)
    p.hotkey('3')
    t.sleep(0.4)
    p.hotkey('8')
    t.sleep(0.4)
    p.hotkey('2')
    t.sleep(0.5)
    p.hotkey('2')

    monsterhp = p.locateCenterOnScreen('monsterhp.PNG', confidence=0.9)  # 이미지를 통한 좌표 탐색
    print(monsterhp)
    if monsterhp:
        p.hotkey('1')
        t.sleep(3)
        getItem = p.locateCenterOnScreen('getItem.PNG', confidence=0.9)
        exitItem = p.locateCenterOnScreen('itemexit.PNG', confidence=0.9)
        if getItem:
            p.moveTo(x=getItem[0],y=getItem[1],duration=0.1)
            t.sleep(0.2)
            p.click(button='left')
        else:
            p.moveTo(x=exitItem[0], y=exitItem[1], duration=0.1)
            t.sleep(0.2)
            p.click(button='left')

        healthChecker()

    else:
        attack()

# (205, 29, 26) ready
# (28, 38, 56) notReady
def healthChecker():

    hp = p.locateCenterOnScreen('HP.PNG', confidence=0.9)
    p.moveTo(x=hp[0] + 160, y=hp[1], duration=0.1)
    t.sleep(0.2)
    hpStatus = imgGrab.grab().getpixel(p.position()) # 색상 추출
    print(hpStatus)
    if hpStatus[0] != 210:
        print('!!')
        p.hotkey(',')
        t.sleep(10)
        p.hotkey(',')
        healthChecker()
    mpChecker()

def mpChecker():
    mp = p.locateCenterOnScreen('MP.PNG', confidence=0.9)
    p.moveTo(x=mp[0] + 100, y=mp[1], duration=0.1)
    t.sleep(0.2)
    mpStatus = imgGrab.grab().getpixel(p.position())  # 색상 추출
    print(mpStatus)
    if mpStatus[0] != 25:
        print('!!')
        p.hotkey(',')
        t.sleep(10)
        p.hotkey(',')
        mpChecker()


if __name__ == '__main__':
    mouseInit()
    t.sleep(0.2)
    p.click(button='left')
    while True:
        healthChecker()
        targetChecker()
    #t = threading.Thread(checkRGB(),args=(1,10000))
    #t.start()





