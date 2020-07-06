from discord.ext.commands import Cog,command
from discord import Forbidden
from ..db import db

class Welcome(Cog):
	def __init__(self,bot):
		self.bot=bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("Welcome")

	@Cog.listener()
	async def on_member_join(self,member):
		db.execute("INSERT INTO exp (UserID) VALUES (?)",member.id)
		try:
			await member.send(f"Welcome to ***{member.guild.name}***! Enjoy your stay here!!")
		except Forbidden:
			pass

	@Cog.listener()
	async def on_member_remove(self,member):
		db.execute("DELETE FROM exp WHERE UserID = ?",member.id)
		await member.send(f"You have left ***{member.guild.name}***, hope to see you again!!")
		
def setup(bot):
	bot.add_cog(Welcome(bot))