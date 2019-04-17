import discord
from discord.ext import commands
from discord.ext.commands import Bot
token = ''
prefix = ''

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix=prefix) # Sets the client and sets the prefix

@bot.event
async def on_ready():
    servers = len(bot.servers)
    users = len(set(bot.get_all_members())
    # MDBL Status Update
    channel = bot.get_channel("567208400891543552")
    await bot.send_message(channel, "@!update {} {}".format(servers, users))
    print("MDBL: Updated bot status (Guilds: {} | Users: {})".format(servers, users))
    
@bot.command(pass_context=True)
async def update(ctx):
    # MDBL Status Update
    servers = len(bot.servers)
    users = len(set(bot.get_all_members())
    channel = bot.get_channel("567208400891543552")
    await bot.send_message(channel, "@!update {} {}".format(servers, users))
    print("MDBL: Updated bot status (Guilds: {} | Users: {})".format(servers, users))
    
bot.run(token)
