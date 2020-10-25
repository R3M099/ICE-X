# ICE X

a discord bot for discord made using **Python** module named **Discord.py**

The prefix for the bot is `.`

The version of discord.py used is `1.4.1`

# COMMANDS

***Type `.help` or `.h` to get the help embed for the bot***

***Type `.help <command_name>` or `.h <command_name>` to get help for the specified command***

## Moderation commands

###### 1. Purge :

**Required Permissions**

*BOT* - manage messages

*User* - manage messages

**Usage : `.purge <no. of messages>`**

Purges/Clears/deletes the given number of messages from the channel.

###### 2. Kick :

**Required Permissions**

*BOT* - kick member

*User* - kick member

**Usage : `.kick <member(s)/member(s)_ID> [reason]`**

Kicks the specified member/members from the server. It supports multi member kick.

###### 3. Ban :

**Required Permissions**

*BOT* - ban member

*User* - ban member

**Usage : `.ban <member(s)/member(s)_ID> [reason]`**

bans the specified member/members from the server. It supports mass ban.

###### 4. Unban :

**Required Permissions**

*BOT* - ban member

*User* - ban member

**Usage : `.unban <member_ID>`**

unbans the specified member from the server.

###### 5. Mute :

**Required Permissions**

*BOT* - manage roles

*User* - manage roles

**Usage : `.mute <member/member_ID> [reason]`**

mutes the specified member/members from the server.

###### 6. Unmute :

**Required Permissions**

*BOT* - manage roles

*User* - manage roles

**Usage : `.unmute <member/member_ID>`**

unmutes the muted member/members from the server.

###### 7. Addrole :

**Aliases** - add

**Required Permissions**

*BOT* - manage roles

*User* - manage roles

**Usage : `.addrole | add <member/member_ID> <role_name>`**

adds a given role to the member.

###### 8. Removerole :

**Aliases** - remove

**Required Permissions**

*BOT* - manage roles

*User* - manage roles

**Usage : `.removerole | remove <member/member_ID> <role_name>`**

removes the given role from the member.

---------------------------------------------------------------------------------------------

## Fun commands

###### 1. Hello :

**Aliases** - Hello, hi, Hi

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.hello | hi | Hello | Hi`**

greets the user with a message.

###### 2. 8ball :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.8ball <question>`**

ask any question to the magic 8 ball.

###### 3. Ping :

**Required Permissions**

*BOT* - N/A

*user* - N/A

**Usage : `.ping`**

returns the latency of the bot.

###### 4. Say :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.say <message>`**

let the bot say what is in your mind.

###### 5. Fact :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : .fact <animal anme>**

Supported Animals -> Dog, Cat, Bird, Panda, Koala

Gives a fact of the given animal along with an image of that animal.

###### 6. Meme :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.meme`**

gives a random meme.

###### 7. Joke :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.joke`**

gives a random joke.

###### 8. Programming Joke :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.pjoke`**

gives a random programming joke.

###### 9. Chuck Norris Joke :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.cnjoke`**

gives a random Chuck Norris joke.

###### 10. XKCD :

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.xkcd`**

gives a random xkcd comic(A webcomic).

---------------------------------------------------------------------------------------------

## Utility commands

###### 1. Serverinfo :

**Aliases** - si

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.serverinfo | si`**

gives the information about the server.

###### 2. Userinfo :

**Aliases** - ui

**Required Permissions**

*BOT* - N/A

*User* - N/A

**Usage : `.userinfo | ui <member/member_ID>`**

gives the information about the specified member.
