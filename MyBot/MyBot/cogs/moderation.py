# Основные библиотеки
import sqlite3,discord,asyncio,time
from discord.ext import commands

connection = sqlite3.connect('server.db')
cursor = connection.cursor()

# Класс Admin
class activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, number: int):
        if number is None:
                await ctx.send(f"**{ctx.author}**, укажите кол-во сообщений")
        else:
            await ctx.channel.purge(limit=number)

    @commands.command(aliases = ['наградить'])
    @commands.has_permissions(administrator=True)
    async def award(self, ctx, member: discord.Member = None, amount: int = None):
        if member is None:
            await ctx.send(f"**{ctx.author}**, укажите пользователя, которому желаете выдать определенную сумму")
        else:
            if amount is None:
                await ctx.send(f"**{ctx.author}**, укажите сумму, которую желаете начислить на счет пользователя")
            elif amount < 1:
                await ctx.send(f"**{ctx.author}**, укажите сумму больше 1 :moneybag:")
            else:
                cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(amount, member.id))
                connection.commit()
    
                await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['отнять'])
    @commands.has_permissions(administrator=True)
    async def take(self, ctx, member: discord.Member = None, amount = None):
        if member is None:
            await ctx.send(f"**{ctx.author}**, укажите пользователя, у которого желаете отнять сумму денег")
        else:
            if amount is None:
                await ctx.send(f"**{ctx.author}**, укажите сумму, которую желаете отнять у счета пользователя")
            elif amount == 'all':
                cursor.execute("UPDATE users SET cash = {} WHERE id = {}".format(0, member.id))
                connection.commit()
    
                await ctx.message.add_reaction('✅')
            elif int(amount) < 1:
                await ctx.send(f"**{ctx.author}**, укажите сумму больше 1 :moneybag:")
            else:
                cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(int(amount), member.id))
                connection.commit()
    
                await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['добавить магазин'])
    @commands.has_permissions(administrator=True)
    async def add_shop(self, ctx, role: discord.Role = None, cost: int = None):
        if role is None:
            await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете внести в магазин")
        else:
            if cost is None:
                await ctx.send(f"**{ctx.author}**, укажите стоимость для даннойй роли")
            elif cost < 0:
                await ctx.send(f"**{ctx.author}**, стоимость роли не может быть такой маленькой")
            else:
                cursor.execute("INSERT INTO shop VALUES ({}, {}, {})".format(role.id, ctx.guild.id, cost))
                connection.commit()
    
                await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['удалитьмагазин'])
    @commands.has_permissions(administrator=True)
    async def remove_shop(self,ctx, role: discord.Role = None):
        if role is None:
            await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете удалить из магазина")
        else:
            cursor.execute("DELETE FROM shop WHERE role_id = {}".format(role.id))
            connection.commit()
    
            await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['мут'])#сделать каунтер в бд
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, time):
        if member == 0:
            embed = discord.Embed(title = "Кого мне мутить?", color=discord.Color.purple())
            await ctx.send(embed = embed)
            return
        elif self.bot.user == member:
            embed = discord.Embed(title = "Ты не можешь меня мутить! Я тут главный", color=discord.Color.purple())
            await ctx.send(embed = embed)
            return
        else:
            muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
            time_convert = {"s":1, "m":60, "h":3600,"d":86400}
            tempmute= int(time[0]) * time_convert[time[-1]]
            print(tempmute)
            await member.add_roles(muted_role)
            embed = discord.Embed(description= f"✅ *{member.display_name}#{member.discriminator} получил мут*", color=discord.Color.purple())
            await ctx.send(embed=embed)
            await asyncio.sleep(tempmute)
            await member.remove_roles(muted_role)
            await member.send('Ваш мут снят. Теперь ты можешь взаимодействовать с другими людьми!')
    

def setup(bot):
    bot.add_cog(activity(bot))
