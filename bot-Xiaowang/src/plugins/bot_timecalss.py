import time
import datetime
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent
from nonebot import on_command,on_keyword


# 时间

bot_time = on_command('几点了',priority=50,block=True)
@bot_time.handle()
async def _(event: GroupMessageEvent):
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    await bot_time.finish(Message(f"[CQ:at,qq={event.user_id}]")+localtime)

#星期
bot_week = on_keyword({'星期','weekday'})
@bot_week.handle()
async def _():
    weektime = datetime.datetime.now().weekday() + 1
    await bot_week.finish(Message("今天星期"+str(weektime)))




