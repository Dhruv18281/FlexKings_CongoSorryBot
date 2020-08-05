import os
import discord
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')
Guild = os.getenv('DISCORD_GUILD')

client = discord.Client()
channel = client.get_channel(647444665955516457)
bot = commands.Bot(command_prefix = 'fk!')

#random text id = 647444665955516457
#text id = 581149640448016401

@bot.event
async def on_ready():
	g = discord.utils.get(bot.guilds, name=Guild)
	print(f'{bot.user} has joined the battle. Welcome King\n'
	f'{g.name}(id: {g.id})'
	)
	
	members = '\n - '.join([member.name for member in g.members])
	print(f'Guild Members:\n - {members}')

@bot.event
async def on_member_join(member):
	r = random.randint(1, 5)
	channel = bot.get_channel(647444665955516457)
	if r==1:
		await channel.send(f'> {member.mention} has joined the battle. Welcome King')
	elif r==2:
		await channel.send(f"> OwO, what's this, {member.mention} is here")
	elif r==3:
		await channel.send(f'> Why do I hear Boss Music? OH GOD {member.mention} IS HERE!!!!')
	elif r==4:
		await channel.send(f'> Congratulations {member.mention}')
	else:
		await channel.send(f'> Sorry {member.mention}')

async def background_loop():
	await bot.wait_until_ready()
	while True:
		peeps = []
		g = discord.utils.get(bot.guilds, name=Guild)
		channel = bot.get_channel(647444665955516457)
		for m in g.members:
			if m.bot:
				continue
			for r in m.roles:
				if r.name == 'reconSquad':
					peeps.append(m)
		rand1 = random.randint(1, 3)
		rand2 = random.randint(1, 3)
		member = random.choice(peeps)
		print("looping")
		if rand1 == 1:
			if rand2 == 1:
				await channel.send(f'> Congratulations, {member.mention}')
			elif rand2 == 2:
				await channel.send(f'> Very very congo, {member.mention}')
			else:
				await channel.send(f'> Everybody, go and congratulate {member.mention}')
		elif rand1 == 2:
			if rand2 == 1:
				await channel.send(f'> Sorry, {member.mention}')
			elif rand2 == 2:
				await channel.send(f'> sorri bhai {member.mention}, very sorri')
			else:
				await channel.send(f'> Gib maafi plox, {member.mention}')
		else:
			if rand2 == 1:
				await channel.send(f'> Congratulations and Sorry {member.mention}')
			elif rand2 == 2:
				await channel.send(f'> rip in pieces, {member.mention}')
			else:
				await channel.send(f'> I lub you, {member.mention}')
		print("printed")
		h = random.randint(30, 60) * 60
		print(h)
		await asyncio.sleep(h)
		print("ready for next")
	print("out while")

@bot.command(name = '8ball')
async def magicball(ctx):
	print("command chala")
	positive = ["Yes", "Definitely", "100% Brooo", "The Universe is asking me to answer, Yes", "Yops"]
	negative = ["No", "Definitely Not", "Na bhai na, bilkul nhi", "The Universe is asking me to answer, No", "Nops"]
	confused = ["Hmmm...Maybe", "Not sure", "Ehhh..IDK bro"]
	roast = ["Kya tatti question hai", "Jaa na, tang mat kar", "I never thought I would hear such a stupid question in my lifetime"]
	rand = random.randint(1, 10)
	print(rand)
	if rand in range(1, 4):
		await ctx.send(f'> ' + random.choice(positive))
	elif rand in range(4, 7):
		await ctx.send(f'> ' + random.choice(negative))
	elif rand in range(7, 10):
		await ctx.send(f'> ' + random.choice(confused))
	else:
		await ctx.send(f'> ' + random.choice(roast))

@bot.command(name = 'test')
async def test(ctx):
	await ctx.send(f'> took command')

bot.loop.create_task(background_loop())
#client.run(Token)
bot.run(Token)