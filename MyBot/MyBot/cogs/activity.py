# Основные библиотеки
import json,requests
from discord.ext import commands



# Класс Admin
class activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ytt(self, ctx):# YouTube Together

        data = {
            "max_age": 86400,
            "max_users": 0,
            "target_application_id": 755600276941176913, # YouTube Together
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot ODQ0MTQwMzA0NjU0MjcwNDY1.YKOE6w._wkG1hgmkakqIIE5prJH4L60EuY",
            "Content-Type": "application/json"
        }
    
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в канал")
        else:
            await ctx.send("Зайдите в канал")
    
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)
    
        await ctx.send(f"https://discord.com/invite/{link['code']}")
    @commands.command()
    async def fish(self, ctx):# Fishington.io
        data = {
            "max_age": 86400,
            "max_users": 0,
            "target_application_id": 814288819477020702, # Fishington.io
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot ODQ0MTQwMzA0NjU0MjcwNDY1.YKOE6w._wkG1hgmkakqIIE5prJH4L60EuY",
            "Content-Type": "application/json"
        }
    
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в канал")
        else:
            await ctx.send("Зайдите в канал")
    
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)
    
        await ctx.send(f"https://discord.com/invite/{link['code']}")
    @commands.command()
    async def poker(self, ctx):# Poker Night
        data = {
            "max_age": 86400,
            "max_users": 0,
            "target_application_id": 755827207812677713, # Poker Night
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot ODQ0MTQwMzA0NjU0MjcwNDY1.YKOE6w._wkG1hgmkakqIIE5prJH4L60EuY",
            "Content-Type": "application/json"
        }
    
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в канал")
        else:
            await ctx.send("Зайдите в канал")
    
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)
    
        await ctx.send(f"https://discord.com/invite/{link['code']}")
    @commands.command()
    async def chess(self, ctx):# Chess
        data = {
            "max_age": 86400,
            "max_users": 0,
            "target_application_id": 832012774040141894, # Chess
            "target_type": 2,
            "temporary": False,
            "validate": None
        }
        headers = {
            "Authorization": "Bot ODQ0MTQwMzA0NjU0MjcwNDY1.YKOE6w._wkG1hgmkakqIIE5prJH4L60EuY",
            "Content-Type": "application/json"
        }
    
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Зайдите в канал")
        else:
            await ctx.send("Зайдите в канал")
    
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)
    
        await ctx.send(f"https://discord.com/invite/{link['code']}")


def setup(bot):
    bot.add_cog(activity(bot))
