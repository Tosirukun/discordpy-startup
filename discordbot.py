from discord.ext import commands
import os
import traceback
import requests
import json
import discord

bot = commands.Bot(command_prefix='tn!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def server(ctx):
    body = requests.get("https://api.tosirukun.tk/api/tapi?type=server").text
    data = json.loads(body)
    await ctx.send(embed=discord.Embed(title="とじるくんネットワークのステータス").add_field(name="現在の接続数", value=data["data"]["online"]).add_field(name="接続可能な最大数", value=data["data"]["max"]))


bot.run(token)
