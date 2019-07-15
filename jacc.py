
token = "token" #You get that from the discord developer portal
userid = "ID" #You own UserID
prefix = "j!" #Prefix for jacc

import discord
from discord.ext import commands

print("Waking up jacc Zzz")

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Do " + prefix + "dm 'message' to run jacc.")

try:
    async def self_check(ctx):
        if bot.user.id == userid or ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dm(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"Sent {user.name} a DM.")
            except:
                print(f"Couldn't DM {user.name}.")
        print("Sent all the server a DM.")

  
except:
    pass

bot.run(token)