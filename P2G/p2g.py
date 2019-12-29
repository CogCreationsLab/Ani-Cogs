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
            await ctx.send(f':white_check_mark: SUCCESSFULY CALCULATED GEOLOCATION VALUE | {geocalc.latlng} |')
