#import required depends
import discord
import requests
import json
from discord.ext import commands
from discord import FFmpegPCMAudio

#import Bot Token 
from apikeys import *

# Intents for the bot
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '/', intents=intents)




async def on_ready():
	print("I'm being useful.")
	print("----------------")



@client.command()
async def helpme(ctx):
	await ctx.send("The commands are /speak, /join1, /leave")



@client.command()
async def speak(ctx):
	source = FFmpegPCMAudio("crazy.mp3", executable="ffmpeg") # Use own mp3 file
	ctx.voice_client.play(source, after=None)



@client.command(pass_context = True)
async def join1(ctx):
	if (ctx.author.voice):
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
		#source = FFmpegPCMAudio('crazy.mp3')  
		#player = voice.play(source)
		# Will implement this if I disable the /speak command.
		
	else:
		await ctx.send("User is not in a voice channel.")



@client.command(pass_context = True)
async def leave(ctx):
	if (ctx.voice_client):
		await ctx.guild.voice_client.disconnect()
		await ctx.send("Left the voice channel")

	else:
		await ctx.send("I am not in a voice channel.")


client.run(BOTTOKEN) # Token ommited for security