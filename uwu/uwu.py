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

from .messages import pat_msg, self_pat_msg
from .messages import cuddle_msg, self_cuddle_msg
from .messages import slap_msg, self_slap_msg
from .gifs import pat_gif, cuddle_gif, slap_gif
#Action Imports

#Coming Soon
#Emote Imports

clist = [
    0xeb4034,
    0x75f6ff,
    0xca75ff,
    0xff526c,
    0xdaff61,
    0xff9245
]

#Lists

class uwu(commands.Cog):
    def __init__(self, bot):
        self.pat_gif = pat_gif
        self.cuddle_gif = cuddle_gif
        self.slap_gif = slap_gif
        self.excited_gif = excited_gif
        #Gifs

        self.pat_msg = pat_msg
        self.cuddle_msg = cuddle_msg
        self.slap_msg = slap_msg
        self.excited_msg = excited_msg
        #Messages
        
        self.selfpat_msg = self_pat_msg
        self.selfcuddle_msg = self_cuddle_msg
        self.selfslap_msg = self_slap_msg
        #Self Messages
        
        self.clist = clist
        #Others

#################        
#Action Commands        
#################        
        
    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.pat_msg)
        self_msg = rand(self.selfpat_msg)
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        else:
            patbed = discord.Embed(color=discord.Color(rand(self.clist)))
            patbed.set_image(url=rand(self.pat_gif))
            patbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=patbed)
        #Pat Command
    
    @commands.command()
    async def cuddle(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.cuddle_msg)
        self_msg = rand(self.selfcuddle_msg)
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        else:
            cuddlebed = discord.Embed(color=discord.Color(rand(self.clist)))
            cuddlebed.set_image(url=rand(self.cuddle_gif))
            cuddlebed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=cuddlebed)
        #Cuddle Command     
        
    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.slap_msg)
        self_msg = rand(self.selfslap_msg)
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        else:
            slapbed = discord.Embed(color=discord.Color(rand(self.clist)))
            slapbed.set_image(url=rand(self.slap_gif))
            slapbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=slapbed)
        #Slap Command
        
#################        
#Emote Commands        
#################
#Coming Soon

#################
#Commands
################
# -Smile
# -Pat-Done
# -Poke
# -Kiss
# -Lick
# -Kill
# -Punch
# -Happy
# -Excited
# -Cuddle-Done
# -Insult
# -Nom
# -Slap-Done
# -Stare
# -Highfive
# -Bite
# -Greet
# -Handholding
# -Tickle
# -Kill
# -Hold
# -Wave
# -Boop
# -Snuggle
# -Bully
