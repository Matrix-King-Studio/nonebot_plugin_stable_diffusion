# -*- coding: utf-8 -*-
# @Time        : 2022/10/13 22:13
# @File        : config.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import nonebot
from pydantic import BaseSettings


class Config(BaseSettings):
	cd_time: int = 60  # cd时间，单位秒
	manager_list: list = []  # 管理员列表（不受冷却时间限制）

	class Config:
		extra = "ignore"


global_config = nonebot.get_driver().config
config = Config(**global_config.dict())  # 载入配置
