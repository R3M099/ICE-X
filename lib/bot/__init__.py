from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from glob import glob
from asyncio import sleep
from discord import Activity, DMChannel, Embed
import discord
import datetime
import re
#from lib.cogs.afk import afk_list
from discord.ext.commands import CommandNotFound,CommandOnCooldown

PREFIX='.'

COGS=[path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
	def __init__(self):
		for cog in COGS:
			setattr(self,cog,False)

	def ready_up(self,cog):
		setattr(self,cog,True)
		print(f"{cog} is ready")

	def all_ready(self):
		return all([getattr(self,cog) for cog in COGS])

class Bot(BotBase):
	def __init__(self):
		self.PREFIX=PREFIX
		self.ready=False
		self.cogs_ready=Ready()
		self.guild=[713107362763767929,673061595303116805,541169120943669248]
		self.scheduler=AsyncIOScheduler()
		super().__init__(command_prefix=PREFIX)

	def setup(self):
		COGS = ["help", "fun", "info", "mod", "Welcome", "log", "invite", "afk", "roles", "astronomy", "xkcd"]
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f"{cog} loaded.")

		print("setup complete")

	def run(self,version):
		self.VERSION=version
		print("Running setup.")
		self.setup()
		with open("./lib/bot/token.0","r",encoding="utf-8") as tf:
			self.TOKEN=tf.read()
		print('Running bot.')
		super().run(self.TOKEN,reconnect=True)

	async def on_connect(self):
		print('Bot connected.')

	async def on_disconnect(self):
		print('Bot disconnected.')

	async def on_command_error(self,ctx,exc):
		if isinstance(exc,CommandNotFound):
			await ctx.send('Command not found.')
		elif isinstance(exc,CommandOnCooldown):
			await ctx.send(f'That command is in cooldown for {exc.retry_after:,.0f} seconds')
		
	async def on_ready(self):
		if not self.ready:
			#while not self.cogs_ready.all_ready():
			#	await sleep(0.5)
			self.ready = True
			await bot.change_presence(status = discord.Status.online, activity = Activity(type = discord.ActivityType.listening, name = "the screams of souls from Hell"))
			#self.scheduler.start()
			print('Bot ready.')
		else:
			print('bot reconnected.')

	async def on_message(self,message):
		t = datetime.datetime.now()
		x = re.findall("^ice\s*x$", message.content)
		y = re.findall("^ICE\s*X$", message.content)
		#mention = message.mentions

		'''for user in mention:
			if user.id in afk_list:
				await message.channel.send(f"**{user.display_name}** is AFK, don't mention him/her")'''

		if x:
			await message.channel.send(f"Hello, World!, I have been created by almighty **℟ʓϺ𝞱#0522**")

		elif y:
			await message.channel.send(f"Hello, World!, I have been created by almighty **℟ʓϺ𝞱#0522**")

		'''for user in mentions:
			if user.id == 537634097137188875:
				await message.channel.send(f"**DO NOT MENTION HIM WITHOUT ANY REASON** :face_with_symbols_over_mouth:")'''

		if bot.user in message.mentions:
			await message.channel.send(f"Hello **{message.author.display_name}**\nPlease type `.help` or `.h` for more info.\nTo get help about commands, type `.help <command name>` or `.h <command name>`.")

		if not message.author.bot:
			if isinstance(message.channel, DMChannel):
				if len(message.content) < 20 or len(message.content) > 500:
					await message.channel.send("Your message should be atleast 20 characters long and no more then 500 characters long.")
				else:
					t = datetime.datetime.utcnow()
					e = Embed(description = f"Complaint from `{message.author.display_name}`",
							  colour = 0x000203)
					e.set_thumbnail(url = message.author.avatar_url)
					e.set_author(name = f"{message.author.display_name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
					fields = [("Member", message.author.display_name, False),
							  ("Message", message.content, False)]
					for name, value, inline in fields:
						e.add_field(name = name, value = value, inline = inline)

					e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
					mod = self.get_cog("mod")
					await self.get_channel(736790701794132029).send(embed = e)
					await message.channel.send("Your message has been relayed to the Moderators/Admins, Thanks for using the modmail :slight_smile:")
		
			
			await self.process_commands(message)

bot=Bot()