from discord.ext.commands import Cog
from discord.ext.commands import command,cooldown,BucketType
from aiohttp import request
from discord.ext.commands.errors import MissingRequiredArgument
from discord import Embed
import datetime
import random

class Fun(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name="hello",aliases=["hi","Hello","Hi"])
	async def say_hello(self,ctx):
		"""Greets you with a message"""
		await ctx.send(f'Hello {ctx.author.mention}!')

	@command(name="8ball")
	@cooldown(1,5,BucketType.user)
	async def magic_ball(self,ctx,*,question):
		"""Ask any question to the magic 8 Ball"""
		responses=['As I see it, yes.',
				   'Ask again later.',
               	   'Better not tell you now.',
           		   'Cannot predict now.',
           		   'Concentrate and ask again.',
               	   'Don’t count on it.',
               	   'It is certain.',
               	   'It is decidedly so.',
               	   'Most likely.',
               	   'My reply is no.',
               	   'My sources say no.',
               	   'Outlook not so good.',
               	   'Outlook good.',
               	   'Reply hazy, try again.',
               	   'Signs point to yes.',
               	   'Very doubtful.',
               	   'Without a doubt.',
               	   'Yes.',
               	   'Yes – definitely.',
               	   'You may rely on it.']
		await ctx.send(f"Question:{question}\n Answer:{random.choice(responses)}")

	@magic_ball.error
	async def magic_ball_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send('Give me a question to Answer')

	@command(name="ping")
	async def ping_pong(self,ctx):
		"""Returns the Latency of the bot"""
		t=datetime.datetime.now()
		e=Embed(title='Pong! :ping_pong:',
				description=f'Latency:{round(self.bot.latency*1000)}ms',
				colour=0x44AD25)
		e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
		await ctx.send(embed=e)

	@command(name="say")
	async def echo_message(self,ctx,*,message):
		"""Let the bot say what's in your mind"""
		await ctx.message.delete()
		await ctx.send(message)

	@echo_message.error
	async def echo_message_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send('What to say?')

	@command(name="fact")
	@cooldown(1,5,BucketType.user)
	async def animal_facts(self,ctx,animal:str):
		"""Gives a fact about the given animal"""
		t=datetime.datetime.utcnow()
		if (animal:=animal.lower()) in ('dog','cat','bird','panda','koala'):
			fact_url=f"https://some-random-api.ml/facts/{animal}"
			image_url=f"https://some-random-api.ml/img/{'birb' if animal=='bird' else animal}"
			async with request("GET",image_url,headers={}) as response:
				if response.status==200:
					data=await response.json()
					image_link=data["link"]
				else:
					image_link=None
			async with request("GET",fact_url,headers={}) as response:
				if response.status==200:
					data=await response.json()
					e=Embed(title=f'{animal.title()} fact',
							description=data["fact"],
							colour=0x3CA5C4)
					if image_link is  not None:
						e.set_image(url=image_link)
					e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
					await ctx.send(embed=e)
				else:
					await ctx.send(f'API returned a {response.status} status')
		else:
			await ctx.send('No facts available for that animal.')
		
	@animal_facts.error
	async def animal_fact_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send('Provide an animal to give fact about!\n1.dog \n2.cat \n3.bird \n4.panda \n5.koala')

	@command(name="meme")
	@cooldown(1,5,BucketType.user)
	async def send_memes(self,ctx):
		"""Sends a random meme"""
		t=datetime.datetime.utcnow()
		meme_url="https://meme-api.herokuapp.com/gimme"
		async with request("GET",meme_url,headers={}) as response:
			if response.status==200:
				data=await response.json()
				image_link=data["url"]
			else:
				image_link=None
		async with request("GET",meme_url,headers={}) as response:
			if response.status==200:
				data=await response.json()
				e=Embed(title="Here's a meme",
						description=data["title"],
						colour=0xD6CD1D)
				if image_link is not None:
					e.set_image(url=image_link)
				e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
				await ctx.send(embed=e)
				
			else:
				await ctx.send(f'API returned a {response.status} status')

	@command(name = "joke")
	@cooldown(1, 5, BucketType.user)
	async def send_jokes(self, ctx):
		'''Sends a random joke'''
		t = datetime.datetime.utcnow()
		joke_url = "https://official-joke-api.appspot.com/random_joke"
		async with request("GET", joke_url, headers = {}) as response:
			if response.status == 200:
				data = await response.json()
				e = Embed(title = data["setup"],
						  description = data["punchline"],
						  colour = ctx.author.colour)

				e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
				await ctx.send(embed = e)

			else:
				await ctx.send(f"API returned a {response.status} status")

	@command(name = "pjoke")
	@cooldown(1, 5, BucketType.user)
	async def send_programming_jokes(self, ctx):
		'''Sends a random programming joke'''
		t = datetime.datetime.utcnow()
		pjoke_url = "https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw&type=twopart"
		async with request("GET", pjoke_url, headers = {}) as response:
			if response.status == 200:
				data = await response.json()
				e = Embed(title = data["setup"],
						  description = data["delivery"],
						  colour = ctx.author.colour)

				e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
				await ctx.send(embed = e)

			else:
				await ctx.send(f"API returned a {response.status} status")

	@command(name = "cnjoke")
	@cooldown(1, 5, BucketType.user)
	async def send_Chuck_Norris_jokes(self, ctx):
		'''Sends a random Chuck Norris joke'''
		t = datetime.datetime.utcnow()
		cnjoke_url = "http://api.icndb.com/jokes/random"
		async with request("GET", cnjoke_url, headers = {}) as response:
			if response.status == 200:
				data = await response.json()
				e = Embed(description = data["value"]["joke"],
						  colour = ctx.author.colour)
				e.set_author(name = "Chuck Noris#0000")
				e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
				await ctx.send(embed = e)

			else:
				await ctx.send(f"API returned a {response.status} status")
		
	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("fun")

def setup(bot):
	bot.add_cog(Fun(bot))