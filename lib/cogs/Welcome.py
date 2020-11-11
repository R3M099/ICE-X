from discord.ext.commands import Cog,command
from discord.utils import get

class Welcome(Cog):
	def __init__(self,bot):
		self.bot=bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("Welcome")

	@Cog.listener()
	async def on_member_join(self,member):
		channel = get(member.guild.channels, name = "welcome")
		if channel is not None:	
			message_1 = await channel.send(f"Welcome **{member.mention}** to ***{member.guild.name}***! Please read the rules before doing anything.\nEnjoy your stay here!!")
			emoji_1 = "🥳"
			await message_1.add_reaction(emoji_1)
		else:
			pass
		
	@Cog.listener()
	async def on_member_remove(self,member):
		channel = get(member.guild.channels, name = "welcome")
		if channel is not None:
			message_2 = await channel.send(f"**{member.display_name}** has left the server :pensive:")
			emoji_2 = "😭"
			await message_2.add_reaction(emoji_2)
		else:
			pass
		
def setup(bot):
	bot.add_cog(Welcome(bot))