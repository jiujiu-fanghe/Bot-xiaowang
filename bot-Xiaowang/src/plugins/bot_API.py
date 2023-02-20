import aiohttp, json
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_command,on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.params import CommandArg
import requests
import random


# 查手机
catch_str = on_command('查手机', aliases={"查手机号", "手机号"},priority=2,block=True)


@catch_str.handle()
async def send_msg(bot: Bot, event: Event, msg: Message = CommandArg()):
    content = msg.extract_plain_text()

    data_json = await get_data(content)
    try:
        msg = '\n' + json.dumps(data_json, indent=2, ensure_ascii=False)
    except:
        msg = '数据解析失败，额度用完或接口寄了喵~'

    await catch_str.finish(Message(f'{msg}'), at_sender=True)


async def get_data(content):
    api_key = 'e14c9cf25c066ddb1fe1a818647ac6e9'
    url = 'http://apis.juhe.cn/mobile/get?phone=' + content + '&key=' + api_key
    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'

    }

    re = requests.get(url=url,headers=heads)
    a = re.json()
    return a


# 字典
catch_str = on_command('字典', aliases={"新华字典"})


@catch_str.handle()
async def send_msg(bot: Bot, event: Event, msg: Message = CommandArg()):
    content = msg.extract_plain_text()

    data_json = await get_data(content)
    try:
        msg = '\n' + str(data_json["result"]["jijie"])
    except:
        msg = '数据解析失败，额度用完或接口寄了喵~'

    await catch_str.finish(Message(f'{msg}'), at_sender=True)


async def get_data(content):
    api_key = "5f8cc6599b92799956e2796a7be53467"
    API_URL = 'http://v.juhe.cn/xhzd/query?word=' + content + '&key=' + api_key
    async with aiohttp.ClientSession() as session:
        async with session.get(url=API_URL) as response:
            result = await response.read()
            ret = json.loads(result)
    # nonebot.logger.info(ret)
    return ret




# 舔狗语录
def get_new1():
    url1 = 'https://api.ixiaowai.cn/tgrj/index.php'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }
    a = requests.get(url=url1,headers=header,verify=False)
    b = a.text
    c = b.replace('*','')
    return c
# print('舔狗语录1：',c)

yulu = on_command('舔狗语录',priority=2,block=True)
@yulu.handle()
async def slove(bot:Bot , event: Event):
    if int(event.get_user_id()) != event.self_id:
        try:
            str1 = get_new1()
            await bot.send(
                event=event,
                message=str1,
                at_sender = True
            )
        except Exception as e:
            await yulu.send('插件出错')