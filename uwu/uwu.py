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
from .messages import wave_msg, self_wave_msg
from .messages import bang_msg, self_bang_msg
from .messages import kill_msg, self_kill_msg
from .messages import kiss_msg, self_kiss_msg
#Action Message Imports

from .gifs import pat_gif, cuddle_gif, slap_gif
from .gifs import wave_gif, bang_gif, kill_gif
from .gifs import kiss_gif
#Action Gif Imports

from .messages import excited_msg, happy_msg
#Emote Message Imports

from .gifs import excited_gif, happy_gif
#Emote Gif Imports

clist = [
    0xeb4034,
    0x75f6ff,
    0xca75ff,
    0xff526c,
    0xdaff61,
    0xff9245
]
#Color List

class uwu(commands.Cog):
    def __init__(self, bot):
        self.pat_gif = pat_gif
        self.cuddle_gif = cuddle_gif
        self.slap_gif = slap_gif
        self.wave_gif = wave_gif
        self.bang_gif = bang_gif
        self.kill_gif = kill_gif
        self.kiss_gif = kiss_gif
        #Action Gifs

        self.excited_gif = excited_gif
        self.happy_gif = happy_gif
        #Emote Gifs
        
        self.pat_msg = pat_msg
        self.cuddle_msg = cuddle_msg
        self.slap_msg = slap_msg
        self.excited_msg = excited_msg
        self.wave_msg = wave_msg
        self.bang_msg = bang_msg
        self.kill_msg = kill_msg
        self.kiss_msg = kiss_msg
        #Action Messages
        
        self.excited_msg = excited_msg
        self.happy_msg = happy_msg
        #Emote Messages
        
        self.selfpat_msg = self_pat_msg
        self.selfcuddle_msg = self_cuddle_msg
        self.selfslap_msg = self_slap_msg
        self.selfwave_msg = self_wave_msg
        self.selfbang_msg = self_bang_msg
        self.selfkill_msg = self_kill_msg
        self.selfkiss_msg = self_kiss_msg
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
        
    @commands.command()
    async def wave(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.wave_msg)
        self_msg = rand(self.selfwave_msg)
        
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        
        else:
            wavebed = discord.Embed(color=discord.Color(rand(self.clist)))
            wavebed.set_image(url=rand(self.wave_gif))
            wavebed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=wavebed)
        #Wave Command
    
    @commands.command()
    async def bang(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.bang_msg)
        self_msg = rand(self.selfbang_msg)
        
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        
        else:
            bangbed = discord.Embed(color=discord.Color(rand(self.clist)))
            bangbed.set_image(url=rand(self.bang_gif))
            bangbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=bangbed)
        #Bang Command
    
    @commands.command()
    async def kill(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.kill_msg)
        self_msg = rand(self.selfkill_msg)
        
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        
        else:
            killbed = discord.Embed(color=discord.Color(rand(self.clist)))
            killbed.set_image(url=rand(self.kill_gif))
            killbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=killbed)
        #Kill Command
    
    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.kiss_msg)
        self_msg = rand(self.selfkiss_msg)
        
        if member == ctx.author:
            return await ctx.send(self_msg.format(auth=auth.display_name))
        
        else:
            kissbed = discord.Embed(color=discord.Color(rand(self.clist)))
            kissbed.set_image(url=rand(self.kiss_gif))
            kissbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            
            await ctx.send(embed=kissbed)
        #Kiss Command
    
#################        
#Emote Commands        
#################

    @commands.command()
    async def excited(self, ctx):
        auth = ctx.author
        msg = rand(self.excited_msg)
        
        excitedbed = discord.Embed(color=discord.Color(rand(self.clist)))
        
        excitedbed.set_image(url=rand(self.excited_gif))
        excitedbed.set_author(name=msg.format(auth=auth.display_name), icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=excitedbed)
        
    @commands.command()
    async def happy(self, ctx):
        auth = ctx.author
        msg = rand(self.happy_msg)
        
        happybed = discord.Embed(color=discord.Color(rand(self.clist)))
        
        happybed.set_image(url=rand(self.happy_gif))
        happybed.set_author(name=msg.format(auth=auth.display_name), icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=happybed)
        

################        
#Commands To Add#
################
# -Smile
# -Pat -Done
# -Poke
# -Kiss -Done
# -Lick
# -Kill
# -Punch
# -Happy -Done
# -Excited -Done
# -Cuddle -Done
# -Insult
# -Nom
# -Slap -Done
# -Stare
# -Highfive
# -Bite
# -Handholding
# -Tickle
# -Kill
# -Hold
# -Wave -Done
# -Boop
# -Bully
