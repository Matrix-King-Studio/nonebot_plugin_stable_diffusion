# -*- coding: utf-8 -*-
# @Time        : 2022/10/13 22:14
# @File        : drawer.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import httpx


# 创建绘画任务
async def drawer_task(text):
	url = "http://123.125.8.44:18080/predictions/stable_diffusion"
	payload = {"q": text}
	async with httpx.AsyncClient(verify=False, timeout=None) as client:
		resp = await client.post(url, data=payload)
		return resp.content.decode()
