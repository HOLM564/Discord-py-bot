import discord
from discord.ext import commands
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import random
import asyncio
from discord.ext import commands
from discord.utils import get
from discord import Embed, Color
import os
import aiofiles
import praw
import giphy_client
from giphy_client.rest import ApiException
from discord.ext import commands
from discord.utils import get
import requests
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio
import pafy
from discord.ext import commands
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import aiohttp



from random import choice

from discord.ext import commands, tasks

def add(x:float ,y: float): 
	return x+y

def mul(x:float ,y: float): 
	return x*y

def sub(x:float ,y: float): 
	return x-y

def div(x:float ,y: float): 
	return x/y




client = discord.Client()
client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    activity = discord.Activity(name='?help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("makám")

@client.command(aliases=['vymazat'])
async def clear(ctx, amount=0):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('nemáš právo')
        return
    amount = amount+0
    if amount > 101:
        await ctx.send('Mužu smazat jen 100 zpráv!')
    else: 
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Bylo smazáno {amount} zpráv!')

@client.command()
async def avatar(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    
    icon_url = member.avatar_url 
 
    avatarEmbed = discord.Embed(title = f"{member.name} Avatar")
 
    avatarEmbed.set_image(url = f"{icon_url}")
 
    avatarEmbed.timestamp = ctx.message.created_at 
 
    await ctx.send(embed = avatarEmbed)

@client.command()
async def poll(ctx, *, question=None):
    if question == None:
        await ctx.send("Napiš něco!")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "Nové hlasování!", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Hlasovaní udělal {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)
 
    await poll_msg.add_reaction("⬆️")
    await poll_msg.add_reaction("⬇️")

@client.command()
async def say(ctx, *, question=None):
    if question == None:
        await ctx.send("")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Napsal {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)

@client.command(case_insensitive=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} byl vyhozen {ctx.guild}!')
 
@client.command(case_insensitive=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} byl zabanovaní {ctx.guild}!')
@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " Byl zamčen!")

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " Byl odemčen!")

@client.command(pass_context = True)
async def randomnumber(ctx):
    embed = discord.Embed(title = "Random číslo", description = (random.randint(1, 101)), color = (0x000000))
    await ctx.send(embed = embed)

@client.command()
async def howgay(ctx, member: discord.Member=None):
    if member == None:

        member = ctx.author
    embed = discord.Embed(title = f"{member.name} Je gay z",                                          description = (random.randint(1, 101)), color = (0x000000))
    await ctx.send(embed = embed)
 
    
 
    

@client.command()
async def L(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    
    icon_url = member.avatar_url 
 
    avatarEmbed = discord.Embed(title = f"{member.name} Je L")
 
    avatarEmbed.timestamp = ctx.message.created_at 
 
    await ctx.send(embed = avatarEmbed)

@client.command()
async def invite(ctx):
    em = discord.Embed(title=" ", colour=000000)
    em.set_author(name="")
    em.add_field(name="přidej si bota na server", value="https://discord.com/api/oauth2/authorize?client_id=890255645608124446&permissions=8&scope=bot")
    await ctx.send(embed=em)

@client.command()
async def ping(ctx):

    await ctx.channel.send(f"Pong {round(client.latency*1000)} ms")

@client.command(description="Gets info about the user")
async def userinfo(ctx):
    user = ctx.author
                 

    
   
    embed=discord.Embed(title="UŽIVATELSKÉ INFORMACE", description=f"Zde jsou informace uživatele: {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Jmeno", value=user.name, inline=True)
    embed.add_field(name="Přezdívka", value=user.nick, inline=True)
    embed.add_field(name="Id", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Nejlepší role", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)


@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Umlčen {member.mention} za {reason}")
    await member.send(f"Byl jsi umlčen ze serveru {guild.name} za {reason}")


@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Odmlčen {member.mention}")
    await member.send(f"Byl jsi odmlčen ze serveru {ctx.guild.name}")




@client.command(name='server',help='Displays Server details')
async def server(ctx):
	name=str(ctx.guild.name)
	description=str(ctx.guild.description)

	owner=str(ctx.guild.owner)
	id=str(ctx.guild.id)
	region=str(ctx.guild.region)
	memberCount=str(ctx.guild.member_count)


	icon=str(ctx.guild.icon_url)

	embed=discord.Embed(title=name+" Informace",description=description,color=discord.Color.blue())
	embed.set_thumbnail(url=icon)
	embed.add_field(name="Majite",value=owner,inline=True)
	embed.add_field(name="Server id",value=id,inline=True)
	embed.add_field(name="Region",value=region,inline=True)
	embed.add_field(name="Počet členu",value=memberCount,inline=True)

	await ctx.send(embed=embed)

@client.command()
async def matplus(ctx,x:float,y:float):
	res=add(x,y)
	await ctx.send(res)

@client.command()
async def matkrat(ctx,x:float,y:float):
	res=mul(x,y)
	await ctx.send(res)
    
@client.command()
async def matminus(ctx,x:float,y:float):
	res=sub(x,y)
	await ctx.send(res)
    
@client.command()
async def matdeleni(ctx,x:float,y:float):
	res=div(x,y)
	await ctx.send(res)


@client.command()
async def help(ctx):
    em = discord.Embed(title=" ", colour=000000)
    em.set_author(name="")
    em.add_field(name="ping", value="pošle latenci bota")
    em.add_field(name="say", value="napíše správu")
    em.add_field(name="lock", value="zamče kanál")
    em.add_field(name="unlock", value="odemče kanál")
    em.add_field(name="ban", value="zabanuje uživatele")
    em.add_field(name="kick", value="vyhodí uživatele")
    em.add_field(name="mute", value="umlčí uživatele")
    em.add_field(name="unmute", value="odmlčí uživatele")
    em.add_field(name="clear", value="vymaže správy")
    em.add_field(name="server", value="pošle informace o serveru ")
    em.add_field(name="userinfo", value="pošle informace o uživatelovi ")
    em.add_field(name="L", value="napíše o někom že je L")
    em.add_field(name="howgay", value="napíše z kolika procent jseš gay")
    em.add_field(name="randomnumber", value="pošle random číslo")
    em.add_field(name="matplus", value="1+1")
    em.add_field(name="matminus", value="1-1")
    em.add_field(name="matkrat", value="1*1")
    em.add_field(name="matdeleni", value="1/1")
    
    await ctx.send(embed=em) 


client.run('TOKEN')
