# Основные библиотеки
import sqlite3,discord,random,time
from discord.ext import commands,tasks


connection = sqlite3.connect('server.db')
cursor = connection.cursor()
tdict = {}

def transform(seconds):
    print(seconds)
    periods = [
        ('д',         60*60*24),
        ('ч',        60*60),
        ('м',      60),
        ('c', 1)
    ]

    strings=[]
    for period_name, period_seconds in periods:
        if seconds > period_seconds:
            period_value , seconds = divmod(seconds, period_seconds)
                
            strings.append("%s%s" % (period_value, period_name))
    return " ".join(strings)

# Класс Admin
class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            id INT,
            cash INT,
            rep INT,
            lvl INT,
            exp INT,
            progres INT,
            voiceActivity INT,
            server_id INT
        )""")
    
        cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
            role_id INT,
            id INT,
            cost INT
        )""")

        for guild in self.bot.guilds:
            for member in guild.members:
                if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                    cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 1, 0, 0, 0, {guild.id})")
                else:
                    pass
    
        connection.commit()
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='сломай нервы разраба'))
        print('bot connected')



    @commands.Cog.listener()
    async def on_member_join(self, member):
        if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 1, 0, 0, 0, {member.guild.id})")
            connection.commit()
        else:
            pass
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if cursor.execute(f"SELECT id FROM users WHERE id = {ctx.member.id}").fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES ('{ctx.member}', {ctx.member.id}, 0, 0, 1, 0, 0, 0, {ctx.member.guild.id})")
            connection.commit()

    @commands.command(aliases = ['баланс'])
    async def balance(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(embed = discord.Embed(
                description = f"""Баланс пользователя **{ctx.author}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} :moneybag:**"""
            ))
            
        else:
            await ctx.send(embed = discord.Embed(
                description = f"""Баланс пользователя **{member}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0]} :moneybag:**"""
            ))

    @commands.command(aliases = ['магазин'])
    async def shop(self, ctx):
        embed = discord.Embed(title = 'Магазин ролей')
    
        for row in cursor.execute("SELECT role_id, cost FROM shop WHERE id = {}".format(ctx.guild.id)):
            if ctx.guild.get_role(row[0]) != None:
                embed.add_field(
                    name = f"Стоимость **{row[1]} :moneybag:**",
                    value = f"Вы приобрете роль {ctx.guild.get_role(row[0]).mention}",
                    inline = False
                )
            else:
                pass
    
        await ctx.send(embed = embed)

    @commands.command(aliases = ['купить'])
    async def buy(self, ctx, role: discord.Role = None):
        if role is None:
            await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете приобрести")
        else:
            if role in ctx.author.roles:
                await ctx.send(f"**{ctx.author}**, у вас уже имеется данная роль")
            elif cursor.execute("SELECT cost FROM shop WHERE role_id = {}".format(role.id)).fetchone()[0] > cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]:
                await ctx.send(f"**{ctx.author}**, у вас недостаточно средств для покупки данной роли")
            else:
                await ctx.author.add_roles(role)
                cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(cursor.execute("SELECT cost FROM shop WHERE role_id = {}".format(role.id)).fetchone()[0], ctx.author.id))
                connection.commit()
    
                await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['реп', '+реп'])
    async def rep(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"**{ctx.author}**, укажите участника сервера")
        else:
            if member.id == ctx.author.id:
                await ctx.send(f"**{ctx.author}**, вы не можете указать смого себя")
            else:
                cursor.execute("UPDATE users SET rep = rep + {} WHERE id = {}".format(1, member.id))
                connection.commit()
    
                await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['лидеры', 'лб', 'lb'])
    async def leaderboard(self, ctx):
        embed = discord.Embed(title = 'Топ 10 сервера')
        counter = 0
    
        for row in cursor.execute("SELECT name, cash FROM users WHERE server_id = {} ORDER BY cash DESC LIMIT 10".format(ctx.guild.id)):
            counter += 1
            embed.add_field(
                name = f'# {counter} | `{row[0]}`',
                value = f'Баланс: {row[1]}',
                inline = False
            )
    
        await ctx.send(embed = embed)

    @commands.command(aliases = ['передать'])
    async def give(self, ctx, member: discord.Member = None, amount: int = None):
        if member is None:
            await ctx.send(f"**{ctx.author}**, укажите пользователя, которому желаете передать определенную сумму")
        else:
            if amount is None:
                await ctx.send(f"**{ctx.author}**, укажите сумму, которую желаете начислить на счет пользователя")
            elif amount > cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]:
                await ctx.send(f"**{ctx.author}**, у вас нет столько :moneybag:")
            elif amount < 1:
                await ctx.send(f"**{ctx.author}**, укажите сумму больше 1 :moneybag:")
            else:
                cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(amount, member.id))
                cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(int(amount), ctx.author.id))
                connection.commit()
    
                await ctx.message.add_reaction('✅')


    @commands.command(aliases = ['инф','инфа'])
    async def info(self, ctx, member: discord.Member = None):
        time = int(cursor.execute("SELECT voiceActivity FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0])
        if time == 0:
            time = "0c"
        else:
            time == transform(time)


        if member is None:
            
            time = int(cursor.execute("SELECT voiceActivity FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0])
            if time == 0:
                time = "0c"
            else:
                time = transform(time)

            emb = discord.Embed(colour=discord.Colour(0x831c99))
            emb.set_thumbnail(url=ctx.author.avatar_url)
            emb.set_author(name=ctx.author)
            emb.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
            emb.add_field(name="Баланс:", value=cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0])
            emb.add_field(name="Репутация:", value=cursor.execute("SELECT rep FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0])
            emb.add_field(name="Уровень:", value=cursor.execute("SELECT lvl FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0])
            emb.add_field(name="Время в войсе:", value=time)
            await ctx.send(embed=emb) 

        else:
            time = int(cursor.execute("SELECT voiceActivity FROM users WHERE id = {}".format(member.id)).fetchone()[0])
            if time == 0:
                time = "0c"
            else:
                time = transform(time)

            emb = discord.Embed(colour=discord.Colour(0x831c99))
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=member)
            emb.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
            emb.add_field(name="Баланс:", value=cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0])
            emb.add_field(name="Репутация:", value=cursor.execute("SELECT rep FROM users WHERE id = {}".format(member.id)).fetchone()[0])
            emb.add_field(name="Уровень:", value=cursor.execute("SELECT lvl FROM users WHERE id = {}".format(member.id)).fetchone()[0])
            emb.add_field(name="Время в войсе:", value=time)
            await ctx.send(embed=emb)


    #add exp and money for activity
    @commands.Cog.listener()
    async def on_message(self, message):
        cursor.execute("UPDATE users SET exp = exp + {} WHERE id = {}".format(random.randint(1,6), message.author.id))
        cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(random.randint(1,3), message.author.id))
        connection.commit()
        

    #add exp and money for voice activity
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        author = member.id
        if before.channel is None and after.channel is not None:
            t1 = time.time()
            tdict[author] = t1
            
        elif before.channel is not None and after.channel is None and author in tdict:
            t2 = time.time()
            print(t2)
            activityPoint = round((t2-tdict[author])/30) 
            cursor.execute("UPDATE users SET voiceActivity = voiceActivity + {} WHERE id = {}".format(round((t2-tdict[author])), member.id))
            connection.commit()
            await member.guild.system_channel.send(str(round(t2-tdict[author]))+"sec")
            i = 0
            while i < activityPoint:
                cursor.execute("UPDATE users SET exp = exp + {} WHERE id = {}".format(random.randint(1,6), member.id))## еще чутка подумать
                cursor.execute("UPDATE users SET cash = cash + {} WHERE id = {}".format(random.randint(1,3), member.id)) 
                connection.commit()
                i = i + 1

def setup(bot):
    bot.add_cog(economy(bot))
