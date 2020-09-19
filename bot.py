import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')


async def on_ready():
    print(f'\n\nBot is ready!\nName: {bot.user.name}\nID: {bot.user.id}\n      ---------\n')

    return

# Load and unload cogs

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}') #loads the extension in the "cogs" folder
    await ctx.send(f'Loaded "{extension}"')
    print(f'Loaded `"{extension}"`')

    return


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}') #unloads the extension in the "cogs" folder
    await ctx.send(f'Unloaded "{extension}"')
    print(f'Unoaded `"{extension}"`')

    return

print('\n')




for filename in os.listdir('./cogs'): #loads all files (*.py)
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') #loads the file without ".py" for example: cogs.ping
        print(f'Loaded {filename[:-3]}')

#end of weather---------------------------------------------------------------
# Time Zones----------------------------------------

bot.run('YOUR_TOKEN_HERE')