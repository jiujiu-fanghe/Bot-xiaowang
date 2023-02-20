'''
当bot被戳一戳时，如果对方在允许列表则发一下张图片，如果不在，则@并让她不再戳了
'''


from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent,Message,MessageSegment
import requests

# 获取图片
# def mc():
#     url = 'https://api.ixiaowai.cn/mcapi/mcapi.php'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
#     }
#     res = requests.get(url,headers=headers)
#     a = res.url
#     return a

# 戳一戳
def _cheak(event: PokeNotifyEvent):
    return event.target_id == event.self_id

gree_list=[3185694026]

poke = on_notice(rule=_cheak)

@poke.handle()
async def _(event: PokeNotifyEvent):
    if (event.user_id in gree_list):
        await poke.finish(Message(f"[CQ:at,qq={gree_list}]你可以戳，并给你一张壁纸"+MessageSegment.image(file=r'file:///root/MyBot/bot-Xiaowang/src/plugins/image/26.jpg')))
    else:
        await poke.finish(Message(f"[CQ:at,qq={event.user_id}]你在戳一下试试"))
