from nonebot import on_command
from nonebot.typing import T_Handler
from .bot_histor import Source, sources
from nonebot.matcher import Matcher
from nonebot.plugin import PluginMetadata

"""
获取关于文学的所有内容，后面会不断完善
"""
__plugin_meta__ = PluginMetadata(
    name="文学",
    description="这个插件连接着关于文学的所有的内容！",
    usage="/历史 /简报 /鸡汤 /毒鸡汤 /诗 /段子",
)


def create_matchers():
    def create_handler(source: Source) -> T_Handler:
        async def handler(matcher: Matcher):
            res = None
            try:
                res = await source.func()
                if not res:
                    res = "获取数据失败"
            except Exception as e:
                print(e)
                res = "出错了，请稍后再试"
            await matcher.finish(res)

        return handler

    for source in sources:
        on_command(
            source.keywords[0], aliases=set(source.keywords), block=True, priority=12
        ).append_handler(create_handler(source))


create_matchers()