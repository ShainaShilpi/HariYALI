import discord
import requests
from discord.ext import commands
client = discord.Client()

intents = discord.Intents(members=True)
client = discord.Client(intents=intents)
client = discord.Client

client = commands.Bot(command_prefix=">")
def get_aqi(city):
    url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
    querystring = {"city": city}
    headers = {
        'x-rapidapi-host': "air-quality-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6be9d4e810msh73e4a0ee5ddc0aep11de96jsn6e35aa8f1fbe"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    if "error" in data.keys():
        return "Couldn't find the place :("
    else:
        aqi = data['overall_aqi']
        return f"AQI in {city.upper()} is {aqi}"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>AQI '):
        aqi = get_aqi(message.content[5:])
        await message.channel.send("> " + aqi)




client.run("OTA4MzQwNjEzMDcyNzE1ODE2.YY0UHg.avTPIDQdotMLlMsI3XvrdCl-SeM")