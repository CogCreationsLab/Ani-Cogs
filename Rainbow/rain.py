import time
import discord
from redbot.core import commands
#Imports

class rainbow(commands.Cog):
    @commands.command()
    async def rainbowset(self, ctx):
        user = ctx.message.author
        delay = ctx.message.content.split(' ')[1]
        frole = ctx.message.content.split(' ')[2]
        rrole = discord.utils.get(user.guild.roles, name=frole)
        print(f'| User: {user} | Delay: {delay} | Role: {rrole} |')
        clist = [0xff0000, 0xff2f00, 0xff5900, 0xff7700, 0xff9d00, 0xffbf00, 0xffdd00, 0xfff200, 0xf2ff00, 0xc8ff00, 0xb7ff00, 0x99ff00, 0x6aff00, 0x3cff00, 0x00ff11, 0x00ff37, 0x00ff55, 0x00ff77, 0x00ff95, 0x00ffb7, 0x00ffdd, 0x00fffb, 0x00e1ff, 0x00bfff, 0x009dff, 0x0080ff, 0x0062ff, 0x0048ff, 0x002fff, 0x1100ff, 0x4400ff, 0x5900ff, 0x7700ff, 0x9900ff, 0xaa00ff, 0xcc00ff, 0xee00ff, 0xff00ee, 0xff00d0, 0xff00ae, 0xff0088, 0xff005d, 0xff0037, 0xff0019]
        while True:
            for c in clist:
                await rrole.edit(role=rrole, colour=discord.Colour(value=c))
                time.sleep(int(delay))
