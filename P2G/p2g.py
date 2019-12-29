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
        if ip None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
        if ip:
            geocalc = geocoder.ip(f'{ip}')
            await ctx.send(f':white_check_mark: SUCCESSFULY CALCULATED GEOLOCATION VALUE | {geocalc.latlng} |')
