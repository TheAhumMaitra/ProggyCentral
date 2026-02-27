import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We are ready to go in, {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "testProggy" in message.content:
        await message.channel.send("The bot is running successfully!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! I'm Proggy Central. Just a bot.")

@bot.command()
async def info_roles(ctx):
    roles_info = '''
__**Staff roles Info (ranked)**__

<@&1467998946382319677> - ***Onwer of the server***

<@&1455478920903262343>  - ***Bots of this server***

<@&1455470726172901449> - ***Main manager of the server***

<@&1466030548454740003> - ***Server manager and most powerful staff***

<@&1455471195695743047> - ***Senior moderator***

<@&1459247321463259294> - ***Junior moderator***

__**Bots roles Info (ranked) : **__

**Note** : This list is also a tier list xD 

__**Server main bots: **__

<@&1475085493887566089> - Proggy's custom bot used for multiple purposes
<@&1473605839796437025> - Main bot of this server 
<@&1455582247695679637> - Senior bot of this server used for automod  (spam, bad words) , logging, other things.
<@&1455472462140805257> - Used for leveling. Back in old days, it was used for moderation.
<@&1473260219420381289> - Used for embedded messages, etc.
<@155149108183695360> - Used mostly for utilities.
<@&1476861100678058107> - Main utilities and fun activities bot

__**Member Roles : **__
<@&1473632734512680960> - All members who verified themself and can access this server
<@&1474514664288157917> - Members who are not verified, also this is a special Wick bot's role. Wick bot can use for automod, etc.


__**Backup bots : **__

<@&1474360955600244801> - Used for embedded messages 
<@282859044593598464> -  Used for utilities.
<@&1474150218575646835> - Used for moderation

__**Fun bots roles (not ranked list) : **__

<@&1474383694692221145> - Main bot used for playing games
<@&1474761894970790060> - Used for sharing memes
<@664508672713424926> - A specified bot used for playing Pokemon 
<@&1466738717178728671> - A specified bot used for playing Uno
<@&1457308571527024694> - A bot for getting Reddit stories 
<@&1466737192465469516> - A fun bot used for counting
    '''
    embed = discord.Embed(title="Roles Info", description=f"{roles_info}")
    await ctx.send(embed=embed, allowed_mentions=discord.AllowedMentions.none())

def start_bot():
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)

if __name__ == "__main__":
    start_bot()