# coding=utf-8
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """控制游戏外观和飞船速度的属性"""

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # get_rect获取相应的surface属性rect
        self.rect = self.image.get_rect()

        """我们要将飞船放在屏幕底部中央，为此，首先将表示屏幕的矩形存储在self.screen_rect中"""
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性center中存储小数值,这里是因为我们在settings中将初始值1设置为1.5
        self.center = float(self.rect.centerx)

        """ 允许不断移动
            结合使用KEYDOWN和KEYUP事件，及一个名为moving_right的标志来实现持续移动
            
            飞船不动时，moving_right为False,玩家按下右箭头键时，将这个标志设置为True,玩家松开时，将这个标志设置为False------见game_function  line16-30  (左同)
            用update方法来检查标志moving_right的状态，如果这个标志为True，就调用飞船的位置
        """
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置,这里用两个if，而没有用elif，是因为
            如果玩家同时按下左右键，将增大center，再减少center的值，即飞船的位置保持不变
            但如果用elif，右箭头始终保持优先地位，当左移动切换到右移动时，玩家可能同时按住左右箭头键，这种情况下，前面的做法更加准确
        """
        # if限制飞船的活动范围（因为在运行游戏的时候，飞船可能飞出屏幕外）
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitem(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
