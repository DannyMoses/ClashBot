from discord.ext import commands

GUILD = 'Bot Testing'

bot = commands.Bot(command_prefix="!")


@bot.command(name="scout", help='Responds with basic op.gg data based on team you are up against')
async def scout(ctx):
    response = "WIP - not implemented yet!"

    await ctx.send(response)


bot.run(TOKEN)
