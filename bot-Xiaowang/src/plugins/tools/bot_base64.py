import nonebot
from nonebot import CommandSession
from nonebot import on_command

@on_command('全员禁言')
async def muteall(session: CommandSession):
    bot = nonebot.get_bot()
    group_id = session.event.group_id
    try:
        await bot.set_group_whole_ban(group_id=group_id)
        session.finish('成功执行')
    except Exception as e:
        session.finish(f'报错，原因{e}')

    stripped_arg = session.current_arg_text.strip()
    session.state['plain_text']=stripped_arg
