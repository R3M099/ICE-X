from discord import Embed
import datetime
from discord.ext.commands import Cog, command

class Invite(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(name = "invite", aliases = ["inv"])
	async def invite_bot(self, ctx):
		"""Send the invite link for the bot"""
		t = datetime.datetime.utcnow()
		e = Embed(description = f"{ctx.author.mention}, here's an invite link for the bot :slight_smile:",
				  colour = 0x0cb44e)
		e.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		e.add_field(name = "Invite Link", value = '**[Invite Me](https://discord.com/api/oauth2/authorize?client_id=723380957343907911&permissions=8&scope=bot "Invite the bot to your server")**')
		e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))

		await ctx.send(embed = e)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("invite")

def setup(bot):
	bot.add_cog(Invite(bot))