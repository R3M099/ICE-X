from discord import Embed
import datetime
from discord.ext.commands import Cog, command
from discord.utils import get

class Log(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("log")

	'''@Cog.listener()
	async def on_user_update(self, before, after):
		t = datetime.datetime.utcnow()
		if before.avatar_url != after.avatar_url:
			e = Embed(colour = 0xc720e5)
			e.set_author(name = f"{after.display_name}#{after.discriminator}", icon_url = before.avatar_url)
			e.set_thumbnail(url = after.avatar_url)
			e.add_field(name = "Avatar Update", value = after.mention, inline = False)
			e.set_footer(text = t.strftime('%d/%b/%Y | %I:%M %p UTC'))
	
			await self.bot.get_channel(736790701794132029).send(embed = e)

	@Cog.listener()
	async def on_member_update(self, before, after):
		t = datetime.datetime.utcnow()	
			
		if before.display_name != after.display_name:
			e = Embed(title = "Member Update",
					  description = "Nickname Changed",
					  colour = 0x620bd2)
			fields = [("Before:", before.display_name, False),
					  ("After:", after.display_name, False)]

			for name, value, inline in fields:
				e.add_field(name = name, value = value, inline = inline)
			e.set_thumbnail(url = after.avatar_url)
			e.set_footer(text = t.strftime('%d/%b/%Y | %I:%M %p UTC'))

			
			await self.bot.get_channel(736790701794132029).send(embed = e)

	@Cog.listener()
	async def on_message_edit(self, before, after):
		t = datetime.datetime.utcnow()
		
		if not after.author.bot:
			if before.content != after.content:
				e = Embed(description = f"Message Edited in `{after.channel}`", 
						  colour = 0xdef00e)
				fields = [("Before:", before.content, False),
					  	  ("After:", after.content, False)]

				for name, value, inline in fields:
					e.add_field(name = name, value = value, inline = inline)
				e.set_author(name = f"{after.author.display_name}#{after.author.discriminator}", icon_url = after.author.avatar_url)
				e.set_footer(text = t.strftime('%d/%b/%Y | %I:%M %p UTC'))

				
				await self.bot.get_channel(736790701794132029).send(embed = e)



	@Cog.listener()
	async def on_message_delete(self, message):
		t = datetime.datetime.utcnow()
		if not message.author.bot:
			e = Embed(description = f"Message sent by `{message.author.display_name}` Deleted in `{message.channel}`",
				  	  colour = 0xf00e11)
			fields = [("Message content", message.content, False)]

			for name, value, inline in fields:
				e.add_field(name = name, value = value, inline = inline)
			e.set_author(name = f"{message.author.display_name}#{message.author.discriminator}", icon_url = message.author.avatar_url)	
			e.set_footer(text = t.strftime('%d/%b/%Y | %I:%M %p UTC'))
			
			await self.bot.get_channel(736790701794132029).send(embed = e)'''


def setup(bot):
	bot.add_cog(Log(bot))