'''
帮助文档
'''
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent
from nonebot import on_command
from nonebot.rule import to_me


bot_help = on_command('帮助',to_me())
@bot_help.handle()
async def _():
    await bot_help.send(Message(
        '功能如下\n'
        '----------------------------------------------\n'
        'api\t\t\t\t系统状态\n'
        '----------------------------------------------\n'
        '关键字匹配（模糊匹配）\t\t精准匹配（需要艾特机器人）\n'
        '----------------------------------------------\n'
        '戳一戳功能\t\t\t\t/舔狗语录\n'
        '----------------------------------------------\n'
        '@机器人/cm酱（功能限制只有SU使用）\t\t\t\t防撤回\n'
        '----------------------------------------------\n'
        '随机禁言（群主，管理员，SU可用）\t\t\t\t文学\n'

    ))

bot_api = on_command('api')
@bot_api.handle()
async def _():
    await bot_api.send(Message(
        '/输入查手机+手机号\n'
        '合成二维码 +内容  \n'
        '艾特我并输入/字典+汉字\t'
    ))

bot_guanjianzi = on_command('关键字匹配')
@bot_guanjianzi.handle()
async def _(event: GroupMessageEvent):
    await bot_guanjianzi.send(Message(f"[CQ:at,qq={event.user_id}]关键字匹配如下\n早，晚，晚安，吃了没，晚上好，博客，爱心，6"))


bot_jinzhun = on_command('精准匹配')
@bot_jinzhun.handle()
async def _(event: GroupMessageEvent):
    await bot_jinzhun.send(Message(f'[CQ:at,qq={event.user_id}]精准匹配如下\n/你是机器人吗，/你是谁，/文学'))

bot_wenxue = on_command('文学')
@bot_wenxue.handle()
async def _():
    await bot_wenxue.send(Message(
        '''
        /历史上的今天\n
        /每日简报\n
        /鸡汤\n
        /毒鸡汤\n
        /诗词\n
        /段子\n
        '''
    ))