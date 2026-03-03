# SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com
#
# SPDX-License-Identifier: 	GPL-3.0-or-later
from random import choice
import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN") #get the main Discord bot connect token

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()

# the intents we should access
intents.message_content = True
intents.members = True

#prefix for running any command
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'We are ready to go in, {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands : \n\n {e}")

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
async def credit(ctx):
    await ctx.send(
        f"{ctx.author.mention}I'm created by Ahum Maitra. Repository url - https://github.com/TheAhumMaitra/ProggyCentral **Note : This project is licensed under the terms of GNU public license version 3")


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
<@&1476861100678058107> - Main utilities and fun activities, multipurpose bot (Chairman said once 'It's the most closet Bleed alternative bot')
<@&1455582247695679637> - Senior bot of this server used for automod  (spam, bad words) , logging, other things.
<@&1478070268118306940> - Used for leveling.
<@&1473260219420381289> - Used for embedded messages, etc.
<@155149108183695360> - Used mostly for utilities.
<@&1476861100678058107> - Main utilities and fun activities bot

__**Member Roles : **__
<@&1473632734512680960> - All members who verified themself and can access this server
<@&1474514664288157917> - Members who are not verified, also this is a special Wick bot's role. Wick bot can use for automod, etc.


__**Additional bots roles: **__

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
    embed = discord.Embed(title="Roles Info", description=f"{roles_info}", color=discord.Color.random())
    await ctx.send(embed=embed, allowed_mentions=discord.AllowedMentions.none())

@bot.command()
async def notice(ctx):
    await ctx.send(f"{ctx.author.mention}Proggy Central is rendering on Render.com's free plan. Render.com doesn't allow to run the server for 24 x 7 xD. So, to use the bot. Please visit https://proggycentral.onrender.com/ . Thanks for your understanding :) . ")

@bot.command(name="avatar", description="Get the avatar of a user xD")
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(title=f"{member.name}'s avatar", color=member.color)
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, message: str):
    await ctx.send(message)

@bot.command()
async def jwquote(ctx):
    quotes = ["Your membership to The Continental has been, by thine own hand, revoked.", "A man's ambition should never exceed his worth. You would do well to remember that, sir.", "A man has to look his best when it's time to get married. Or buried.", "You stabbed the devil in the back and forced him back into the life that he had just left.", "I can assure you that the stories you hear about this man, if nothing else, have been watered down.", "How you do anything is how you do everything.", "...Yeah", "Friendship means little when it’s convenient.", "Those who cling to death, live. Those who cling to life, die.", "Fools talk. Cowards are silent. But wise men listen.", "Exactly. Rules. Without them, we'd live with the animals.", "John Wick is a man of focus, commitment, sheer will... something you know very little about.", "Tell them all... Whoever comes, whoever it is... I'll k**l them. I'll k**l them all.", "People keep asking me if I'm back, and I haven't really had an answer. But now, yeah, I'm thinking I'm back!", ""]
    await  ctx.send(f"{ctx.author.mention}\n**{choice(quotes)}**")

@bot.command()
async def send_rules(ctx):
    rules = '''
    **Please follow all the rules listed below while participating in this server.**

**1. ** Most text channels are English only
Mods must be able to read all messages clearly.

**2. ** All members must communicate respectfully. Harassment, bullying, hate speech, or discrimination of any kind—including racism, sexism, xenophobia, homophobia, transphobia, or misogyny—will not be tolerated.

**3. ** Keep all discussion civil and in the correct channels
Mods may asks you to move your conversation to the correct channel.

**4. ** No inappropriate language
Remain respectful of others at all times.

**5. ** Keep personal drama out of chat

**6. ** No impersonation
Do not impersonate other users, moderators, and/or famous personalities.

**7. ** No spamming
Do not flood chat rooms with messages. Encouraging others to spam is also not allowed.

**8. ** No NSFW content
Do not post or have conversations around NSFW content.

**9. ** No inappropriate or offensive usernames, status's or profile pictures
You may be asked to change these if they violate our rules.

**10.** No politics
Talking about serious issues involving government officials, political parties, religions, or geo-political disagreements is not allowed. Even if these topics are approached in a civil manner, this is not the correct space for these conversations.

**11.** No self-promotion, soliciting, or advertising
This also includes user DMs.

**12.** No malicious links
Any link that track IP addresses, or lead to malicious websites that contain malware will be removed.

**13.** Don't evade filters
This applies to both words and links. If something is censored, it is censored for a reason!

**14.** Follow the Discord ToS and Community Guidelines
Terms of Service: https://discordapp.com/terms
Community Guidelines: https://discord.com/guidelines

**15.** *Moderators and Upper rankers hold final say
Listen to and respect the volunteers that keep this server running.

**16.** Any type of Ping abuse, such as @everyone or @here will result to ban.

**17.** Don't argue, just apologise

**18.** Be kind always

**19.** Please don't use profanity, vulgar words, inappropriate language/ words.

**20.** Do not copy and paste answers from ChatGPT or similar AI tools.

**21.** Don't engage into toxic people's drama.

**Here are some great words told by Robert Greene:**

 "some people are toxic they have deep levels of insecurity and issues stemming from a troubled damaged childhood usually and they have patterns that are pretty negative and destructive they have a need to sabotage other people or to sabotage themselves and getting involved with someone like that can really ruin your life you get sucked into their dramas they kind of control the dynamic they feed off of controlling you by all of the emotions that they can stir up" 

**React once you have understood with this emoji - ✅**
    '''
    consequences=discord.Embed(title="Please remember", color=discord.Color.random())
    consequences.set_image(url="https://imageio.forbes.com/blogs-images/scottmendelson/files/2019/03/FIN02_JW3_1Sht_Payoff_VF1-1200x675.jpg?format=jpg&height=600&width=1200&fit=bounds")
    rules_image=discord.Embed(color=discord.Color.random())
    rules_embed = discord.Embed(description=f"{rules}", color=discord.Color.random())
    rules_image.set_image(url="https://media.tenor.com/DEPkXx3uo_oAAAAe/rules-discord-rules.png")
    notice = discord.Embed(description="__**Note : **__  *In certain situations we can change/edit/add rule(s)*", color=discord.Color.random())

    await ctx.send(embeds=[rules_image,rules_embed,notice,consequences], allowed_mentions=discord.AllowedMentions.none())

@bot.tree.command(name="help", description="Get all information about Proggy Central and list all commands")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} \n **Here is the list of all commands :** \n\n __**Prefix commands**__ \n `!info_roles` - This command will send all information about all roles \n `!avatar [`member_name`] ` - Get the avatar of a user \n\n __**Slash commands : **__ \n `/help` - Shows this help page", ephemeral=True)

def start_bot():
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)


if __name__ == "__main__":
    start_bot()
