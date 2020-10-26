from discord.ext.commands import Cog, command, bot_has_permissions, has_permissions
from discord.ext.commands import MissingRequiredArgument, CheckFailure
from discord import Member, Role
from discord.utils import get
import datetime

class Roles(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(name = "addrole", aliases = ["add"])
	@bot_has_permissions(manage_roles = True)
	@has_permissions(manage_roles = True)
	async def add_role(self, ctx, member: Member, *, role = None):
		'''Adds a given role to a member'''
		get_role = get(ctx.guild.roles, name = role)
		
		if not get_role:
			NewRole = await ctx.guild.create_role(name = role)
			await member.add_roles(NewRole)
			await ctx.send(f"**{member.display_name}** has `{NewRole.name}` added")

		else:
			await member.add_roles(get_role)
			await ctx.send(f"**{member.display_name}** has `{get_role.name}` added")
		
	@add_role.error
	async def  add_role_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("One or more required arguments are missing")
			await ctx.send(f"use `.addrole|add <member> <role>`")

		if isinstance(exc, CheckFailure):
			await ctx.send("Missing required permission to execute that command")

	@command(name = "removerole", aliases = ["remove"])
	@bot_has_permissions(manage_roles = True)
	@has_permissions(manage_roles = True)
	async def remove_role(self, ctx, member: Member, *, role = None):
		'''removes the given role from the member '''
		get_role = get(ctx.guild.roles, name = role)
		
		if not get_role:
			await ctx.send("Either that role does not exist or the member does not have that role")

		else:
			await member.remove_roles(get_role)
			await ctx.send(f"**{member.display_name}** has `{get_role.name}` removed")

	@remove_role.error
	async def remove_role_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("One or more required arguments are missing")
			await ctx.send(f"use `.removerole|remove <member> <role>`")

		if isinstance(exc, CheckFailure):
			await ctx.send("Missing required permission to execute that command")

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("roles")

def setup(bot):
	bot.add_cog(Roles(bot))