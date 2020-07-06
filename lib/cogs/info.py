from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed,Member
from typing import Optional
import datetime

class Info(Cog):
	def __init__(self,bot):
		self.bot=bot

	@command(name="userinfo",aliases=["ui"])
	async def user_info(self,ctx,member:Optional[Member]):
		t=datetime.datetime.now()
		member=member or ctx.author
		e=Embed(title="{}'s info".format(member.name),
				description="Here's some info about the user.",
				colour=member.colour)
		fields=[("Name",member.name,True),
				("ID",member.id,True),
				("Status",member.status,True),
				("Is Bot",'Yes' if member.bot else 'No',True),
				("Highest Role",member.top_role.mention,True),
				("Number of Roles",len(member.roles),True),
				("Created at",member.created_at.strftime('%d/%m/%Y %H:%M:%S %p UTC'),True),
				("Joined at",member.joined_at.strftime('%d/%m/%Y %H:%M:%S %p UTC'),True)]
		for name,value,inline in fields:
			e.add_field(name=name,value=value,inline=inline)
		e.set_thumbnail(url=member.avatar_url)
		e.set_footer(text='Today at ' + t.strftime('%I:%M %p'))
		await ctx.send(embed=e)
	
	@command(name="serverinfo")
	async def server_info(self,ctx):
		t=datetime.datetime.now()
		e=Embed(title=f"{ctx.guild.name} info",
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
				("Created on",ctx.guild.created_at.strftime('%d/%m/%Y %H:%M:%S %p UTC'),True)]
		for name,value,inline in fields:
			e.add_field(name=name,value=value,inline=inline)
		e.set_thumbnail(url=ctx.guild.icon_url)
		e.set_footer(text='Today at ' + t.strftime('%I:%M %p'))
		await ctx.send(embed=e)

	@command(name="avatar",aliases=["av"])
	async def member_avatar(self,ctx,member:Optional[Member]):
		t=datetime.datetime.now()
		member=member or ctx.author
		e=Embed(title=f"{member.name}#{member.discriminator}",
				description="Avatar",
				colour=member.colour)
		e.set_image(url=member.avatar_url)
		e.set_footer(text='Today at ' + t.strftime('%I:%M %p'))
		await ctx.send(embed=e)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("info")

def setup(bot):
	bot.add_cog(Info(bot))