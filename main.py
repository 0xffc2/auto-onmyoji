#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append(r'libs')
from win import *
from game import *
from PIL import Image
import time


rangeRB = (420, 280, 490, 300)

wins = search()

if len(wins) == 0:
    print "no onmyoji !!!"
    sys.exit()

mode = 0

if len(wins) == 1:
    mode = 1
    print 'single mode'
elif len(wins) == 2:
    print 'multi mode'
else:
    print 'too many onmyoji !!!'
    sys.exit()

def checkAct(win):
    if isInvite(win):
        return 'invite'
    if isGame(win):
        return 'game'
    if singleStart(win):
        return 'start'
    if multiStart(win):
        return 'mstart'
    if inRoom(win):
        return 'room'
    if isRedEgg(win):
        return 'redegg'
    if isRedEggOpen(win):
        return 'redeggopen'
    if isVic(win):
        return 'vic'
    if isVic2(win):
        return 'vic2'
    return 'unknown'

if mode == 1:
    # 单人模式
    win = wins[0]
    setPos(win, 0, 0, 0, 350)
    act = 'start'
    while 1:
        print act
        if act == 'start':
            if singleStart(win):
                # print 'start'
                clickRange(win, singleStartBox)
                time.sleep(1) # 7秒转场
        elif act == 'game':
            if isGame(win):
                # print 'in game!!!' # 在游戏中就停顿2秒
                time.sleep(1)
        elif act == 'vic':
            if isVic(win):
                # print 'win!!!'
                clickRange(win, vicStartBox)
                time.sleep(1)
                clickRange(win, redEggBox)
                time.sleep(1)
                clickRange(win, redEggOpenBox)
                time.sleep(1)
        elif act == 'redegg':
            if isRedEgg(win):
                # print 'redegg'
                clickRange(win, redEggBox)
                time.sleep(1)
                clickRange(win, redEggOpenBox)
                time.sleep(1)
        elif act == 'redeggopen':
            if isRedEggOpen(win):
                # print 'redeggopen'
                clickRange(win, redEggOpenBox)
                time.sleep(1)
        elif act == 'invite':
            if isInvite(win):
                # print 'invite!!!'
                clickRange(win, inviteBox)
                time.sleep(1)
        time.sleep(1)
        act = checkAct(win)
        continue
else:
    # 双人模式
    masterWin = None
    win2 = None
    setPos(wins[0], 0, 0, 0, 350)
    a = input('is master? (0|1)')
    if a == 1:
        masterWin = wins[0]
        win2 = wins[1]
    else:
        masterWin = wins[1]
        win2 = wins[0]
    setPos(masterWin, 0, 0, 0, 350)
    setPos(win2, 0, 350, 0, 350)

    act = 'start'
    act2 = 'game'
    while 1:
        print act, act2
        gameslp = 0
        vicslp = 0
        reslp = 0
        reoslp = 0
        inviteslp = 0
        startslp = 0

        maybereg = 0

        if act2 == 'game':
            if isGame(win2):
                # print 'p2 in game!!!'
                gameslp = 1
        elif act2 == 'vic2':
            if isVic2(win2):
                # print 'p2 win!!!'
                maybereg = 1
                clickRange(win2, vic2StartBox)
                vicslp = 1
        elif act2 == 'redegg':
            if isRedEgg(win2):
                # print 'p2 redegg'
                maybereg = 1
                clickRange(win2, redEggBox)
                reslp = 1
        elif act2 == 'redeggopen':
            if isRedEggOpen(win2):
                # print 'p2 redeggopen'
                maybereg = 1
                clickRange(win2, redEggOpenBox)
                reoslp = 1
        elif act2 == 'invite':
            if isInvite(win2):
                # print 'p2 invite!!!'
                clickRange(win2, inviteBox)
                inviteslp = 1

        if act == 'mstart':
            if multiStart(masterWin):
                # print 'start'
                clickRange(masterWin, multiStartBox)
                startslp = 1
        elif act == 'game':
            if isGame(masterWin):
                # print 'in game!!!' # 在游戏中就停顿2秒
                gameslp = 1
        elif act == 'vic2':
            if isVic2(masterWin):
                # print 'win!!!'
                maybereg = 1
                clickRange(masterWin, vic2StartBox)
                vicslp = 1
        elif act == 'redegg':
            if isRedEgg(masterWin):
                # print 'redegg'
                clickRange(masterWin, redEggBox)
                reslp = 1
        elif act == 'redeggopen':
            if isRedEggOpen(masterWin):
                # print 'redeggopen'
                clickRange(masterWin, redEggOpenBox)
                reoslp = 1
        elif act == 'invite':
            if isInvite(masterWin):
                # print 'invite!!!'
                clickRange(masterWin, inviteBox)
                inviteslp = 1
        if maybereg == 1: # 可能是结束， 两边都点一下右下角
            clickRange(masterWin, rangeRB)


        time.sleep(gameslp + vicslp + reslp + reoslp + inviteslp + startslp)
        act = checkAct(masterWin)
        act2 = checkAct(win2)
        continue
