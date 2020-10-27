from discord.ext.commands import Cog,command
from typing import Optional
from discord.utils import get
from discord import Embed
import datetime

class Help(Cog):
	def __init__(self,bot):
		self.bot=bot
		self.bot.remove_command("help")

	@command(name="help", aliases = ["h"])
	async def show_help(self, ctx, argument = None):
		"""Shows this message"""
		t=datetime.datetime.utcnow()
		
		initial_help_embed = Embed(title="Help for **{}**".format(ctx.guild.name), 
				   				   description=f"the prefix for the server is `.`.\nType `.help` or `.h` to get the help embed for the bot.", 
				   				   colour=0x0AEE0D)
		
		fields=[(f"`Modmail System`", "If you have any complaints against any members, DM the bot your complaint(make sure DMs are open).", False),
				("NOTE:", "Please Refrain yourself from wrong usage of the ModMail system as it may result in you being banned/kicked", False),
				(f"1.**__`MODERATION COMMANDS`__**: *Type `.help moderation/mod` for more info*", "The commands available to Mods/Admins of a server only", False),
				(f"2.**__`FUN COMMANDS`__**: *Type `.help fun for more info`*", "The commands available to all members for having fun", False),
				(f"3.**__`UTILITY COMMANDS`__**: *Type `.help utility/util` for more info*", "List of the utility commands available", False),
				(f"4.**__`ASTRONOMY COMMANDS`__**: *Type `.help astronomy` for more info*", "List of Astronomy commands available(currently only one)", False),
				(f"5.**__`SUPPORT COMMANDS`__**: *type `.help support` for more info*", "Shows the support commands", False)]
		
		for name,value,inline in fields:
			initial_help_embed.add_field(name=name,value=value,inline=inline)
		
		initial_help_embed.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		initial_help_embed.set_thumbnail(url=ctx.guild.icon_url)
		initial_help_embed.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		mod_help_embed = Embed(title = f"Help with *Moderation Commands*:",
							   description = "Available to Mods/admins of the server only",
							   colour = ctx.author.colour)

		fields = [(f"1. `purge`", f"Purges/Clears/deletes the given number of messages from the channel.\n**USAGE :** `.purge <no. of messages>`", False),
				  (f"2. `kick`", f"Kicks the specified member/members from the server. It supports multi member kick.\n**USAGE :** `.kick <member(s)/member(s)_ID> [reason]`", False),
				  (f"3. `ban`", f"bans the specified member/members from the server. It supports mass ban.\n**USAGE :** `.ban <member(s)/member(s)_ID> [reason]`", False),
				  (f"4. `unban`", f"unbans the specified member from the server.\n**USAGE :** `.unban <member_ID>`", False),
				  (f"5. `mute`", f"mutes the specified member/members from the server.\n**USAGE :** `.mute <member/member_ID> [reason]`", False),
				  (f"6. `unmute`", f"unmutes the muted member/members from the server.\n**USAGE :** `.unmute <member/member_ID>`", False),
				  (f"7. `addrole` | *Aliases* : `add`", f"adds a given role to the member.\n**USAGE :** `.addrole <member/member_ID> <role_name>`", False),
				  (f"8. `removerole` | *Aliases* : `remove`", f"removes the given role from the member.\n**USAGE :** `.removerole <member/member_ID> <role_name>`", False)]
		
		for name, value, inline in fields:
			mod_help_embed.add_field(name = name, value = value, inline = inline)

		mod_help_embed.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		mod_help_embed.set_thumbnail(url = ctx.guild.icon_url)
		mod_help_embed.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		fun_help_embed = Embed(title = f"Help with *Fun Commands*:",
							   description = "Available to all members of the server",
							   colour = ctx.author.colour)

		fields = [(f"1. `hello` | *Aliases* : `hi`,`Hello`,`Hi`", f"greets the user with a message.\n**USAGE :** `.hello`", False),
				  (f"2. `8ball`", f"ask any question to the magic 8 ball.\n**USAGE :** `.8ball <question>`", False),
				  (f"3. `ping`", f"returns the latency of the bot.\n**USAGE :** `.ping`", False),
				  (f"4. `say`", f"let the bot say what is in your mind.\n**USAGE :** `.say <message>`", False),
				  (f"5. `fact`", f"Gives a fact of the given animal along with an image of that animal.\n**USAGE :** `.fact <animal_name>`", False),
				  (f"6. `meme`", f"gives a random meme.\n**USAGE :** `.meme`", False),
				  (f"7. `joke`", f"gives a random joke.\n**USAGE :** `.joke`", False),
				  (f"8. `pjoke`", f"gives a random programming joke.\n**USAGE :** `.pjoke`", False),
				  (f"9. `cnjoke`", f"gives a random Chuck Norris joke.\n**USAGE :** `.cnjoke`", False),
				  (f"10. `xkcd`", f"gives a random xkcd comic(A webcomic).\n**USAGE :** `.xkcd`", False)]
		
		for name, value, inline in fields:
			fun_help_embed.add_field(name = name, value = value, inline = inline)

		fun_help_embed.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		fun_help_embed.set_thumbnail(url = ctx.guild.icon_url)
		fun_help_embed.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		utils_help_embed = Embed(title = f"Help with *Utility Commands*:",
							     description = "Available to all members of the server",
							     colour = ctx.author.colour)

		fields = [(f"1. `serverinfo` | *Aliases* : `si`", f"gives the information about the server.\n**USAGE :** `.serverinfo`", False),
				  (f"2. `userinfo` | *Aliases* : `ui`", f"gives the information about the specified member.\n**USAGE :** `.userinfo <member/member_ID>`", False),
				  (f"3. `avatar` | *Aliases* : `av`", f"gives the avatar of the member if provided or else gives the avatar of the user of the command.\n**USAGE :** `.avatar [member/member_ID]`", False)]
		
		for name, value, inline in fields:
			utils_help_embed.add_field(name = name, value = value, inline = inline)

		utils_help_embed.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		utils_help_embed.set_thumbnail(url = ctx.guild.icon_url)
		utils_help_embed.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		space_help_embed = Embed(title = f"Help with *Astronomy Commands*:",
							     description = "Available to all members of the server",
							     colour = ctx.author.colour)

		fields = [(f"1. `apod`", f"gives the Astronomy Picture Of Day(Source-**NASA**).\n**USAGE :** `.apod`", False)]
				  
		for name, value, inline in fields:
			space_help_embed.add_field(name = name, value = value, inline = inline)

		space_help_embed.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		space_help_embed.set_thumbnail(url = ctx.guild.icon_url)
		space_help_embed.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		support_help_embed = Embed(title = f"Help with *Support Commands*:",
							   	   description = "Available to all members of the server",
							   	   colour = ctx.author.colour)

		fields = [(f"1. `invite` | *Aliases* : `inv`", f"sends the invite link of the bot in embedded form.\n**USAGE :** `.invite`", False)]
				  
		for name, value, inline in fields:
			support_help_embed.add_field(name = name, value = value, inline = inline)

		support_help_embed.set_author(name = f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url = ctx.author.avatar_url)
		support_help_embed.set_thumbnail(url = ctx.guild.icon_url)
		support_help_embed.set_footer(text = f"Requested by {ctx.author.display_name} | {t.strftime('%b %d, %Y | %I:%M %p UTC')}")

		if argument is None:
			await ctx.send(embed = initial_help_embed)

		elif argument == "moderation" or argument == "mod":
			await ctx.send(embed = mod_help_embed)

		elif argument == "fun":
			await ctx.send(embed = fun_help_embed)

		elif argument == "utility" or argument == "util":
			await ctx.send(embed = utils_help_embed)

		elif argument == "astronomy":
			await ctx.send(embed = space_help_embed)

		elif argument == "support":
			await ctx.send(embed = support_help_embed)

		else:
			await ctx.send("invalid argument")
		
	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("help")

def setup(bot):
	bot.add_cog(Help(bot))