from discord.ext import commands

import discord
import json
import embeds

with open('config.json', 'r') as f:
	config = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'])

async def on_ready():
	guild_names = ', '.join([ a.name for a in bot.guilds ])
	print('python-bot online and logged in as %s' % bot.user)
	print('Connected to %s guild(s): %s' % (len(bot.guilds), guild_names))
	print('Now awaiting commands...')

async def on_command_error(ctx, err):
	await ctx.send(embed=embeds.CommandErrorEmbed(err, ctx))

@bot.command(name=config['commands']['calculate_sum'], help='')
@commands.has_permissions(administrator=True)
async def calculate_sum(ctx, *values : int):
    await ctx.send(sum(values))

bot.add_listener(on_ready)
bot.add_listener(on_command_error)
bot.run(config['token'])
