import discord
#Discord Framework

from redbot.core import commands
#Redbot Framework

import time
import socket
#Other Imports

class Porto(commands.Cog):
    @commands.command()
    async def porto(self, ctx, ipv4, port1, port2):
        open_ports = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockbed = discord.Embed(
        title = 'OPEN PORTS',
        color= discord.Color(0x7bf542)
        )
        for p in open_ports:
            sockbed.add_field(p)
        #Variables

        await ctx.send(f'*[+] SCANNING **{ipv4}** FOR OPEN PORTS[+]*')
        #Confirmation message

        for port in range(int(port1), int(port2)):
            if sock.connect_ex((ipv4, port)):
                open_ports.append(port)
                #Adding open ports to list
            else:
                pass
                #If not open pass
