import discord,random,sys
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from discord.member import Member
import textwrap
import urllib
import aiohttp,io
import datetime



# Класс Admin
class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ship(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"{ctx.author}, укажите участника")

        elif member.id == 844140304654270465:
            await ctx.send(f"{ctx.author}, я не могу любить😢")

        elif member.id == 243454122580246528:
            img = Image.open("1.png")
            idraw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", size=128)
            idraw.text((130, 150), "100%", font=font)
            img.save('2.png')
            img.close()
            file = discord.File("2.png",filename="image.png")
            emb = discord.Embed(title=f"**{ctx.author.name}**, ваша совместимость с **{member.name}**:",colour=discord.Colour(0x831c99))
            emb.set_image(url="attachment://image.png")
            emb.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
            await ctx.send(file=file,embed=emb)

        elif ctx.author.id == 243454122580246528 and member.id == 433352849293049866 or ctx.author.id == 433352849293049866 and member.id == 43454122580246528:
            img = Image.open("1.png")
            idraw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", size=128)
            idraw.text((130, 150), "9999999999%", font=font)
            img.save('2.png')
            img.close()
            file = discord.File("2.png",filename="image.png")
            emb = discord.Embed(title=f"**{ctx.author.name}**, ваша совместимость с **{member.name}**:",colour=discord.Colour(0x831c99))
            emb.set_image(url="attachment://image.png")
            emb.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
            await ctx.send(file=file,embed=emb)
        elif ctx.author.id == member.id:
             await ctx.send("Фее (¬_¬ )")

        else:
            img = Image.open("1.png")
            idraw = ImageDraw.Draw(img)
            rand = str(random.randint(1,100))
            counter = len(rand)
            print(counter)
            if counter == 1:
                text =' ' + rand + '%'
            else:
                text = rand + '%'
            font = ImageFont.truetype("arial.ttf", size=128)
            idraw.text((130, 150), text, font=font)
            img.save('2.png')
            img.close()
            file = discord.File("2.png",filename="image.png")
            emb = discord.Embed(title=f"**{ctx.author.name}**, ваша совместимость с **{member.name}**:",colour=discord.Colour(0x831c99))
            emb.set_image(url="attachment://image.png")
            emb.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
            await ctx.send(file=file,embed=emb)

    @commands.command()
    async def horny(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "horny.png")
                    em = discord.Embed(title=f"**{member}**, теперь ты официально Horny ",color=0x831c99)
                    em.set_image(url="attachment://horny.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No horny :(')
                await session.close()
    
    @commands.command()#триггеред ава
    async def triggered(self,ctx, member: discord.Member=None):
        if not member: # if no member is mentioned
            member = ctx.author # the user who ran the command will be the member  
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                await trigSession.close() # closing the session and;  
                await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file

    @commands.command()#лоли ава
    async def lolice(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/lolice?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "lolice.png")
                    em = discord.Embed(title=f"**{member}**, теперь ты лоль ",color=0x831c99)
                    em.set_image(url="attachment://lolice.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No lolice :(')
                await session.close()

    @commands.command()#simp ава
    async def simp(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/simpcard?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "simp.png")
                    em = discord.Embed(title=f"**{member}**, теперь ты официально SIMP ",color=0x831c99)
                    em.set_image(url="attachment://simp.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No simp :(')
                await session.close()

    @commands.command()#simp ава
    async def pixelate(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")   
                    em = discord.Embed(title=f"**{member}**, теперь ты официально SIMP ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No pixelate :(')
                await session.close()
######################################################################################################
    @commands.command()#simp ава
    async def jail(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")
                    em = discord.Embed(title=f"**{member}**, теперь ты за решеткой ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No jail :(')
                await session.close()

    @commands.command()#simp ава
    async def comrade(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/comrade?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")
                    em = discord.Embed(title=f"**{member}**, теперь ты комрад ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No comrade :(')
                await session.close()

    @commands.command()#simp ава
    async def wasted(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")    
                    em = discord.Embed(title=f"**{member}**, теперь ты потрачен ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No wasted :(')
                await session.close()

    @commands.command()#simp ава
    async def gay(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")                
                    em = discord.Embed(title=f"**{member}**, теперь ты гей ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No gay :(')
                await session.close()

    @commands.command()#simp ава
    async def glass(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")                
                    em = discord.Embed(title=f"**{member}**, ты выполнил свою миссию ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No glass :(')
                await session.close()

    @commands.command()#simp ава
    async def passed(self,ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/passed?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "pixelate.png")                
                    em = discord.Embed(title=f"**{member}**, ты... Я не знаю что это... ",color=0x831c99)
                    em.set_image(url="attachment://pixelate.png")
                    em.set_footer(text="C любовью MAKIGO", icon_url=self.bot.user.avatar_url)
                    await ctx.send(embed=em, file=file)
                else:
                    await ctx.send('No passed :(')
                await session.close()







































































def setup(bot):
    bot.add_cog(fun(bot))