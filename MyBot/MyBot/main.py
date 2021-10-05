# Основные библиотеки
import discord,os
from discord.ext import commands

# Файл конфигурации
import setting.config
from setting.config import setting

# Коги
cogs = [
    "activity","moderation","economy","fun"
]

# Класс Main
class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Переменная Client к которой мы будем обращаться будущем
client = Main(
    command_prefix = setting["PREFIX"],
    intents = discord.Intents.all(),
    #help_command = None
)

# Вывод в консоль сообщения о включении
@client.event
async def on_ready():
    print(f"{client.user.name} Is a ready")

# Инициализация Main файла + загрузка когов
if __name__ == "__main__":
    for extension in cogs:
        cog = f"cogs.{extension}"
        try:
            client.load_extension(cog)
        except Exception as e:
            print(e)


@client.command()
async def load(ctx,extension):
    if ctx.author.id == 243454122580246528:
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Ког загружен")
    else:
        await ctx.send("Вы не создатель бота")

@client.command()
async def unload(ctx,extension):
    if ctx.author.id == 243454122580246528:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send("Ког выгружен")
    else:
        await ctx.send("Вы не создатель бота")

@client.command()
async def reload(ctx,extension):
    if ctx.author.id == 243454122580246528:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Коги перезагружен")
    else:
        await ctx.send("Вы не создатель бота")



# Старт бота
client.run(setting["TOKEN"])