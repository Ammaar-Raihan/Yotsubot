import random
import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='!')
TOKEN = ''

statusMsg = cycle(['with my toys', 'with my friends',
                   'with you :D', 'on my bike', 'with jumbo', 'with rocks'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')


@client.event
async def on_message(ctx):
    if ctx.author.id == 274993976841338881:
        return

    author = ctx.author
    userid = ctx.author.id
    content = ctx.content
    channel = ctx.channel
    print('{} ({}) in {}: {}'.format(author, userid, channel, content))

    if author == client.user:
        return

    badabing = '<:badabing:583350658078474260>'
    badaboom = '<:badaboom:583350676776681472>'

    if content == badabing:
        await channel.send(badaboom)

    await client.process_commands(ctx)


@tasks.loop(minutes=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(statusMsg)))


@client.command(aliases=['colour', 'color', 'c'])
async def change_colour(ctx, *, colorCode: discord.Color):
    """Change user's role color to the provided hex value."""
    memberRole = ctx.author.top_role
    print(memberRole.color)
    print(colorCode)
    await memberRole.edit(color=colorCode)


@client.command(aliases=['name', 'n'])
async def change_name(ctx, *, roleName):
    """Change user's role name to the provided string."""
    memberRole = ctx.author.top_role
    await memberRole.edit(name=roleName)


@client.command()
async def smile(ctx):
    smileEmbed = discord.Embed(
        title="My smile is gone for good",
        colour=discord.Color.blue()
    )
    smileEmbed.set_image(url="https://i.imgur.com/WIliq9j.jpg")
    await ctx.send(content=None, embed=smileEmbed)


@client.command()
async def hate(ctx):
    author = str(ctx.author.id)
    await ctx.send("I don't like you <@" + author + ">")


@client.command()
async def love(ctx):
    author = str(ctx.author.id)
    await ctx.send("I love you <@" + author + ">")


client.run(TOKEN)
