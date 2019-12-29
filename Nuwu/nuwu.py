import discord
from discord.ext import commands
#Discord Framework

from redbot.core import Config
from redbot.core import commands
#Redbot Framework

import re
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
  'https://tinyurl.com/sqpd32d',
  'https://tinyurl.com/v2bw45p',
  'https://tinyurl.com/vs837wy',
  'https://tinyurl.com/qtfv86r',
  'https://tinyurl.com/t8uruwz',
  'https://tinyurl.com/tsxcqb4',
  'https://tinyurl.com/sxxw945',
  'https://tinyurl.com/uc8qhsl',
  'https://tinyurl.com/shcuo5q',
  'https://tinyurl.com/w3ora95',
  'https://tinyurl.com/rz97mrw',
  'https://tinyurl.com/sbsbehy',
  'https://tinyurl.com/tohxyhm',
  'https://tinyurl.com/se3kddj',
  'https://tinyurl.com/vqwwf24',
  'https://tinyurl.com/tlrj7zl',
  'https://tinyurl.com/wpgpwjp',

]

smilem = [
  "{auth} smiles at {mem} OwO!",
  "{auth} just smiled at {mem} feelings :O?!!?",
  "{mem} recieved a big smile from {auth} -3-"
]

pokeg = [
  'https://tinyurl.com/vn2es66',
  'https://tinyurl.com/shto3tc',
  'https://tinyurl.com/wrc7soc',
  'https://tinyurl.com/vx4jb58',
  'https://tinyurl.com/u8n6rsk',
  'https://tinyurl.com/v3wtwrk',
  'https://tinyurl.com/qrsxchw',
  'https://tinyurl.com/w2k87tc',
  'https://tinyurl.com/wjzyrsh',
  'https://tinyurl.com/snc3fbz',
  'https://tinyurl.com/ueqqfeh',
  'https://tinyurl.com/yx5ualte',
  'https://tinyurl.com/tu3bmvg',
  'https://tinyurl.com/u63ezhm',
  'https://tinyurl.com/y6wqvm93',
  'https://tinyurl.com/rdmjkw9',
  'https://tinyurl.com/qlcuehm',
  'https://tinyurl.com/thbft72'
]


pokem = [
  '{auth} poked {mem} o0o!',
  '{mem} just got poked by {auth} -3-',
  '{mem recieves a pokey pokey from {auth} =-=}'
]


lickg = [
  'https://tinyurl.com/r9pf8dd',
  'https://tinyurl.com/ukaxkl9',
  'https://tinyurl.com/vjxtj75',
  'https://tinyurl.com/sys2xqp',
  'https://tinyurl.com/wzghhdt',
  'https://tinyurl.com/vjypp36',
  'https://tinyurl.com/sx5bqcs',
  'https://tinyurl.com/uq7exyw',
  'https://tinyurl.com/uq7exyw',
  'https://tinyurl.com/twe7rbm',
  'https://tinyurl.com/vnsw6j3',
  'https://tinyurl.com/r2rgfnx',
  'https://tinyurl.com/tne6atv',
  'https://tinyurl.com/udq6nxc',
  'https://tinyurl.com/vdmwg9j',
  'https://tinyurl.com/vrrrzpj',
  'https://tinyurl.com/ukav5lp',
  'https://tinyurl.com/y9z86edv'
]

lickm = [
  'D-did {auth} j-just lick {mem}?!?',
  '{auth} i-is licking {mem} 1.1!!',
  '{mem} j-just got licked by {auth} 0-0...',

]

killg = [
    'https://tinyurl.com/tajkkcw',
    'https://tinyurl.com/rkb9yes',
    'https://tinyurl.com/rrbunuq',
    'https://tinyurl.com/stoyu4q',
    'https://tinyurl.com/rpe8tjk',
    'https://tinyurl.com/rpe8tjk',
    'https://tinyurl.com/sk69fwx',
    'https://tinyurl.com/r5jwyk6',
    'https://tinyurl.com/tmzdm6x',
    'https://tinyurl.com/qpvkvct',
    'https://tinyurl.com/vg65mvv'
]

killm = [
    '{auth} annihilated {mem} Uhoh...',
    '{mem} got killed by {auth}!',
    '{mem} died by the hands of {auth} 00F!'
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
class Converter:
    async def convert(self, ctx, argument):
        raise NotImplementedError('Derived classes need to implement this.')

class IDConverter(Converter):
    def __init__(self):
        self._id_regex = re.compile(r'([0-9]{15,21})$')
        super().__init__()

    def _get_id_match(self, argument):
        return self._id_regex.match(argument)


class Nuwu(commands.Cog, IDConverter):
    def __init__(self, bot):
        self.patg = patg
        self.kissg = kissg
        self.smileg = smileg
        self.pokeg = pokeg
        self.lickg = lickg
        self.killg = killg
        #Gifs

        self.patm = patm
        self.kissm = kissm
        self.smilem = smilem
        self.pokem = pokem
        self.lickm = lickm
        self.killm = killm
        #Messages

        self.clist = clist
        #Others

    @commands.command()
    async def pat(self, ctx, member):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        match = self._get_id_match(member) or re.match(r'<@!?([0-9]+)>$', member)
        guild = ctx.guild
        msg = rand(self.patm)
        #Variables
        if member == auth:
            await ctx.send('A-are you feeling lonely? ;c')
        if member != auth:
            pass
        if match is None:
            await ctx.send(f':x: **{member}** is not in the server, please use the correct syntax | [p]pat <member>')
            return False
        if guild:
            patbed = discord.Embed(description=msg.format(mem=member, auth=auth), color=discord.Color(rand(self.clist)))
            patbed.set_image(url=rand(self.patg))
            await ctx.send(embed=patbed)
        #Message Sending

    @commands.command()
    async def kiss(self, ctx, member):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        match = self._get_id_match(member) or re.match(r'<@!?([0-9]+)>$', member)
        guild = ctx.guild
        msg = rand(self.kissm)
        #Variables

        if member == auth:
            await ctx.send('Y-y-you c-cant kiss yourself ^0^!')
            return False
        if member != auth:
            pass
        if match is None:
            await ctx.send(f':x: **{member}** is not in the server, please use the correct syntax | [p]kiss <member>')
            return False
        if guild:
            kissbed = discord.Embed(description=msg.format(mem=member, auth=auth), color=discord.Color(rand(self.clist)))
            kissbed.set_image(url=rand(self.kissg))
            await ctx.send(embed=kissbed)
        #Message Sending

    @commands.command()
    async def smile(self, ctx, member):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        match = self._get_id_match(member) or re.match(r'<@!?([0-9]+)>$', member)
        guild = ctx.guild
        msg = rand(self.smilem)
        #Variables
        if member == auth:
            await ctx.send('I-im not a mirror -3-')
            return False
        if member != auth:
            pass
        if match is None:
            await ctx.send(f':x: **{member}** is not in the server, please use the correct syntax | [p]smile <member>')
            return False
        if guild:
            smilebed = discord.Embed(description=msg.format(mem=member, auth=auth), color=discord.Color(rand(self.clist)))
            smilebed.set_image(url=rand(self.smileg))
            await ctx.send(embed=smilebed)
        #Message Sending

    @commands.command()
    async def poke(self, ctx, member):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        match = self._get_id_match(member) or re.match(r'<@!?([0-9]+)>$', member)
        guild = ctx.guild
        msg = rand(self.pokem)
        #Variables
        if member == auth:
            await ctx.send('Hey! D-dont poke yourself 😤')
            return False
        if member != auth:
            pass
        if match is None:
            await ctx.send(f':x: **{member}** is not in the server, please use the correct syntax | [p]poke <member>')
            return False
        if guild:
            pokebed = discord.Embed(description=msg.format(mem=member, auth=auth), color=discord.Color(rand(self.clist)))
            pokebed.set_image(url=rand(self.pokeg))
            await ctx.send(embed=pokebed)
        #Message Sending

    @commands.command()
    async def lick(self, ctx, member):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        match = self._get_id_match(member) or re.match(r'<@!?([0-9]+)>$', member)
        guild = ctx.guild
        msg = rand(self.lickm)
        #Variables

        if member == auth:
            await ctx.send('H-how do you lick yourself 0-0...')
            return False
        if member != auth:
            pass
        if match is None:
            await ctx.send(f':x: **{member}** is not in the server, please use the correct syntax | [p]lick <member>')
            return False
        if guild:
            lickbed = discord.Embed(description=msg.format(mem=member, auth=auth), color=discord.Color(rand(self.clist)))
            lickbed.set_image(url=rand(self.lickg))
            await ctx.send(embed=lickbed)

    @commands.command()
    async def kill(self, ctx, member):
        fauth = ctx.message.author.id
        auth = f'<@!{fauth}>'
        match = self._get_id_match(member) or re.match(r'<@!?([0-9]+)>$', member)
        guild = ctx.guild
        msg = rand(self.killm)
        #Variables

        if member == auth:
            await ctx.send('P-please d-d-dont commit suicide...')
            return False
        if member != auth:
            pass
        if match is None:
            await ctx.send(f':x: **{member}** is not in the server, please use the correct syntax | [p]kill <member>')
            return False
        if guild:
            killbed = discord.Embed(description=msg.format(mem=member, auth=auth), color=discord.Color(rand(self.clist)))
            killbed.set_image(url=rand(self.killg))
            await ctx.send(embed=killbed)
#Class
###################
#Finished Commands#
###################
# -Smile
# -Pat
# -Poke
# -Kiss
# -Lick
# -Kill

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
