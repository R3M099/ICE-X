from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from glob import glob
from asyncio import sleep
from discord import Game
from discord.ext.commands import CommandNotFound,CommandOnCooldown
from ..db import db

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
		self.guild=[713107362763767929,673061595303116805]
		self.scheduler=AsyncIOScheduler()
		db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX)

	def setup(self):
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f"{cog} cog loaded.")
		print("setup complete.")

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
			await ctx.send(f'That command is in cooldown for {exc.retry_after:,.2f} seconds')
		
	async def on_ready(self):
		if not self.ready:
			while not self.cogs_ready.all_ready():
				await sleep(0.5)
			self.ready=True
			await bot.change_presence(activity=Game(f"in {len(self.guild)} servers"))
			self.scheduler.start()
			print('Bot ready.')
		else:
			print('bot reconnected.')

	async def on_message(self,message):
		if not message.author.bot:
			await self.process_commands(message)

bot=Bot()