# -*- coding: utf-8 -*-
# @Time        : 2022/10/13 22:14
# @File        : limiter.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time

from collections import defaultdict

from .config import config


class FreqLimiter:
	def __init__(self, default_cd_seconds):
		self.next_time = defaultdict(float)
		self.default_cd = default_cd_seconds

	def check(self, key) -> bool:
		return bool(time.time() >= self.next_time[key])

	def start_cd(self, key, cd_time=0):
		self.next_time[key] = time.time() + (cd_time if cd_time > 0 else self.default_cd)

	def left_time(self, key) -> float:
		return self.next_time[key] - time.time()


limiter = FreqLimiter(config.cd_time)
