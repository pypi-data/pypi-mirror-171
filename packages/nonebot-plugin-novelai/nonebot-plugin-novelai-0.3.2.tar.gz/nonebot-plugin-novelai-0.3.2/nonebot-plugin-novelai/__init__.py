from . import txt2pix, config
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="AI绘图",
    description="调用novelai进行二次元AI绘图",
    usage=f"基础用法:\n.aidraw[指令] [空格] loli,[参数]\n示例:.aidraw loli,cute,kawaii,",
)
