from time import sleep
import discord
from discord import app_commands
import random
from webserver import keep_alive
import os
import cloudscraper

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1035271016034861146))
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "mines", description = "Sends a Mines Prediction.", guild=discord.Object(id=1035271016034861146))
async def slash(interaction: discord.Interaction, round_id: str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        emb = discord.Embed(title = "Round ID Error!",  description = "Inputed Round ID is Invalid!", color = 0x000000)
        await interaction.response.send_message(embed=emb)
    elif round_length == 36:
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ ', '❓ '
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = "✅ "
        elif a == 2:
            mine2 = "✅ "
        elif a == 3:
            mine3 = "✅ "
        elif a == 4:
            mine4 = "✅ "
        elif a == 5:
            mine5 = "✅ "
        elif a == 6:
            mine6 = "✅ "
        elif a == 7:
            mine7 = "✅ "
        elif a == 8:
            mine8 = "✅ "
        if b == 9:
            mine9 = "✅ "
        elif b == 10:
            mine10 = "✅ "
        elif b == 11:
            mine11 = "✅ "
        elif b == 12:
            mine12 = "✅ "
        elif b == 13:
            mine13 = "✅ "
        if c == 14:
            mine14 = "✅ "
        elif c == 15:
            mine15 = "✅ "
        elif c == 16:
            mine16 = "✅ "
        elif c == 17:
            mine17 = "✅ "
        if d == 18:
            mine18 = "✅ "
        elif d == 19:
            mine19 = "✅ "
        elif d == 20:
            mine20 = "✅ "
        elif d == 21:
            mine21 = "✅ " 
        elif d == 22:
            mine22 = "✅ " 
        elif d == 23:
            mine23 = "✅ "
        elif d == 24:
            mine24 = "✅ "
        elif d == 25:
            mine25 = "✅ "
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        info = str(random.randint(45, 90))
        icon = 'https://cdn.discordapp.com/attachments/1035141882717679616/1035181961041416212/IMG_5636.gif'
        
        em = discord.Embed(description = "`Connected to Klay - Mines Predictor`", color=0x000000)
        
        em.set_footer(text="Klay Predictor", icon_url=icon)
        em.add_field(name="Grid",value="```\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n```")
        em.add_field(name = "Round ID", value = "```\n" + round_id + "\n```")
        em.add_field(name="Win Rate", value="```\n" + info + "%" +  "\n```")
        
        await interaction.response.send_message(embed=em) 
        

@tree.command(name = "towers", description = "Sends a Towers Prediction.", guild=discord.Object(id=1035271016034861146))
async def slash2(interaction: discord.Interaction, round_id: str):
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length < 36:
        emb = discord.Embed(title = "Round ID Error!",  description = "Inputed Round ID is Invalid!", color = 0x000000)
        await interaction.response.send_message(embed=emb)
    elif round_length == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓', '❓'
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = "⭐️"
        elif a == 2:
            tower2 = "⭐️"
        elif a ==3:
            tower3 = "⭐️"
        if b == 1:
            tower4 = "⭐️"
        elif b == 2:
            tower5 = "⭐️"
        elif b ==3:  
            tower6 = "⭐️"
        if c == 1:
            tower7 = "⭐️"
        elif c == 2:
            tower8 = "⭐️"
        elif c ==3:
            tower9 = "⭐️"
        if d == 1:
            tower10 = "⭐️"
        elif d == 2:
            tower11 = "⭐️"
        elif d ==3:
            tower12 = "⭐️"
        if e == 1:
            tower13 = "⭐️"
        elif e == 2:
            tower14 = "⭐️"
        elif e ==3:
            tower15 = "⭐️"
        if f == 1:
            tower16 = "⭐️"
        elif f == 2:
            tower17 = "⭐️"
        elif f ==3:
            tower18 = "⭐️"
        if g == 1:
            tower19 = "⭐️"
        elif g == 2:
            tower20 = "⭐️"
        elif g ==3:
            tower21 = "⭐️"
        if h == 1:
            tower22 = "⭐️"
        elif h == 2:
            tower23 = "⭐️"
        elif h ==3:
            tower24 = "⭐️"

        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
        info = str(random.randint(45, 95))
        icon = 'https://cdn.discordapp.com/attachments/1035141882717679616/1035181961041416212/IMG_5636.gif'
        
        em = discord.Embed(description="`Connected to Klay - Towers Predictor`", color=0x000000)
        
        em.set_footer(text="Klay Predictor", icon_url=icon)
        em.add_field(name="Grid", value="```\n" + row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n```")   
        em.add_field(name = "Round ID", value = "```\n" + round_id + "\n```")
        em.add_field(name="Win Rate", value="```\n" + info + "%" +  "\n```")
        await interaction.response.send_message(embed=em) 

@tree.command(name = "pricelist", description = "Sends the Paid Bot Prices.", guild=discord.Object(id=1035271016034861146))
async def slash3(interaction: discord.Interaction):
  em = discord.Embed(title = "Paid Klay Prices & Perks!", description = "Want to buy? Create a ticket at #ticket by clicking the button!", color = 0x000000)
  em.set_image(url="https://cdn.discordapp.com/attachments/1035519963357790289/1035924218619117638/Untitled4_20221029223245.png")


  await interaction.response.send_message(embed = em)

s = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})

def crashPoint(num):
    info = s.get('https://api.bloxflip.com/games/crash').json()['history'][num]['crashPoint']
    return info

@tree.command(name="crash", description="Sends Crash Prediction", guild=discord.Object(id=1035271016034861146))
async def slash4(interaction: discord.Interaction):
    one = crashPoint(0)
    two = crashPoint(1)
    three = crashPoint(2)

    pst3 = [one, two, three]

    #get average of paste 3 games
    average = sum(pst3) / len(pst3)
    prediction = (1 / (average - 2) / 1)
    if prediction < 1:
        prediction = 1. + prediction
    safe = ''
    if prediction > 3:
        safe = 'Above 2x'
    elif prediction < 3:
        safe = "Less than 1.5x"
    elif prediction > 4:
        safe = 'Above 4x'
    prediction = "{:.2f}".format(prediction)
    em = discord.Embed(color=0xff55ff)
    em.add_field(name=f"**Prediction: {prediction}x**", value=f"Average: {int(average)}\nSafe Bet: {safe}")
    await interaction.response.send_message(embed=em)

keep_alive()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)