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
        mislist = MissList(self.x,self.y,self.screen,self.name)
        self.missList.append(mislist)
        #创建一个玩家飞机类，继承自飞机类
class GamePlane(Plane):
        #重写父类的方法
        def __init__(self,screen,name):
            #设置玩家飞机的默认位置
            self.x = 230
            self.y = 600
            self.imageName = './feiji/hero.gif'

            super().__init__(screen,name)



        #向左移动
        def moveLeft(self):
            self.x-=10
        #向右移动
        def moveRight(self):
            self.x+=10
        def shedaodan(self):
            super().shedaodan()

        #创建一个敌人飞机类,继承自飞机类
class EnemyPlane(Plane):
        #重写父类的__init__方法
        def __init__(self,screen,name):
        #设置敌机的默认位置
            self.x=0
            self.y=0
            self.imageName='./feiji/enemy-1.gif'
        #调用父类的__init__方法
            super().__init__(screen,name)
            self.direction='right'
        def move(self):
            #如果碰到了右边的边界就往左走，如果碰到了左边的就往右走
            if self.direction=='right':
                self.x+=2
            elif self.direction=='left':
                self.x-=2
            if self.x > 480-50:
                self.direction='left'
            elif self.x<0:
                self.direction='right'


        #创建一个导弹类，继承自基类
class  MissList(Base):
        #重写基类的__init__方法
        def __init__(self,x,y,screen,planeName):
            super().__init__(screen,planeName)
        #根据飞机的名字来选择导弹的类型，并设置导弹的运动方向
            if planeName =='game':
                imageName='./feiji/bullet-3.gif'
                self.x=x+40
                self.y=y-20
            elif planeName=='enemy':
                imageName='./feiji/bullet-1.gif'
                self.x=x+30
                self.y=y+30
            self.image=pygame.image.load(imageName).convert()
        #导弹的移动方法
        def move(self):
            if self.name=='game':
                self.y-=2
            elif self.name=='enemy':
                self.y+=2
        #导弹的显示方法
        def display(self):
            self.screen.blit(self.image,(self.x,self.y))
        #判断导弹是否超出屏幕的范围
        def judge(self):
            if self.y<0 or self.y>480:
                return True
            else:
                return False



'''
1.搭建界面
'''

if __name__ == '__main__' :
    # 1.创建一个窗口用来实现窗口
    screen = pygame.display.set_mode((480,890),0,32)
    # 2.创建一个和窗口大小一样的图片，用来放置图片
    background = pygame.image.load("./feiji/background.png").convert()
    #创建一个玩家飞机对象
    gamePlane = GamePlane(screen,'game')
    #创建一个敌人飞机对象
    enemyPlane = EnemyPlane(screen,'enemy')


    while True:
        # 设定需要显示的背景图
        screen.blit(background,(0,0))
        gamePlane.display()
        enemyPlane.shedaodan()
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
                gamePlane.moveLeft()
                #控制飞机向左移动
                #x-=5
            # 检测键盘是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:

                print('right')
                gamePlane.moveRight()
                #控制飞机向右移动

            # 检测键盘是否是空格
            elif event.key == K_SPACE:
                print("space")
                gamePlane.shedaodan()

        # 更新需要显示的内容
        pygame.display.update()

