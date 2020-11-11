from discord.ext.commands import Cog, Greedy
from discord.ext.commands import command,cooldown,BucketType
from discord.ext.commands import MissingRequiredArgument, CheckFailure
from discord.ext.commands import bot_has_permissions, has_permissions
from discord.utils import get
from discord import Member,Embed,PermissionOverwrite
from typing import Optional
import datetime

class Mod(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name="purge")
	@cooldown(1,5,BucketType.user)
	@bot_has_permissions(manage_messages=True)
	async def clear_messages(self,ctx,limit:int):
		if 0<limit<=100:
			if ctx.author.guild_permissions.manage_messages:
				await ctx.message.delete()
				await ctx.channel.purge(limit=limit)
				await ctx.send(f"{limit} messages deleted.", delete_after = 1)

			else:
				await ctx.send("You do not have required permission to execute that command")

		else:
			await ctx.send("The number of messages provided is out of bounds.")

	@clear_messages.error
	async def clear_messages_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send("Provide the number of messages to delete.")

	@command(name="kick")
	@cooldown(1,5,BucketType.user)
	@bot_has_permissions(kick_members=True)
	@has_permissions(kick_members = True)
	async def kick_member(self, ctx, targets:Greedy[Member], *, reason:Optional[str] = "No reason provided."):
		"""Kicks a member from the server(supports multi user kick)"""
		t=datetime.datetime.utcnow()

		if not len(targets):
			await ctx.send("One or more required arguments are missing")

		else:
			for target in targets:
				if (ctx.author.top_role.position > target.top_role.position and not target.guild_permissions.administrator):
					
					channel = get(target.guild.channels, name = "moderation-logs")
					
					await target.kick(reason = reason)

					e=Embed(title="Kicked Member",
							description=f"{target.mention} has been kicked successfully",
							colour=0xDF8F0D)
					e.add_field(name="Reason:",value=reason,inline=False)
					e.add_field(name="Responsible Mod:",value=ctx.author.mention,inline=False)
					e.set_thumbnail(url=target.avatar_url)
					e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))

					await ctx.send(f"**{target.display_name}** has been kicked successfully by **{ctx.author.display_name}** for reason: {reason}.")
					if channel is not None:
						await channel.send(embed = e)
						break

				elif target.guild_permissions.administrator:
					await ctx.send("Can't kick an Administrator")

				elif ctx.author.top_role.position < target.top_role.position:
					await ctx.send("You can't kick a member higher then you")

				elif ctx.author == target:
					await ctx.send("You can't kick yourself")

				else:
					await ctx.send(f"{target.display_name} could not be kicked")
			
	@kick_member.error
	async def kick_member_error(self,ctx,exc):
		if isinstance(exc, CheckFailure):
			await ctx.send("Missing required permission to execute that command.")
		
	@command(name="ban")
	@cooldown(1,5,BucketType.user)
	@bot_has_permissions(ban_members=True)
	@has_permissions(ban_members = True)
	async def ban_member(self,ctx,targets:Greedy[Member],*,reason:Optional[str]="No reason provided."):
		"""Bans a member from the Server(supports mass ban)"""
		t=datetime.datetime.utcnow()

		if not len(targets):
			await ctx.send("One or more required arguments are missing")

		else:
			for target in targets:
				if (ctx.author.top_role.position > target.top_role.position and not target.guild_permissions.administrator):
					
					channel = get(target.guild.channels, name = "moderation-logs")

					await target.ban(reason = reason)

					e=Embed(title="Banned Member",
							description=f"{target.mention} has been banned successfully",
							colour=0xDF8F0D)
					e.add_field(name="Reason:",value=reason,inline=False)
					e.add_field(name="Responsible Mod:",value=ctx.author.mention,inline=False)
					e.set_thumbnail(url=target.avatar_url)
					e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))

					await ctx.send(f"**{target.display_name}** has been banned successfully by **{ctx.author.display_name}** for reason: {reason}.")
					if channel is not None:
						await channel.send(embed = e)
						break

				elif target.guild_permissions.administrator:
					await ctx.send("Can't ban an Administrator")

				elif ctx.author.top_role.position < target.top_role.position:
					await ctx.send("You can't ban a member higher then you")

				elif ctx.author == target:
					await ctx.send("You can't ban yourself")

				else:
					await ctx.send(f"{target.display_name} could not be banned")
	@ban_member.error
	async def ban_member_error(self,ctx,exc):
		if isinstance(exc,CheckFailure):
			await ctx.send("Missing required permission to execute the command")

	@command(name="unban")
	@cooldown(1,5,BucketType.user)
	@bot_has_permissions(ban_members=True)
	async def unban_member(self,ctx,UserID:int=""):
		"""Unbans a member from previously banned member"""
		t=datetime.datetime.utcnow()
		if ctx.author.guild_permissions.ban_members:
			bans=await ctx.guild.bans()
			for ban in bans:
				if ban.user.id==UserID:
					e=Embed(title="Unbanned Member",
							description=f"{ban.user.mention} has been unbanned successfully",
							colour=0x2ED018)
					e.add_field(name="Responsible Mod:",value=ctx.author.mention,inline=False)
					e.set_thumbnail(url=ban.user.avatar_url)
					e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
					await ctx.message.delete()
					await ctx.guild.unban(ban.user)
					await ctx.send(f"{ban.user.mention} has been unbanned successfully by **{ctx.author.display_name}**.")
					#await self.bot.get_channel(736790701794132029).send(embed = e)
				else:
					await ctx.send("User not found in banned list.")

	@unban_member.error
	async def unban_member_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send("Provide a User ID to unban.")

	@command(name="mute")
	@cooldown(1,5,BucketType.user)
	@bot_has_permissions(manage_roles=True)
	async def mute_member(self,ctx,member:Member,*,reason:Optional[str]="No reason provided."):
		"""Mutes a member from the server"""
		t=datetime.datetime.utcnow()

		if ctx.author.guild_permissions.manage_roles:

			channel = get(member.guild.channels, name = "moderation-logs")

			e=Embed(title='Muted Member',
					description=f'{member.mention} has been muted successfully.',
					colour=0x17D8CF)
			e.add_field(name='Reason',value=reason,inline=False)
			e.add_field(name='Responsible Mod',value=ctx.author.mention,inline=False)
			e.set_thumbnail(url=member.avatar_url)
			e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
			role=get(ctx.guild.roles,name="Muted")
			if ctx.author.top_role.position<member.top_role.position:
				await ctx.send('you cannot mute a member higher then you.')
			elif ctx.author==member:
				await ctx.send('you cannot mute yourself.')
			elif not role:
				NewRole=await ctx.guild.create_role(name="Muted")
				overwrite=PermissionOverwrite()
				overwrite.send_messages=False
				for channel in ctx.guild.text_channels:
					await channel.set_permissions(NewRole,overwrite=overwrite)
				await member.add_roles(NewRole)
				await ctx.send(f"**{member.display_name}** has been muted successfully by **{ctx.author.display_name}** for reason: {reason}.")

				if channel is not None:
					await channel.send(embed = e)
					
				return
			else:
				overwrite=PermissionOverwrite()
				overwrite.send_messages=False
				for channel in ctx.guild.text_channels:
					await channel.set_permissions(role,overwrite=overwrite)
				await member.add_roles(role)
				await ctx.send(f"**{member.display_name}** has been muted successfully by **{ctx.author.display_name}** for reason:{reason}.")
				if channel is not None:
					await channel.send(embed = e)
					
				return
			return

		else:
			await ctx.send("You do not have the required permissions")

	@mute_member.error
	async def mute_member_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send("Provide a member to mute.")

	@command(name="unmute")
	@cooldown(1,5,BucketType.user)
	@bot_has_permissions(manage_roles=True)
	async def unmute_member(self,ctx,member:Member):
		"""Unmutes a member from the server"""
		t=datetime.datetime.utcnow()
		if ctx.author.guild_permissions.manage_roles:
			channel = get(member.guild.channels, name = "moderation-logs")
			e=Embed(title='Unmuted Member',
					description=f'{member.mention} has been unmuted successfully.',
					colour=0x1046CB)
			e.add_field(name='Responsible Mod',value=ctx.author.mention,inline=False)
			e.set_thumbnail(url=member.avatar_url)
			e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
			role=get(ctx.guild.roles,name="Muted")
			if ctx.author==member:
				await ctx.send("You are not Muted.")
			elif not role:
				pass
			else:
				await member.remove_roles(role)
				await ctx.send(f"**{member.display_name}** has been unmuted successfully by **{ctx.author.display_name}**.")
				if channel is not None:
					await channel.send(embed = e)

		else:
			await ctx.send(f'You do not have the required permission.')

	@unmute_member.error
	async def unmute_member_error(self,ctx,exc):
		if isinstance(exc,MissingRequiredArgument):
			await ctx.send("Provide a member to unmute.")

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("mod")

def setup(bot):
	bot.add_cog(Mod(bot))