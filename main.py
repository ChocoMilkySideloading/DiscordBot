import os
import discord
from discord import app_commands
from discord.ext import commands
import openai
import random

# Read tokens from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot is ready as {client.user}")
    try:
        synced = await client.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Sync error: {e}")

@client.tree.command(name="ask", description="Ask the AI anything")
@app_commands.describe(question="Your question")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=200
        )
        answer = response.choices[0].message.content
        await interaction.followup.send(answer)
    except Exception as e:
        await interaction.followup.send(f"⚠️ Error: {e}")

@client.tree.command(name="dns", description="Best DNS by Choco Milky Sideloading")
async def dns(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Here is the best DNS by Choco Milky Sideloading:\n"
        "https://cdn.discordapp.com/attachments/1376994219649929388/1398794767084683274/Neb_DNS__Webclip.mobileconfig?ex=688de8e4&is=688c9764&hm=b61ec89bedd7a640ba4aadd7bdc522a117f68f91c0336c4b12e98a43563e0ba7&"
    )

@client.tree.command(name="8ball", description="Magic 8 ball answers")
@app_commands.describe(question="Ask the 8 ball")
async def eight_ball(interaction: discord.Interaction, question: str):
    responses = [
        "Yea", "Nah bruh", "Looks like that’s a yes", "Prolly bro",
        "Doubt it", "100%", "Absolutely not", "Might be, might not",
        "Try again later", "Fr fr", "For sure", "Lmao nope", "It’s possible",
        "Why are you asking me?", "💀", "Signs point to yes", "Very doubtful",
        "Without a doubt", "Ask again later", "Better not tell you now",
        "Cannot predict now", "Concentrate and ask again", "Don't count on it",
        "My reply is no", "Outlook good", "Outlook not so good"
    ]
    answer = random.choice(responses)
    await interaction.response.send_message(f"🎱 {answer}")

@client.tree.command(name="chocomilky", description="Choco Milky app for iOS 14+")
async def chocomilky(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Here is the Choco Milky app for iOS 14 and over:\n"
        "https://cdn.discordapp.com/attachments/1373569891994697888/1378195101104476232/choco_milky_app.mobileconfig?ex=688d74b5&is=688c2335&hm=1ded2c12cd49bccb9d3fb48beadd07a1e4b22c63a99b74e3e9ba4e5271fc32bd&"
    )

@client.tree.command(name="coinflip", description="Flip a coin")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"🪙 The coin landed on **{result}**!")

@client.tree.command(name="roll", description="Roll a dice (1-6)")
async def roll(interaction: discord.Interaction):
    number = random.randint(1, 6)
    await interaction.response.send_message(f"🎲 You rolled a **{number}**!")

@client.tree.command(name="joke", description="Tell a random joke")
async def joke(interaction: discord.Interaction):
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t programmers like nature? It has too many bugs.",
        "Why do we tell actors to 'break a leg?' Because every play has a cast.",
        "I would tell you a construction joke, but I'm still working on it."
    ]
    await interaction.response.send_message(random.choice(jokes))

@client.tree.command(name="pfp", description="Get someone's profile picture")
@app_commands.describe(user="The user whose profile picture you want")
async def pfp(interaction: discord.Interaction, user: discord.Member):
    avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
    embed = discord.Embed(title=f"{user.display_name}'s Profile Picture")
    embed.set_image(url=avatar_url)
    await interaction.response.send_message(embed=embed)

client.run(DISCORD_TOKEN)
