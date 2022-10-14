# -*- coding: utf-8 -*-
# @Time        : 2022/10/14 23:54
# @File        : main.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import asyncio

import httpx
from nonebot.adapters.onebot.v11 import Message, MessageSegment


async def func():
	url = "http://123.125.8.44:18080/predictions/stable_diffusion"
	payload = {"q": "二次元，中国女孩，唯美，烟火，棕红色长发，金色眼睛，洛丽塔风格，精致面容，毛发细致，cg感，高清，8k，浪漫主义"}
	async with httpx.AsyncClient(verify=False, timeout=None) as client:
		resp = await client.post(url, json=payload)
		print(f"resp: {resp.content}")
		msg = Message(f"小麦原创绘画：主题为的作品")
		msg += MessageSegment.image(resp.content.decode())
		print(f"msg: {msg}")


asyncio.run(func())
