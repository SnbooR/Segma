import discord
import os
from discord.ext import commands
import psutil
from pretty_help import Navigation, PrettyHelp, __version__
                   # you can change the prefix from here
bot = commands.Bot(command_prefix="YOUR_PREFIX", help_command=PrettyHelp())


@bot.event
async def on_ready():
        
    print('Logged in as:\n')
    print('Bot name:\n', bot.user.name)
    print('Bot id:\n',bot.user.id)
    print('Discord Version:\n',discord.__version__) 
    print('------')
    print('Servers connected to:')
    
    # whats the bot listening to, change the 'YOUR_BOT_STATUS'
    activity = discord.Game(name="YOUR_BOT_STATUS", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    
    # allow the bot to send a message when he go online.
    channel = bot.get_channel(YOUR_CHANNEL_ID)
    await channel.send("I'm online!")
    
    for guild in bot.guilds:
        print(guild.name, "\n")

# Load and unload cogs

@bot.command()
@commands.is_owner()
async def load(ctx, extension, hidden=True):
        bot.load_extension(f'cogs.{extension}') #loads the extension in the "cogs" folder
        await ctx.send(f'Loaded "{extension}"')
        print(f'Loaded `"{extension}"`')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension, hidden=True):
        bot.unload_extension(f'cogs.{extension}') #unloads the extension in the "cogs" folder
        await ctx.send(f'Unloaded "{extension}"')
        print(f'Unoaded `"{extension}"`')

# only the owner of the bot can load and unload cogs, you can change it to a specific role or else
print('\n')

for filename in os.listdir('./cogs'): #loads all files (*.py)
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') #loads the file without ".py" for example: cogs.ping

bot.run('YOUR_BOT_TOKEN')
