#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import random
import win32api
import win32gui
import win32con
from ctypes import *
import sys
from pymouse import PyMouse
from PIL import ImageGrab

def gbk2utf8(s):
    return s.decode('gbk').encode('utf-8')

# 搜索yys窗口
def search():
    hList = []
    rList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hList)
    for h in hList:
        title = win32gui.GetWindowText(h)
        clsname = win32gui.GetClassName(h)
        if clsname == 'Win32Window0' and gbk2utf8(title) == '阴阳师-网易游戏':
            rList.append(h)
    return rList

# 激活窗口
def active(win):
    windll.user32.SwitchToThisWindow(win, True)

# 设置窗口位置和大小
def setPos(win, x, y, w, h):
    win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, x, y, w, h, win32con.SWP_SHOWWINDOW)

def getPos(win):
    return win32gui.GetWindowRect(win)

# 点击窗口的坐标
def click(win, delX, delY):
    left, top, right, bottom = win32gui.GetWindowRect(win)
    PyMouse().click(left + delX, top + delY)

# 点击窗口的范围
def clickRange(win, box):
    (x1, y1, x2, y2) = box
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    click(win, x, y)

# 截图窗口
def capture(win):
    active(win)
    return ImageGrab.grab(win32gui.GetWindowRect(win))

