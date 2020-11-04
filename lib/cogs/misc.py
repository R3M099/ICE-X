from discord.ext.commands import Cog, command, CheckFailure, has_permissions, MissingRequiredArgument, Greedy
from discord import Member
import json
#from ..db import db

class Misc(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name = "prefix")
	@has_permissions(administrator = True)
	async def change_prefix(self, ctx, new):

		if len(new) > 2:
			await ctx.send("Command prefix cannot be more then 2 characters long")

		else:
			with open("./lib/cogs/prefixes.json", "r") as pf:
				prefixes = json.load(pf)

			prefixes[str(ctx.guild.id)] = new

			with open("./lib/cogs/prefixes.json", "w") as pf:
				json.dump(prefixes, pf, indent = 4)

			await ctx.send(f"Prefix set to `{new}` succesfully")

	@change_prefix.error
	async def change_prefix_error(self, ctx, exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Missing required permissions to execute that command")

		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("one or more required arguments are missing")

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("misc")

def setup(bot):
	bot.add_cog(Misc(bot))
