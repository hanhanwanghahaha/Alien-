# coding=utf-8
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近(左边距设置为外星人的宽度，上边距设置为外星人的高度)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitem(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右或向右移动外星人"""
        # fleet_direction为1,就将外星人当前的x坐标增大alien_speed_factor，从而外星人向右移，如果fleet_direction为-1，就将外星人当前的x坐标减去alien_speed_factor
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction
                   )

        # 使用self.x的值来更新rect的位置
        self.rect.x = self.x
