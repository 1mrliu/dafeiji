# coding = UTF8
import pygame
from pygame.locals import *


'''
用面向对象的方式显示飞机，并控制左右运动
1.实现飞机在你想出现的位置显示
2.用按键控制飞机移动
3.按下空格时，显示一颗子弹
'''
class HeroPlane(object):

    def __init__(self,screen):

        #设置飞机的默认位置
        self.x = 230
        self.y = 650

        #设置要显示内容的窗口
        self.screen = screen

        #根据名字生成飞机图片
        self.image = pygame.image.load("./feiji/hero.gif").convert()

        #用来保存英雄飞机的子弹
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))


        #存放需需要删除的子弹的信息

        needDelItemList = []

        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)

        for i in needDelItemList:
            self.bulletList.remove(i)






        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def moveLeft(self):
        self.x -=10

    def moveRight(self):
        self.x +=10

    def sheBullet(self):
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)


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

