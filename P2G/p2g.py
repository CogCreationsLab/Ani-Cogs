import discord
#Discord Framework

from redbot.core import commands
#Redbot Framework

import time
import geocoder
#General Imports

class P2G(commands.Cog):
    @commands.command()
    async def p2g(self, ctx, ipv4):
        if ipv4 is None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
        if ipv4:
            geocalc = geocoder.ip(f'{ipv4}')
            geo1 = geocalc.latlng[0]
            geo2 = geocalc.latlng[1]
            mgmsg = f'{geo1}{geo2}'
            geobed = discord.Embed(description=mgmsg,color=discord.Color(0xff4040))
            await ctx.send(embed=geobed)
