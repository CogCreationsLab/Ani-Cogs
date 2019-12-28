import discord
from discord.ext import commands
#Discord Framework

from redbot.core import Config
from redbot.core import commands
#Redbot Framework

import time
from random import choice as rand
#General Imports

patg = [
    "https://i.imgur.com/YTGnx49.gif",
    "https://i.imgur.com/U37wHs9.gif",
    "https://i.imgur.com/BU2IQym.gif",
    "https://i.imgur.com/yp6kqPI.gif",
    "https://i.imgur.com/uDyehIe.gif",
    "https://i.imgur.com/vG8Vuqp.gif",
    "https://i.imgur.com/z4uCLUt.gif",
    "https://i.imgur.com/ZIRC9f0.gif",
    "https://i.imgur.com/s8m4srp.gif",
    "https://i.imgur.com/LKvNxmo.gif",
    "https://i.imgur.com/j4W4GFt.gif",
    "https://i.imgur.com/75bX4A1.gif",
    "https://i.imgur.com/dSlfpe3.gif",
    "https://i.imgur.com/JjxaT8e.gif",
    "https://i.imgur.com/QWBlOaQ.gif",
    "https://i.imgur.com/5448px6.gif",
    "https://i.imgur.com/4WJRAGw.gif",
    "https://i.imgur.com/v1sSh5r.gif"
]

patm = [
    "{auth} pats {mem} on the head ^-^",
    "{auth} pattie cakes {mem}s head 0-0",
    "{mem} gets a lucky 'ol pat on the head from {auth} nUwU",
    "{mem} recieves a pat from {auth} =-=",
]

kissg = [
    "https://cdn.weeb.sh/images/SyY0j6Ov-.gif",
    "https://cdn.weeb.sh/images/ByVQha_w-.gif",
    "https://cdn.weeb.sh/images/SJrBZrMBz.gif",
    "https://cdn.weeb.sh/images/HkZyXs3A-.gif",
    "https://cdn.weeb.sh/images/Sk1k3TdPW.gif",
    "https://cdn.weeb.sh/images/HklBtCvTZ.gif",
    "https://cdn.weeb.sh/images/ryFdQRtF-.gif",
    "https://cdn.weeb.sh/images/H1a42auvb.gif",
    "https://cdn.weeb.sh/images/SJSr3TOv-.gif",
    "https://cdn.weeb.sh/images/SJINn6OPW.gif",
    "https://cdn.weeb.sh/images/ryoW3T_vW.gif",
    "https://cdn.weeb.sh/images/r1mcJlFVz.gif",
    "https://cdn.weeb.sh/images/BJSdQRtFZ.gif",
    "https://cdn.weeb.sh/images/ByTBhp_vZ.gif",
    "https://cdn.weeb.sh/images/Bkuk26uvb.gif",
    "https://cdn.weeb.sh/images/rkM4nTOPb.gif",
    "https://cdn.weeb.sh/images/SJ8I2Tuv-.gif",
    "https://cdn.weeb.sh/images/rJoL2pdvb.gif"
]

kissm = [
    "{auth} kisses {mem} OwO!",
    "{auth} just kissed {mem} :O",
    "{mem} recieved a beautiful kiss from {auth} -3-",
    "{mem} blushes as {auth} kissed him/her #-#",
    ]

smileg = [
  'https://media.giphy.com/media/ree8xCap5nHi/giphy.gif',
  'https://media.giphy.com/media/ivibkKm68n3a/giphy.gif',
  'https://thumbs.gfycat.com/OblongAdoredGoshawk-size_restricted.gif',
  'https://media0.giphy.com/media/rFfmUWVMOyKVG/source.gif',
  'https://media1.tenor.com/images/6c115f367d18498f4d4b8d561a8445a2/tenor.gif?itemid=11672437',
  'https://media.giphy.com/media/arzM4yh4TgeNW/giphy.gif',
  'https://thumbs.gfycat.com/SplendidBeautifulFieldspaniel-size_restricted.gif',
  'https://data.whicdn.com/images/320836413/original.gif',
  'http://cdn63.picsart.com/191956697002202.gif',
  'https://i.pinimg.com/originals/ef/c9/47/efc9470fad6963192c9273e0c975ffb5.gif',
  'https://i.kym-cdn.com/photos/images/newsfeed/001/139/889/b3a.gif',
  'http://i.imgur.com/Y5o48VW.gif'
]

smilem = [
  "{auth} smiles at {mem} OwO!",
  "{auth} just smiled at {mem} feelings :O?!!?",
  "{mem} recieved a big smile from {auth} -3-"
]

pokeg = [
  'https://i.pinimg.com/originals/9d/25/23/9d25235a88f0fb52c3b72bf9404d2b7e.gif',
  'https://thumbs.gfycat.com/ConventionalIlliterateFattaileddunnart-size_restricted.gif',
  'https://media1.tenor.com/images/3b9cffb5b30236f678fdccf442006a43/tenor.gif?itemid=7739077',
  'https://media1.tenor.com/images/01b264dc057eff2d0ee6869e9ed514c1/tenor.gif?itemid=14346763',
  'https://gifimage.net/wp-content/uploads/2017/09/anime-poke-gif-9.gif',
  'https://media.giphy.com/media/vqRI8gmKvrTOM/giphy.gif',
  'https://thumbs.gfycat.com/ImprobableAdorableGardensnake-size_restricted.gif',
  'http://i.imgur.com/oyIXHxY.gif'
]


pokem = [
  '{auth} poked {mem} o0o!',
  '{mem} just got poked by {auth} -3-',
  '{mem recieves a pokey pokey from {auth} =-=}'
]

clist = [
    0xeb4034,
    0x75f6ff,
    0xca75ff,
    0xff526c,
    0xdaff61,
    0xff9245
]

#Lists

class Nuwu(commands.Cog):
    def __init__(self, bot):
        self.patg = patg
        self.kissg = kissg
        self.smileg = smileg
        self.pokeg = pokeg
        #Gifs

        self.patm = patm
        self.kissm = kissm
        self.smilem = smilem
        self.pokem = pokem
        #Messages

        self.clist = clist
        #Others

    @commands.command()
    async def pat(self, ctx):
        fauth = ctx.author.id
        auth = f'<@!{fauth}>'
        mem = ctx.message.content.split(' ')[1]
        msg = rand(self.patm)
        #Variables
        if mem == auth:
            await ctx.send('A-are you feeling lonely? ;c')
        elif mem != auth:
            patbed = discord.Embed(description=msg.format(mem=mem, auth=auth), color=discord.Color(rand(self.clist)))
            patbed.set_image(url=rand(self.patg))
            await ctx.send(embed=patbed)
        #Message Sending

    @commands.command()
    async def kiss(self, ctx):
        fauth = ctx.author.id
        auth = f'<@!{fauth}>'
        mem = ctx.message.content.split(' ')[1]
        msg = rand(self.kissm)
        #Variables
        if mem == auth:
            await ctx.send('Y-y-you c-cant kiss yourself ^0^!')
        elif mem != auth:
            kissbed = discord.Embed(description=msg.format(mem=mem, auth=auth), color=discord.Color(rand(self.clist)))
            kissbed.set_image(url=rand(self.kissg))
            await ctx.send(embed=kissbed)
        #Message Sending

    @commands.command()
    async def smile(self, ctx):
        fauth = ctx.author.id
        auth = f'<@!{fauth}>'
        mem = ctx.message.content.split(' ')[1]
        msg = rand(self.smilem)
        #Variables

        if mem == auth:
            await ctx.send('W-well you can always smile in the mirror -3-')
        elif mem != auth:
            smilebed = discord.Embed(description=msg.format(mem=mem, auth=auth), color=discord.Color(rand(self.clist)))
            smilebed.set_image(url=rand(self.smileg))
            await ctx.send(embed=smilebed)
        #Message Sending

    @commands.command()
    async def poke(self, ctx):
        fauth = ctx.author.id
        auth = f'<@!{fauth}>'
        mem = ctx.message.content.split(' ')[1]
        msg = rand(self.pokem)
        #Variables

        if mem == auth:
            await ctx.send('Hey! Y-you cant poke yourself 😤')
        elif mem != auth:
            smilebed = discord.Embed(description=msg.format(mem=mem, auth=auth), color=discord.Color(rand(self.clist)))
            smilebed.set_image(url=rand(self.pokeg))
            await ctx.send(embed=smilebed)
        #Message Sending


#Class
