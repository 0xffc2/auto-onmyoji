#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,sys
from win import *
from PIL import Image
import imagehash

width = 568
height = 350

dataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
singleStartJPG = os.path.join(dataPath, 'single-start.jpeg') # 单人开始界面
multiStartJPG = os.path.join(dataPath, 'multi-start.jpeg') # 多人房间（房主）
otherInviteJPG = os.path.join(dataPath, 'other-invite.jpeg') # 悬赏邀请
gameJPG = os.path.join(dataPath, 'game.jpeg') # 正在游戏中
vicJPG = os.path.join(dataPath, 'vic.jpeg') # 胜利结算界面
vic2JPG = os.path.join(dataPath, 'vic2.jpeg') # 2人胜利结算界面
redEggJPG = os.path.join(dataPath, 'red-egg.jpeg') # 红蛋
redEggOpenJPG = os.path.join(dataPath, 'red-egg-open.jpeg') # 红蛋开

inviteBox = (365, 245, 385, 265)
inviteWHash = imagehash.whash(Image.open(otherInviteJPG).crop(inviteBox))

gameBox = (20, 300, 50, 330)
gameWHash = imagehash.whash(Image.open(gameJPG).crop(gameBox))

multiStartBox = (420, 280, 490, 300)
multiStartWHash = imagehash.whash(Image.open(multiStartJPG).crop(multiStartBox))

redEggBox = (230, 130, 330, 230)
regEggWHash = imagehash.whash(Image.open(redEggJPG).crop(redEggBox))

redEggOpenBox = (230, 280, 350, 300) #(230, 200, 330, 300)
regEggOpenWHash = imagehash.whash(Image.open(redEggOpenJPG).crop(redEggOpenBox))

singleStartBox = (395, 235, 440, 255)
singleStartWHash = imagehash.whash(Image.open(singleStartJPG).crop(singleStartBox))

vicStartBox = (180, 80, 250, 150)
vicStartWHash = imagehash.whash(Image.open(vicJPG).crop(vicStartBox))

vic2StartBox = (180, 60, 250, 130)
vic2StartWHash = imagehash.whash(Image.open(vic2JPG).crop(vic2StartBox))

existRoomBox = (80, 280, 140, 300)
existRoomWHash = imagehash.whash(Image.open(multiStartJPG).crop(existRoomBox))

# 是否有人邀请
def isInvite(win):
    pic = capture(win)
    no = pic.crop(inviteBox)
    return like(no, inviteWHash)

def isGame(win):
    pic = capture(win)
    no = pic.crop(gameBox)
    return like(no, gameWHash)

def singleStart(win):
    pic = capture(win)
    no = pic.crop(singleStartBox)
    return like(no, singleStartWHash)

def inRoom(win):
    pic = capture(win)
    no = pic.crop(existRoomBox)
    return like(no, existRoomWHash)

def multiStart(win):
    pic = capture(win)
    no = pic.crop(multiStartBox)
    pix = no.getpixel((10, 10))
    avg = sum(pix) / len(pix)
    sdsq = sum([(i - avg) ** 2 for i in pix])
    stdev = (sdsq / (len(pix) - 1)) ** .5
    return stdev > 70 and like(no, multiStartWHash)

def isRedEgg(win):
    pic = capture(win)
    no = pic.crop(redEggBox)
    return like(no, regEggWHash)

def isRedEggOpen(win):
    pic = capture(win)
    no = pic.crop(redEggOpenBox)
    return like(no, regEggOpenWHash)

def isVic(win):
    pic = capture(win)
    no = pic.crop(vicStartBox)
    return like(no, vicStartWHash)

def isVic2(win):
    pic = capture(win)
    no = pic.crop(vic2StartBox)
    return like(no, vic2StartWHash)

def like(img, hs):
    return imagehash.whash(img) - hs < 10



# 360 200      390     230   yes 按钮
# 360 240      390     270   no  按钮