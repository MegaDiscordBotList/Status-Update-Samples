# MDBL - Discord Bot Listing
# Last Updated: 6/5/2019

# https://mdbl.surge.sh
# https://github.com/MegaDiscordBotList

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import config
owner = 'id'
admins = ['id', 'id']


async def post(bt, servers, users, channels, commands):
    # Posts status
    bot = bt
    try:
        print("\n-----------MDBL-----------\n"
              "Admins: {} | API: v6.6".format(len(admins)))
        print("\nSending update command... If this doesn't change there must of been an error")
        channel = bot.get_channel("567208400891543552")
        try:
            await bot.send_message(channel, "@!update {} {} {} {}".format(servers, users, channels, commands))
            msg = await bot.wait_for_message(content='API = True')
            return print("[MDBL]: Updated bot status (Guilds: {} | Users: {} | Channels: {} | Commands: {})".format(servers, users, channels, commands))
        except:
            print("[MDBL] Error sending or awaiting message!")
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print("[MDBL] Unable to execute script!\n{}".format(exc))
