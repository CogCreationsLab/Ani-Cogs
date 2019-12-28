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
  'https://media.giphy.com/media/arzM4yh4TgeNW/giphy.gif',
  'https://thumbs.gfycat.com/SplendidBeautifulFieldspaniel-size_restricted.gif',
  'https://data.whicdn.com/images/320836413/original.gif',
  'http://cdn63.picsart.com/191956697002202.gif',
  'https://i.pinimg.com/originals/ef/c9/47/efc9470fad6963192c9273e0c975ffb5.gif',
  'https://i.kym-cdn.com/photos/images/newsfeed/001/139/889/b3a.gif',
  'https://i.pinimg.com/originals/f6/82/fd/f682fd97c3bcb5c6f4bb4e84218f3f82.gif',
  'https://thumbs.gfycat.com/LeadingShortCanadagoose-size_restricted.gif',
  'https://img.buzzfeed.com/buzzfeed-static/static/2015-08/24/13/enhanced/webdr14/anigif_original-26898-1440435930-6.gif',
  'https://steamuserimages-a.akamaihd.net/ugc/89351200168033872/687AAA1ADC378839A3437E2EB1DCA201DF106EE1/',
  'https://i.pinimg.com/originals/97/c7/2b/97c72b01531ec28db47f155d43f11e66.gif',
  'http://i.imgur.com/Y5o48VW.gif',
  'https://media3.giphy.com/media/GT6hcXiYvsnxm/source.gif',

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
  'https://i.imgur.com/Zi4ahyj.gif',
  'https://ci.memecdn.com/262033.gif',
  'https://4.bp.blogspot.com/-2jQvKwLGfMs/WPbrTtTEieI/AAAAAAAAzOA/KJsetp15cqs4nTuZGUoLmoTYeDHSsOMHgCPcB/s1600/Omake%2BGif%2BAnime%2B-%2BEromanga-sensei%2B-%2BEpisode%2B2%2B-%2BTomoe%2BPokes%2BMasamune%2527s%2BCheek.gif',
  'https://i.gifer.com/S010.gif',
  'https://1.bp.blogspot.com/-0cu-3g3bio4/Vx_hCIRUcYI/AAAAAAAAcE8/mcV22O8uolst5z3Rd-reMOPhxoLLMeXaACKgB/s1600/Omake%2BGif%2BAnime%2B-%2BKuma%2BMiko%2B-%2BEpisode%2B4%2B-%2BMachi%2BCheek%2BPoke.gif',
  'https://media.tenor.com/images/0e20ef804a6ecdd9dcb8065e7390963f/tenor.gif',
  'https://media.tenor.com/images/814ed3218c9899cdb79c3d9f5573495d/tenor.gif',
  'https://pa1.narvii.com/6946/d5b18a40da583b359f2e953c1c7abe27f4c28b21r1-600-338_hq.gif',
  'https://media1.tenor.com/images/ce3593d0d5052339cdae55ed0d75e7aa/tenor.gif?itemid=9966199',
  'https://thumbs.gfycat.com/PlainHeartyGonolek-size_restricted.gif',
  'http://i.imgur.com/oyIXHxY.gif'
]


pokem = [
  '{auth} poked {mem} o0o!',
  '{mem} just got poked by {auth} -3-',
  '{mem recieves a pokey pokey from {auth} =-=}'
]


lickg = [
  'https://media.giphy.com/media/x4P8TaYhGn4FW/giphy.gif',
  'https://i.gifer.com/CAmE.gif',
  'https://media.giphy.com/media/8GiREm7aqMwN2/200.gif',
  'https://ci.memecdn.com/5938991.gif',
  'https://68.media.tumblr.com/b80cda919b3309f2cb974635e429db57/tumblr_osuazevFcj1qcsnnso1_500.gif',
  'https://i.kym-cdn.com/photos/images/newsfeed/000/996/752/fdf.gif',
  'https://pa1.narvii.com/5748/477a68bdbb9eaa255263eb970fda433b7dc7a38b_hq.gif',
  'https://media1.tenor.com/images/4626d4bbe60ef15212e3181f11d6704a/tenor.gif?itemid=13451633',
  'https://66.media.tumblr.com/1074acf4d3e68a0a94ab7c9d5eea6e7f/tumblr_njxe8wuAup1snkggso1_500.gif',
  'https://media1.tenor.com/images/b4b16656ced5859d917c889709592b5d/tenor.gif?itemid=4863352',
  'https://i.kym-cdn.com/photos/images/original/001/093/355/909.gif',
  'https://33.media.tumblr.com/799d48bdb36dcbe6ee5717630f74e504/tumblr_n0bxdsE4M11rb3ea0o1_500.gif',
  'https://38.media.tumblr.com/b0dea211949e13cd9c221ac6c3461da6/tumblr_nlhtufSUA61qbb4ago1_500.gif',
  'https://media.tenor.com/images/ffb9602b95fe735fd757c183d25af18f/tenor.gif',
  'https://media.tenor.com/images/3185cbd38fbf5b2e337b9a9de317c66c/tenor.gif',
  'https://media.tenor.com/images/4daf1e8ec23c3869466d446439abf70b/tenor.gif',
  'https://media1.tenor.com/images/8e16f796361326db09c5d81d18d91d28/tenor.gif?itemid=12630638',
  'https://media.tenor.com/images/46a0d241fddbbcc2f7c37a0e6cc66166/tenor.gif'
]

lickm = [
  'D-did {auth} j-just lick {mem}?!?',
  '{auth} i-is licking {mem} 1.1!!',
  '{mem} j-just got licked by {auth} 0-0...',

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
        self.lickg = lickg
        #Gifs

        self.patm = patm
        self.kissm = kissm
        self.smilem = smilem
        self.pokem = pokem
        self.lickm = lickm
        #Messages

        self.clist = clist
        #Others

    @commands.command()
    async def pat(self, ctx):
        fauth = ctx.message.author.id
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
        fauth = ctx.message.author.id
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
        fauth = ctx.message.author.id
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
        fauth = ctx.message.author.id
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

    @commands.command()
    async def lick(self, ctx, guild: discord.Guild):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        mem = ctx.message.content.split(' ')[1]
        msg = rand(self.lickm)
        #Variables
        if mem in(self.guild.members):
            await ctx.send(f'{mem} is not in the server, please use the correct syntax | [p]lick <member>')
        elif mem == auth:
            await ctx.send('H-how do you lick yourself 0-0...')
        elif mem != auth:
            smilebed = discord.Embed(description=msg.format(mem=mem, auth=auth), color=discord.Color(rand(self.clist)))
            smilebed.set_image(url=rand(self.lickg))
            await ctx.send(embed=smilebed)
        #Message Sending
#Class


#################
#Commands To Add#
################
# -Happy
# -Excited
# -Cuddle
# -Insult
# -Nom
# -Slap
# -Stare
# -Highfive
# -Bite
# -Greet
# -Punch
# -Handholding
# -Tickle
# -Kill
# -Hold
# -Wave
# -Boop
# -Snuggle
# -Bully
