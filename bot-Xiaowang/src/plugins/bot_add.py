from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent

welcom=on_notice()

@welcom.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "欢迎！：[CQ:at,qq={}]".format(user)
    msg = at_ + '倒霉蛋加入😍😍，艾特我并输入/帮助，查看机器人功能呦！！'
    msg = Message(msg)
    if event.group_id == 515297509:
        await welcom.finish(message=Message(f'{msg}'))

@welcom.handle()
async def welcome(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    msg = "{}倒霉蛋离开了😭😭".format(user)
    msg = Message(msg)
    if event.group_id == 515297509:
        await welcom.finish(message=Message(f'{msg}'))



