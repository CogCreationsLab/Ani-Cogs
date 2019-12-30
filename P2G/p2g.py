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
        geolat = geocalc.lat
        geolng = geocalc.lng
        #Getting Latitude/Longitude

        mgmsg = f':white_check_mark: FOUND GEOLOCATION | {geolat}, {geolng}'
        mgmap = f'https://www.google.com/maps/search/{geolat},+{geolng}'
        #Message + Creating URL

        if ipv4 is None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
            #Checking for IPV4

        if geolat is None and geolng is None:
            await ctx.send(':x: INCORRECT SYNTAX | [p]p2g <ipv4>')
            return False
            #Checking for Latitude/Longitude

        if ipv4:
            geobed = discord.Embed(
                title='GEOLOCATION CORDINATES',
                description=mgmsg,
                color=discord.Color(0xff4040)
            )
            geobed.add_field(name='Google Maps URL: ', value=mgmap, inline=True)
            #Creating Embed

            await ctx.send(embed=geobed)
            #Sending Embed