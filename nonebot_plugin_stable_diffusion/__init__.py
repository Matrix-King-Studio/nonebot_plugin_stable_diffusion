# -*- coding: utf-8 -*-
# @Time        : 2022/10/13 22:09
# @File        : __init__.py.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from nonebot import logger
from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, RawCommand

from .config import config
from .drawer import drawer_task
from .limiter import limiter

drawer = on_command("画画", aliases={"画画帮助"}, priority=5, block=True)


@drawer.handle()
async def _(matcher: Matcher, event: GroupMessageEvent, command=RawCommand(), args=CommandArg()):
	# 判断是否触发帮助 或 绘画主题任务描述为空
	if command == "画画帮助" or str(args).strip() == '':
		help_msg = "发送：/画画 二次元，中国女孩，唯美，烟火，棕红色长发，金色眼睛，洛丽塔风格，精致面容，毛发细致，cg感，高清，8k，浪漫主义"
		await matcher.finish(help_msg)

	# 判断用户是否触发频率限制
	user_id = event.user_id
	managers = config.wenxin_manager_list  # 管理员列表(不触发冷却时间限制)
	if not limiter.check(user_id):
		left_time = limiter.left_time(user_id)
		await matcher.finish(f"不可以哦，你刚画了一次哎，需要等待{int(left_time)}秒再找俺画画！")

	# 启动画画任务
	text = args  # 绘画的任务描述文字
	await matcher.send(f"小麦绘制内容为“{text}”的作品（预计1-2分钟）...")

	try:
		img_url = await drawer_task(text)

		if not str(user_id) in managers:
			limiter.start_cd(user_id)  # 启动冷却时间限制

		msg = Message(f"小麦原创绘画：主题为“{text}”的作品")
		msg += MessageSegment.image(img_url)
		await matcher.finish(msg)
	except Exception as e:
		logger.error(f"error: {e}")
		await matcher.finish(f"55555，江郎才尽了，画不出来了。（骗你的，报错了，请联系管理员（2426671397）处理。）")