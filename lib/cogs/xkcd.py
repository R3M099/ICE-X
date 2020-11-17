from discord.ext.commands import Cog, command, cooldown, BucketType
from discord.ext.commands import MissingRequiredArgument, BadArgument
from aiohttp import request
from discord import Embed
import random
import datetime

class Xkcd(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name = "xkcd")
	@cooldown(1, 5, BucketType.user)
	async def xkcd(self, ctx, number: int):
		t = datetime.datetime.utcnow()

		xkcd_url = f"https://xkcd.com/{number}/info.0.json"
		
		async with request("GET", xkcd_url, headers = {}) as response:
			if response.status == 200:
				data = await response.json()
				image_link = data["img"]
			else:
				image_link = None

		async with request("GET", xkcd_url, headers = {}) as response:
			if response.status == 200:
				data = await response.json()
				e = Embed(title = data["title"],
						  description = data["alt"],
						  colour = ctx.author.colour)
				e.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
				if image_link is not None:
					e.set_image(url = image_link)
				e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
				await ctx.send(embed = e)

			else:
				await ctx.send(f'API returned a {response.status} status')

	@xkcd.error
	async def xkcd_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("One or more required arguments are missing")
		if isinstance(exc, BadArgument):
			await ctx.send("number must be an integer")
	
	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("xkcd")

def setup(bot):
	bot.add_cog(Xkcd(bot))
