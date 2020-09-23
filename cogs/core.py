import discord
from discord.ext import commands
import platform
import requests

class Core(commands.Cog, name="core"):
    """
    Main Bot commands
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} has been loaded\n-------")

#Wather----------------------------------------------------

    @commands.command(name="weather")
    async def Weather(self, ctx, *, city: str):
        """
        Show your city's weather
        """
        api_key = 'your_apikey'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":
            async with channel.typing():
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                owner = str(ctx.guild.owner)
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                weather_description = z[0]["description"]
                embed = discord.Embed(title=f"Weather in {city_name}",
                                color=ctx.guild.me.top_role.color,
                                timestamp=ctx.message.created_at,)
                embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
                embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Coded by {owner} with ❤ using discord.py", icon_url="https://www.python.org/static/opengraph-icon-200x200.png")

                await channel.send(embed=embed)
        else:
            await channel.send("City not found.")    
    
    # invite the bot.

    @commands.command(name="invite", usage="invite")
    async def invite(self, ctx):
        """
        Invite this bot
        """
        await ctx.send(
            embed=discord.Embed(
                title="Invite Link",
                description=f"https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}"
                    "&permissions=268823640&scope=bot",
                colour=ctx.author.colour,
                )
            )

    # show member's avatar.

    @commands.command(name='avatar', aliases=['Avatar'])
    async def av_cmd(self, ctx, user: discord.Member):
        """
        Show member's avatar
        """
        embed = discord.Embed(
        colour = ctx.author.colour,
        title=f"{user}"
        )
        embed.set_image(url=f"{user.avatar_url}")
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url="https://www.python.org/static/opengraph-icon-200x200.png")
        await ctx.send(embed=embed)

# if the member don't mention a member then send his own avatar.

    @av_cmd.error
    async def av_error(self, ctx, error):
        if isinstance (error, commands.MissingRequiredArgument):

            embed = discord.Embed(
                colour = ctx.author.colour,
                title=f"{ctx.author}"
                )
            embed.set_image(url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)


    @commands.command(name="ping", description="Pings the bot")
    async def ping(self, ctx):
        """
        Ping the bot
        """
        await ctx.send(f'Ping is: `{round(self.bot.latency * 1000)}ms`')



    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
        """
        Usefull command to show member's info
        """
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at,
                                    title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("```%a, %#d %B %Y, %I:%M %p UTC```"), inline=False)
        embed.add_field(name="ID:", value=f"```{member.id}```", inline=False)
        embed.add_field(name="Display Name:", value=f"```{member.display_name}```", inline=True)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url="https://www.python.org/static/opengraph-icon-200x200.png")

        await ctx.send(embed=embed)

    @commands.command(aliases=["sinfo"])
    async def server(self, ctx):
        """
        Show server info.
        """
        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        embed = discord.Embed(
            title= "Server info for: " + name,
            colour = ctx.author.colour
        )
        embed.set_image(url='https://icon-library.com/images/more-info-icon/more-info-icon-12.jpg')
        embed.set_thumbnail(url=icon)
        embed.add_field(name="**Server Owner**", value=f"```{owner}```", inline=True)
        embed.add_field(name="**Server ID**", value=f"```{id}```", inline=True)
        embed.add_field(name="**Region**", value=f"```{region}```", inline=True)
        embed.add_field(name="**Members**", value=f"```{memberCount}```", inline=True)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url="https://www.python.org/static/opengraph-icon-200x200.png")
        await ctx.send(embed=embed)


    @commands.command(name="info", aliases=["stats"])
    async def info(self, ctx):
        """
        Show bot's stats
        """
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(
            title='***About Sigma***', 
            description = '*Sigma was made by* ' '[@Fate 怒#5957](https://github.com/nxtlo) ' '*for self learning using* ' '[Discord.py](https://github.com/Rapptz/discord.py)', 
            colour=ctx.author.colour, 
            timestamp=ctx.message.created_at
            )
        embed.add_field(name='**Python version**', value=f"```{pythonVersion}```")
        embed.add_field(name='**Discord.py version**', value=f"```{dpyVersion}```")
        embed.add_field(name='**Total Guilds**', value=f"```{serverCount}```")
        embed.add_field(name=f'**Total Users**', value=f"```{memberCount}```")
        embed.add_field(name='**Bot Developer**', value=f"<@350750086357057537>")

        embed.set_footer(text=f"{self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Core(bot))