from discord.ext.commands import Cog, command, has_permissions
from discord.ext.commands import MissingRequiredArgument, BadArgument, CheckFailure
from discord import Embed
from datetime import datetime, timedelta

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Reactions(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.polls = []
		self.giveaways = []

	@command(name = "createpoll", aliases = ["makepoll"])
	@has_permissions(manage_guild = True)
	async def create_poll(self, ctx, time: int, question: str, *options):
		t = datetime.utcnow()

		if len(options) > 10:
			await ctx.send("Too many options provied(max. limit is 10)")

		else:
			e = Embed(title = f"Poll created by **`{ctx.author.display_name}`**",
					  description = f"TOPIC: **{question}**",
					  colour = ctx.author.colour)
			fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False),
					  ("Time", f"{time} hours", False),
					  ("Instructions", "React to give your vote", False)]

			for name, value, inline in fields:
				e.add_field(name = name, value = value, inline = inline)

			e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))

			message = await ctx.send(embed = e)

			for emoji in numbers[:len(options)]:
				await message.add_reaction(emoji)

			self.polls.append((message.channel.id, message.id))

			self.bot.scheduler.add_job(self.complete_poll, "date", run_date = datetime.now() + timedelta(hours = time), args=[message.channel.id, message.id])

	async def complete_poll(self, channel_id, message_id):
		message = await self.bot.get_channel(channel_id).fetch_message(message_id)

		most_voted = max(message.reactions, key=lambda r: r.count)

		await message.channel.send(f"The results are in and option {most_voted.emoji} was the most popular with {most_voted.count-1:,} votes!")
		
		self.polls.remove((message.channel.id, message.id))

	@create_poll.error
	async def create_poll_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("one or more arguments are missing")

		if isinstance(exc, BadArgument):
			await ctx.send("Time must be integer and question must be a string inside double quotes")

		if isinstance(exc, CheckFailure):
			await ctx.send("Missing required permissions to execute that command")

	@Cog.listener()
	async def on_raw_reaction_add(self, payload):

		if payload.message_id in (poll[1] for poll in self.polls):
	
			message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

			for reaction in message.reactions:
				if not payload.member.bot and payload.member in await reaction.users().flatten() and reaction.emoji != payload.emoji.name:
					await message.remove_reaction(reaction.emoji, payload.member)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("reactions")

def setup(bot):
	bot.add_cog(Reactions(bot))