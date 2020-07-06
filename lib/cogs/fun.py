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
		await ctx.send(f'Hello {ctx.author.mention}!')

	@command(name="8ball")
	@cooldown(1,10,BucketType.user)
	async def magic_ball(self,ctx,*,question):
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
		t=datetime.datetime.now()
		e=Embed(title='Pong!',
				description=f'Latency:{round(self.bot.latency*1000)}ms',
				colour=0x44AD25)
		e.set_footer(text='Today at '+t.strftime('%I:%M %p'))
		await ctx.send(embed=e)

	@command(name="say")
	async def echo_message(self,ctx,*,message):
		await ctx.message.delete()
		await ctx.send(message)

	@echo_message.error
	async def echo_message_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send('What to say?')

	@command(name="fact")
	@cooldown(1,5,BucketType.user)
	async def animal_facts(self,ctx,animal:str):
		t=datetime.datetime.now()
		if (animal:=animal.lower()) in ('dog','cat','bird'):
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
					e.set_footer(text='Today at '+t.strftime('%I:%M %p'))
					await ctx.send(embed=e)
				else:
					await ctx.send(f'API returned a {response.status} status')
		else:
			await ctx.send('No facts available for that animal.')
		
	@animal_facts.error
	async def animal_fact_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send('Provide an animal to give fact about!')

	@command(name="meme")
	@cooldown(1,5,BucketType.user)
	async def send_memes(self,ctx):
		t=datetime.datetime.now()
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
				if image_link is  not None:
					e.set_image(url=image_link)
				e.set_footer(text='Today at '+t.strftime('%I:%M %p'))
				await ctx.send(embed=e)
			else:
				await ctx.send(f'API returned a {response.status} status')
		
	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("fun")

def setup(bot):
	bot.add_cog(Fun(bot))