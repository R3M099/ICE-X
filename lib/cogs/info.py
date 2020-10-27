from discord.ext.commands import Cog
from discord.ext.commands import command, MissingRequiredArgument
from discord import Embed,Member
from typing import Optional
import datetime

class Info(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name="userinfo",aliases=["ui"])
	async def user_info(self,ctx,member:Member):
		"""Shows the information about the user"""
		t=datetime.datetime.utcnow()
		roles = []
		for role in member.roles:
			roles.append(role)
		member=member or ctx.author
		e=Embed(title="{}'s info".format(member.name),
				description="Here's some info about the user.",
				colour=member.colour)
		fields=[("Name",member.name,True),
				("ID",member.id,True),
				("Status",member.status,True),
				("Is Bot",'Yes' if member.bot else 'No',True),
				(f"Roles ({len(member.roles)})",', '.join(role.mention for role in roles),True),
				("Created at",member.created_at.strftime('%d/%m/%Y %H:%M:%S UTC'),True),
				("Joined at",member.joined_at.strftime('%d/%m/%Y %H:%M:%S UTC'),True)]
		for name,value,inline in fields:
			e.add_field(name=name,value=value,inline=inline)
		e.set_thumbnail(url=member.avatar_url)
		e.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")
		await ctx.send(embed=e)

	@user_info.error
	async def user_info_error(self, ctx, exc):
		if isinstance(exc, MissingRequiredArgument):
			await ctx.send("Provide a member or User ID to show information about")
	
	@command(name="serverinfo", aliases=["si"])
	async def server_info(self,ctx):
		"""Shows the information about the Server"""
		t=datetime.datetime.utcnow()
		e=Embed(title=f"**{ctx.guild.name}** info",
				description="Here's some info about the Server.",
				colour=ctx.guild.owner.colour)
		fields=[("Server Name",ctx.guild.name,True),
				("Owner Name",ctx.guild.owner.display_name,True),
				("Server ID",ctx.guild.id,True),
				("Server Region",ctx.guild.region,True),
				("Roles",len(ctx.guild.roles),True),
				("Channel Categories",len(ctx.guild.categories),True),
				("Text Channels",len(ctx.guild.text_channels),True),
				("Voice Channels",len(ctx.guild.voice_channels),True),
				("Members",len(ctx.guild.members),True),
				("Humans", sum(not member.bot for member in ctx.guild.members),True),
				("Bots", sum(member.bot for member in ctx.guild.members),True),
				("Boost level", ctx.guild.premium_tier,True),
				("number of boosts", ctx.guild.premium_subscription_count,True),
				("Created on",ctx.guild.created_at.strftime('%d/%m/%Y %H:%M:%S UTC'),True)]
		for name,value,inline in fields:
			e.add_field(name=name,value=value,inline=inline)
		e.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		e.set_thumbnail(url=ctx.guild.icon_url)
		e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
		await ctx.send(embed=e)

	@command(name="avatar",aliases=["av"])
	async def member_avatar(self,ctx,member:Optional[Member]):
		"""Shows the avatar of the user"""
		t=datetime.datetime.now()
		member=member or ctx.author
		e=Embed(title=f"{member.name}#{member.discriminator}",
				description="Avatar",
				colour=member.colour)
		e.set_image(url=member.avatar_url)
		e.set_footer(text = t.strftime('%b %d, %Y | %I:%M %p UTC'))
		await ctx.send(embed=e)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("info")

def setup(bot):
	bot.add_cog(Info(bot))