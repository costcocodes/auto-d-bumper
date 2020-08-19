import logging
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(description="Bumper", command_prefix=".b ")

TOKEN = input('Please enter the token for the account you want to auto bump:\n')


@bot.command(aliases=['bump'])
async def start(ctx):
    while 1:
        bumpy = 0
        bumpy = bumpy + 1
        try:
            print("Processing a new bump...")
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
            print(f"Bump nr.{bumpy} processed successfully!")
        except:
            print(f"Couldn't process bump nr. {bumpy}. ")

@bot.event
async def on_connect():
    print("Successfully connected!")


@bot.event
async def on_ready():
    print('All systems fully operational.')


try:
    bot.run(TOKEN, bot=False)
except Exception as e:
    print(f"Invalid Token: {TOKEN}")
