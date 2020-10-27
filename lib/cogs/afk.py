from discord.ext.commands import Cog, command, bot_has_permissions
from discord.ext.commands import MissingRequiredArgument, BadArgument
from discord.utils import get
import asyncio

afk_list = []

class AFK(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name = "afk")
	@bot_has_permissions(manage_roles = True)
	async def afk(self, ctx, mins:int):
		"""sets the user to AFK for the given ammount of time"""
		current_nick = ctx.author.nick
		role = get(ctx.guild.roles, name = "afk")
		if mins <= 1440 and mins > 0:
			if not role:
				NewRole = await ctx.guild.create_role(name = "afk")
				await ctx.author.add_roles(NewRole)
				await ctx.send(f"{ctx.author.mention} has gone AFK for {mins} mins")
				await ctx.author.edit(nick = f"</AFK>{ctx.author.name}")

				afk_list.append(ctx.message.author.id)
				#await ctx.send(afk_list)

				c = 0
				while c <= mins:
					c += 1
					await asyncio.sleep(60)

					if c == int(mins):
						await ctx.author.edit(nick = current_nick)
						await ctx.author.remove_roles(NewRole)
						await ctx.send(f"{ctx.author.mention} is no longer AFK")
						afk_list.remove(ctx.message.author.id)
						break

			else:
				await ctx.author.add_roles(role)
				await ctx.send(f"{ctx.author.mention} has gone AFK for {mins} mins")
				await ctx.author.edit(nick = f"</AFK>{ctx.author.name}")

				afk_list.append(ctx.message.author.id)

				c = 0
				while c <= mins:
					c += 1
					await asyncio.sleep(60)

					if c == int(mins):
						await ctx.author.edit(nick = current_nick)
						await ctx.author.remove_roles(role)
						await ctx.send(f"{ctx.author.mention} is no longer AFK")
						afk_list.remove(ctx.message.author.id)
						break

		else:
			await ctx.send("time should be max 1 day and above 0")

	@afk.error
	async def afk_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("How much time(mins) you want to be AFK")
		if isinstance(exc, BadArgument):
			await ctx.send("Given time is not an Integer")

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("afk")

def setup(bot):
	bot.add_cog(AFK(bot))