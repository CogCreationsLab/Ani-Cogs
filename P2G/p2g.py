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
        geocalc = geocoder.ip(f'{ipv4}')
        #Getting Latitude/Longitude

        mgmsg = f':white_check_mark: FOUND GEOLOCATION | {geo1}, {geo2}'
        mgmap = f'https://www.google.com/maps/search/{geo1},+{geo2}'
        #Message + Creating URL

        if ipv4 is None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
            #Checking for IPV4

        if geo1 is None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
            #Checking for Latitude

        if geo2 is None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
            #Checking for Longitude/Latitude

        if ipv4:
            geo1 = geocalc.latlng[0]
            geo2 = geocalc.latlng[1]
            geobed = discord.Embed(description=mgmsg,color=discord.Color(0xff4040))
            geobed.set_image(url=mgmap)
            await ctx.send(embed=geobed)
            #Creating & Sending Embed
