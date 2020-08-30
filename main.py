from discord.ext import commands

RIOT_API = 'RGAPI-db7a7e85-984b-440f-b444-d8184b3170ce'
TOKEN = 'NzQ3NTkwODI0NjMxNzMwMjI2.X0RGNg.0h_zwy7Arw5jox1BShhqeh0Pxro'
GUILD = 'Bot Testing'

bot = commands.Bot(command_prefix="!")


@bot.command(name="scout", help='Responds with basic op.gg data based on team you are up against')
async def scout(ctx):
    response = "WIP - not implemented yet!"

    await ctx.send(response)


bot.run(TOKEN)
