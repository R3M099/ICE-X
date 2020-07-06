from discord.ext.commands import Cog,command
from discord import Forbidden

class Welcome(Cog):
	def __init__(self,bot):
		self.bot=bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("Welcome")

	@Cog.listener()
	async def on_member_join(self,member):
		try:
			await member.send(f"Welcome to ***{member.guild.name}***! Enjoy your stay here!!")
		except Forbidden:
			pass

	@Cog.listener()
	async def on_member_remove(self,member):
		try:
			await member.send(f"You have left ***{member.guild.name}***, hope to see you again!!")
		except Forbidden:
			pass
		
def setup(bot):
	bot.add_cog(Welcome(bot))