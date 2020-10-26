# coding=utf-8

"""将所有的设置储存在同一个地方"""


class Settings():
    # 储存外星人入侵所有设置的类
    def __init__(self):
        """初始化游戏的设置"""
        # 外星人设置
        # 添加一个控制外星人速度的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 添加子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 限制子弹数量6个
        self.bullets_allowed = 6

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        # 调整飞船的速度,将初始值1设置为1.5
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 以1.1倍速加快游戏节奏
        self.speedup_scale = 1.1
        # 提高外星人点数的速度
        self.score_scale = 1.5

        # 初始化随游戏进行而变化的属性
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右，fleet_direction为-1表示向左
        self.fleet_direction = 1

        # 每击落一个外星人将得到50个点
        self.alien_points = 50

    def increase_speed(self):
        """提高速度和外星人点数设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
