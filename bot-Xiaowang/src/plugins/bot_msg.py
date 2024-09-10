from nonebot import on_keyword,on_command
from nonebot.adapters.onebot.v11 import Message,Bot,Event
from nonebot.adapters.onebot.v11 import GroupMessageEvent,MessageSegment,GROUP_ADMIN,GROUP_OWNER
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from requests_html import HTMLSession
import requests,json,os,random


# 吃饭----问答
day_etc = on_keyword({'吃了吗','吃饭没','吃饭了吗','吃饭'})
@day_etc.handle()
async def _():
    await day_etc.finish(Message('终于能吃饭了，饿死了😍😍'))




# 早----问答
day_morning = on_keyword({'早上好','早','早安','早早'})
@day_morning.handle()
async def _():
    await day_morning.finish(Message('再睡会'))




# 再睡会----问答
day_morning_1 = on_keyword({'再睡会'})
@day_morning_1.handle()
async def _():
    await day_morning_1.finish(Message('？你还有脸睡觉？？'))




# 晚上好-----问答
day_evening = on_keyword({'晚上好','晚好'})
@day_evening.handle()
async def _():
    await day_evening.finish(Message('晚上好呀，美好的一天结束了'))




# 晚安----问答
day_wanan = on_keyword({'晚安','睡觉'})
@day_wanan.handle()
async def _():
    await day_wanan.finish(Message("不早了，赶快睡觉觉哦🛏️🛏️"))






# 爱心-------问答
day_love = on_keyword({'爱心',"love"})
@day_love.handle()
async def _():
    await day_love.finish(Message('爱心在这哟------》http://47.92.94.31:520/'))



# 6 ------问答
day_liu = on_command('6',priority=40)
@day_liu.handle()
async def _():
    await day_liu.finish(Message('666'))

#？？
day_wenhao = on_command('？',priority=60)
@day_wenhao.handle()
async def _(event: GroupMessageEvent):
    await day_wenhao.finish(Message(f'[CQ:at,qq={event.user_id}]你有什么问题吗？？'))


#你是机器人吗------问答
day_bot = on_command('你是机器人吗',to_me(),priority=60,block=True)
@day_bot.handle()
async def _(event: GroupMessageEvent):
    await  day_bot.finish(Message(f"[CQ:at,qq={event.user_id}]你才是机器人"))

#你是谁 -------问答
day_whois = on_command("你是谁",to_me(),priority=60,block=True)
@day_whois.handle()
async def _(event: GroupMessageEvent):
    await day_whois.finish(Message(f"[CQ:at,qq={event.user_id}]你管我？你@我干嘛？？"))
#课程表————————问答

day_class = on_command('课程表',priority=50,block=True)
@day_class.handle()
async def _(event:GroupMessageEvent):
    await day_class.finish(Message(f"[CQ:at,qq={event.user_id}]")+MessageSegment.image(file=r'file:///root/MyBot/bot-Xiaowang/src/plugins/image/课程表.jpg'))

# 获取图片,mc酱

def mc():
    url = 'https://api.gmit.vip/Api/McImg?format=image'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    res = requests.get(url,headers=headers,verify=False)
    a = res.url
    return a

day_mc = on_command("mc酱",to_me())

@day_mc.handle()
async def _mc(event: Event,bot: Bot):
    if event.get_user_id != str(event.self_id):
        try:
            if event.get_user_id() == '3185694026':
                meg = MessageSegment.image(file=mc())
                await bot.send(event=event,message='超级用户:\n'+meg)
            else:
                if await GROUP_ADMIN(bot, event):
                    await bot.send(
                        event=event,
                        message='管理员，你没有权限查看'
                    )
                elif await GROUP_OWNER(bot,event):
                    await bot.send(
                        event=event,
                        message='群主，你没有权限查看'
                    )
                else:
                    await bot.send(
                        event=event,
                        message='底层人员，更没有权限'
                    )

        except Exception as e:
            await bot.send(event=event,message='mc酱插件故障')



