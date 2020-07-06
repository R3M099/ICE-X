from discord.ext.commands import Cog,command
from typing import Optional
from discord.utils import get
from discord import Embed
import datetime

def syntax(command):
	cmd=str(command)
	params=[]
	for key,value in command.params.items():
		if key not in ("self","ctx"):
			params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")
	params=" ".join(params)
	return f"```.{cmd} {params}```"

def aliases(command):
	aliases=command.aliases
	if aliases is None:
		return f"```{aliases}```"
	else:
		return None

class Help(Cog):
	def __init__(self,bot):
		self.bot=bot
		self.bot.remove_command("help")

	async def cmd_help(self,ctx,command):
		t=datetime.datetime.now()
		e=Embed(title=f'help with `{command}`',
				description=f'Use:{syntax(command)}',
				colour=ctx.author.colour)
		e.add_field(name='Aliases:',value=aliases(command),inline=False)
		e.set_footer(text='Today at '+t.strftime('%I:%M %p'))
		await ctx.send(embed=e)

	@command(name="help")
	async def show_help(self,ctx,cmd:Optional[str]):
		if not cmd:
			t=datetime.datetime.now()
			e=Embed(title="Help for **{}**".format(ctx.guild.name),
					description=f"the prefix for the server is `.`",
    				colour=0x0AEE0D)
			fields=[(f"`help`","Shows the help for the server",False),
					(f"`hello`","Says hello to the user",False),
					(f"`8ball`","Ask question to the magic 8 ball",False),
					(f"`ping`","Returns the bot latency",False),
					(f"`say`","The bot will say anything you want to say",False),
					(f"`fact`","Shows the fact about the given animal",False),
					(f"`meme`","Shows a random meme",False),
					(f"`userinfo`","Shows the information about a specified user",False),
					(f"`serverinfo`","Shows the information about the server",False),
					(f"`avatar`","Shows the avatar of a specified user",False),
					(f"`purge`","Clears the given ammount of messages",False),
					(f"`kick`","Kicks the specified user from the server",False),
					(f"`ban`","Bans the specified user from the server",False),
					(f"`unban`","Unbans the specified user from the server",False),
					(f"`mute`","Mutes a member from the server",False),
					(f"`unmute`","Unmutes a member from the server",False)]
			for name,value,inline in fields:
				e.add_field(name=name,value=value,inline=inline)
			e.set_thumbnail(url=ctx.guild.icon_url)
			e.set_footer(text='Today at '+t.strftime('%I:%M %p'))
			await ctx.send(embed=e)
		
		else:	
			if (command:=get(self.bot.commands,name=cmd)):
				await self.cmd_help(ctx,command)
			else:
				await ctx.send('That command does not exist.')

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("help")

def setup(bot):
	bot.add_cog(Help(bot))