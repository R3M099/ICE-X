from discord.ext.commands import Cog, command, cooldown, BucketType
from aiohttp import request
from discord import Embed
from typing import Optional
import datetime

class Astronomy(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name = "apod")
	@cooldown(1, 20, BucketType.user)
	async def apod(self, ctx):
		'''Sends Astronomy Picture of the day'''
		t = datetime.datetime.utcnow()
		
		API_KEY = "API_KEY"
		
		apod_url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

		async with request("GET", apod_url, headers = {}) as response:
			if response.status == 200:
				data = await response.json()
				image_link = data["hdurl"]
			else:
				image_link = None	

		async with request("GET", apod_url, headers = {}) as response:
			
			if response.status == 200:
				data = await response.json()
				e = Embed(title = data["title"], 
						  description = data["explanation"], 
						  colour = 0x1a1d56)

				e.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
				if image_link is not None:
					e.set_image(url = image_link)
				e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
				await ctx.send(embed = e)

			else:
				await ctx.send(f'API returned a {response.status} status')

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("astronomy")

def setup(bot):
	bot.add_cog(Astronomy(bot))
