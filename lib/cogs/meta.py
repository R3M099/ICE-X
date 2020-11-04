from datetime import datetime, timedelta
from platform import python_version
from time import time
from discord import __version__ as discord_version
from discord.ext.commands import Cog, command
from discord import Embed, AppInfo
from psutil import Process, virtual_memory

class Meta(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(name = "botinfo")
	async def show_bot_info(self, ctx):
		t = datetime.utcnow()

		proc = Process()
		with proc.oneshot():
			uptime = timedelta(seconds=time()-proc.create_time())
			cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
			mem_total = virtual_memory().total / (1024**2)
			mem_of_total = proc.memory_percent()
			mem_usage = mem_total * (mem_of_total / 100)
		
		e = Embed(title = f"Information about `ICE X`",
				  colour = ctx.author.colour)

		fields = [("Bot version", self.bot.VERSION, True),
				  ("Bot Owner", f"<@!537634097137188875>", True),				  
				  ("Python version", python_version(), True),
				  ("discord.py version", discord_version, True),
				  ("Uptime", uptime, True),
				  ("CPU time", cpu_time, True),
				  ("Memory usage", f"{mem_usage:,.3f} / {mem_total:,.0f} MiB ({mem_of_total:.0f}%)", True),
				  ("Invite Bot", '**[Invite](https://discord.com/api/oauth2/authorize?client_id=723380957343907911&permissions=8&scope=bot "Invite the bot to your server")**', False)]

		for name, value, inline in fields:
			e.add_field(name=name, value=value, inline=inline)

		e.set_thumbnail(url = self.bot.user.avatar_url)
		e.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		await ctx.send(embed=e)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("meta")


def setup(bot):
	bot.add_cog(Meta(bot))