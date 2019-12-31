import discord
#Discord Framework

from redbot.core import commands
#Redbot Framework

import time
import socket
#Other Imports

class Porto(commands.Cog):
    @commands.command()
    async def porto(self, ctx, ipv4):
        open_ports = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockbed = discord.Embed(
        title = 'OPEN PORTS',
        color= discord.Color(0x7bf542)
        )
        sockbed.add_field(open_ports)
        #Variables

        await ctx.send(f'[+] SCANNNING {ipv4} FOR OPEN PORTS[+]')
        #Confirmation message

        for port in range(80,65500):
            if s.connect_ex((ipv4, port)):
                open_ports.append(port)
                #Adding open ports to list
            else:
                pass
                #If not open pass
