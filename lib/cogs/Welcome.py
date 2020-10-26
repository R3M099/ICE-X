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
			await member.send("Please read the rules and follow them in order to avoid consequences :pray:")
			await member.send(f"We got a modmail system so if you have any complaint against any member from the server, DM the bot(20-500 characters) your complaint.\n**Please Refrain yourself from wrong usage of the system as it may get you kicked/banned from the server** ")
			await self.bot.get_channel(736790701794132029).send(f"Welcome **{member.mention}** to ***{member.guild.name}***! Enjoy your stay here!!")
		except Forbidden:
			await self.bot.get_channel(736790701794132029).send(f"Welcome **{member.mention}** to ***{member.guild.name}***! Enjoy your stay here!!")

	@Cog.listener()
	async def on_member_remove(self,member):
		try:
			await member.send(f"You have left ***{member.guild.name}***, hope to see you again!!")
		except Forbidden:
			await self.bot.get_channel(736790701794132029).send(f"**{member.display_name}** has left the server :pensive:")
		
def setup(bot):
	bot.add_cog(Welcome(bot))