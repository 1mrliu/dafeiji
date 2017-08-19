# coding = UTF8
import pygame
from pygame.locals import *
import random

'''
使用面向对象的方法实现
'''
        #定义基类
class Base():
    def __init__(self,screen,name):
        #设置要显示内容的窗口
        self.screen = screen
        self.name = name



        #创建一个飞机类，继承自基类
class Plane(Base):
        #重写了基类的__init__方法
    def __init__(self,screen,name):
        super().__init__(screen,name)

        #根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()

        #用来保存飞机的所有导弹
        self.missList = []
        #显示的方法
    def display(self):
        #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))

        #存放需需要删除的对象的信息
        needDelItemList = []

        for i in self.missList:
            if i.judge():
                needDelItemList.append(i)

        for i in needDelItemList:
            self.missList.remove(i)
        #遍历飞机所有的导弹信息
        for daodan in self.missList:
            daodan.display()
            #修改导弹的位置信息
            daodan.move()

    def shedaodan(self):
        mislist = MissLis(self.x,self.y,self.screen,self.name)
        self.missList.append(mislist)
        #创建一个玩家飞机类，继承自飞机类
class GamePlane(Plane):
        #重写




class  Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()

    def move(self):
        self.y -= 2

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def judge(self):
        if self.y<0:
            return True
        else:
            return False


    #敌人飞机的设置
class EnemyPlane(object):
    def __init__(self,screen):

     #设置飞机默认的位置
     self.x = 0
     self.y = 0

     #设置要显示内容的窗口
     self.screen = screen

     self.imageName = "./feiji/enemy-1.gif"

     self.image = pygame.image.load(self.imageName).convert()

     self.direction ='right'

     #用来存储敌人飞机发射的所有子弹

     self.bulletList = []

    def move(self):

        #如果碰到了右边的边界，就往左走，碰到了左边的边界，就往右走

        if   self.direction=='right':
             self.x+=2
        elif self.direction=='left':
             self.x-=2
        if   self.x==480-20:
             self.direction='left'
        elif self.x<0:
             self.direction='right'

    def sheBullet(self):
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))


'''
1.搭建界面
'''

if __name__ == '__main__' :

    # 1.创建一个窗口用来实现窗口
    screen = pygame.display.set_mode((480,890),0,32)

    # 2.创建一个和窗口大小一样的图片，用来放置图片
    background = pygame.image.load("./feiji/background.png").convert()

    #创建一个飞机对象
    heroPlane = HeroPlane(screen)

    #创建一个敌人飞机对象
    enemyPlane = EnemyPlane(screen)


    while True:
        # 设定需要显示的背景图
        screen.blit(background,(0,0))

        heroPlane.display()

        enemyPlane.sheBullet()
        enemyPlane.move()
        enemyPlane.display()


        # 获取事件，比如按键之类
        for event in pygame.event.get():

        # 判断是否是点击了退出按钮

          if event.type == QUIT:
            print("exit")
            exit()
          elif event.type == KEYDOWN:
            #检测键盘是否是a或者left
            if  event.key == K_a or event.key == K_LEFT:

                print('left')
                heroPlane.moveLeft()
                #控制飞机向左移动
                #x-=5
            # 检测键盘是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:

                print('right')
                heroPlane.moveRight()
                #控制飞机向右移动

            # 检测键盘是否是空格
            elif event.key == K_SPACE:
                print("space")
                heroPlane.sheBullet()

        # 更新需要显示的内容
        pygame.display.update()

