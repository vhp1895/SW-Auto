#! python3
# auto the fuck out of GB10

import pyautogui
import threading
import sys
import time
import os
import path

# set cwd
os.chdir('C:\\Users\\Administrator\\Desktop\\SW')


def Run(type):
    while pyautogui.locateOnScreen(path.NoEnergy) is None:
        # Chờ tới khi thắng và mở hòm

        while pyautogui.locateOnScreen(path.Victory) is None:
            time.sleep(1)

        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(path.Victory)))
        time.sleep(1)
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(path.Victory)))
        time.sleep(3)

        # Nhận phần thưởng (Có 2 loại phần thưởng: 1 nhận = Get, 2 nhận = OK)
        if pyautogui.locateOnScreen(path.Get) is None:
            pyautogui.click(pyautogui.center(
                pyautogui.locateOnScreen(path.Ok)))
        else:
            pyautogui.click(pyautogui.center(
                pyautogui.locateOnScreen(path.Get)))
        time.sleep(2)

        # Quay lại phase chuẩn bị
        pyautogui.click(pyautogui.center(
            pyautogui.locateOnScreen(eval('path.'+type))))
        time.sleep(1)


def revive():
    while not pyautogui.locateOnScreen(path.Revive):
        time.sleep(10)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Revive)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Revive1)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Revive2)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Revive3)))


def refillSP(type):
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Shop)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.SocialPoint)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.RefillConfirm)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.DoneRefill)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.CloseRefill)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(eval('path.'+type))))
    time.sleep(2)


def refillCrystal(type):
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Shop)))
    time.sleep(3)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.Crystal)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.RefillConfirm)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.DoneRefill)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(path.CloseRefill)))
    time.sleep(2)
    pyautogui.click(pyautogui.center(
        pyautogui.locateOnScreen(eval('path.'+type))))
    time.sleep(2)


def Dungeon(type, SP, xtal):
    # Chạy trước 1 vòng đến khi hết energy
    print(type)
    print(SP)
    print(xtal)
    Run(type)
    Revive = threading.Thread(target=revive)
    Revive.start()
    # Làm gì nếu có hoặc không refill
    if int(SP) > 0 and int(xtal) == 0:
        for k in range(1, int(SP) + 1):
            refillSP(type)
            Run(type)
            print('Đã chạy ' + str(k) + ' vòng')
    elif int(xtal) > 0 and int(SP) == 0:
        for k in range(1, int(xtal) + 1):
            refillCrystal(type)
            Run(type)
            print('Đã chạy ' + str(k) + ' vòng')
    elif int(xtal) > 0 and int(SP) > 0:
        for k in range(1, int(SP) + 1):
            refillSP(type)
            Run(type)
            print('Đã chạy ' + str(k) + ' vòng Social Point')
        for k in range(1, int(xtal) + 1):
            refillCrystal(type)
            Run(type)
            print('Đã chạy ' + str(k) + ' vòng Crystal')
    elif int(SP) == 0 and int(xtal) == 0:
        print('Xong!')
    else:
        print('Số Âm!')


def main():
    type = sys.argv[1]
    SP = sys.argv[2]
    xtal = sys.argv[3]
    Dungeon(type, SP, xtal)


if __name__ == '__main__':
    main()
