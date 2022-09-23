import time
import pyautogui
import random

pyautogui.PAUSE = 0.1


def testClickEvent():
    btpoing = pyautogui.locateOnScreen('bt.png')
    x, y = pyautogui.center(btpoing)
    #pyautogui.click(x, y)
    print(x, y)
    print('-----------------------------')
    while(True):
        print(pyautogui.position())
        time.sleep(1)

    '''
    st = time.time()
    clickButton()
    et = time.time()
    print("执行时长(秒)：")
    print(et-st)

    ''' 
    quit()
#testClickEvent()


'''--------------------正式调用事件--------------------'''


def clickButton():
    counti = 30
    movex = 195
    isleft = True
    countRC = 1

    pyautogui.click()
    
    while (counti>=0):
        currentMouseX, currentMouseY = pyautogui.position()
        counti -= 1
        if isleft:
            countRC = randomClient(currentMouseX + movex, currentMouseY, countRC)
            isleft = False
        else:
            countRC = randomClient(currentMouseX - movex, currentMouseY, countRC)
            isleft = True

        #print(isleft, currentMouseX)


def randomClient(movex, movey, ccrc):
    pyautogui.moveTo(movex, movey)
    if(ccrc <= 2):
        pyautogui.click()
    else:
        ri = random.randint(1,3)
        for i in range(1,ri):
            pyautogui.click(button='left', clicks=2)
    return ccrc + 1


# 整点前的最后0.5秒开始执行点击事件
print('事件已正常启动，整点将会执行䇋交叉点击事件！点击操作将持续5-10秒.')
while True:
    ct = time.time()
    ts = time.strftime('%M%S', time.localtime(ct))
    time_stamp = "%s%03d" % (ts, (ct - int(ct)) * 1000)
    #print(time_stamp)

    if int(time_stamp) >= 5959500:
        st = time.time()
        clickButton()
        et = time.time()
        print("执行时长(秒)：")
        print(et-st)
        break




