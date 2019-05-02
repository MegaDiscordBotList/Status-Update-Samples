import discord
from discord.ext import commands
from discord.ext.commands import Bot
import logging
ownerid = [''] # Your Discord id
admins = ['', ''] # Put peoples ids in here that you want to be adble to use the update command
logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix='!') # Sets the client and sets the prefix

@bot.event
async def on_ready():
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    # MDBL Status Update
    print("-----------MDBL-----------\n
          "Admins: {} | API: v6.6")
    print("\nSending update command...")
    try:
        channel = bot.get_channel("567208400891543552")
    except:
        print("[MDBL] Unable to get channel!")
    try:
        await bot.send_message(channel, "@!update {} {} {} {}".format(servers, users, channels, commands))
        msg = await bot.wait_for_message(content='API = True')
        return print("MDBL: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))
    except:
        print("[MDBL] Error sending or awaiting message!")
    return print("MDBL: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))

@bot.command(pass_context=True)
async def update(ctx):
    """Update status for MDBL"""
    # MDBL Status Update
    cmds = len(bot.commands)
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    author = ctx.message.author
    if author.id == ownerid or in admins:
        channel = bot.get_channel("567208400891543552")
        await bot.send_message(channel, "@!update {} {} {} {}".format(servers, users))
        msg = await bot.wait_for_message(content='API = True')
        print("MDBL: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))
    else:
        await bot.say("You are not the owner/admin of this bot)
bot.run('token')
 
