import discord
import random
import requests

class MyClient(discord.Client):
    #Wenn eingeloggt
    async def on_ready(self):
        print("Der Bre ist am Start!!")
       

    #Wenn Nachricht
    async def on_message(self, message):
        print("Nachricht von " + str(message.author) + " ennthält " + str(message.content))

        if message.content.startswith("Hallo Rama"):
            await message.channel.send("Hallo " + str(message.author) + " du geile Sau!!")
        
        if message.content.startswith("rama welche lane"):
            num = random.randint(1,5)
            lane = ""
            if num == 1:
                lane = "Top"
            elif num == 2:
                lane = "Jungle"
            elif num == 3:
                lane = "Mid"
            elif num == 4:
                lane = "ADC"
            elif num == 5:
                lane = "Support"
            
            await message.channel.send("Du gehst auf die " + lane + " Lane Bre.")
        
        if message.content.startswith("rama wer wohin"):
            lanes = ["Toplane", "Jungle", "Midlane", "ADC", "Support"]
            random.shuffle(lanes)
            await message.channel.send("Edwin: " + lanes[0] + "\nDennis: " + lanes[1] + "\nJoschka: " + lanes[2] + "\nTim: " + lanes[3] + "\nLeon: " + lanes[4])
        
        if message.content.startswith("bre"):
            await message.channel.send("Ich möchte nicht \"bre\" genannt werden, nenn mich bitte \"rama\" und ich erfülle dir deine Wünsche!")
        
        if message.content.startswith("rama btc"):
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            json = response.json()
            await message.channel.send(str(json["bpi"]["USD"]["rate_float"]))

        if message.content.startswith("rama witz"):
            response = requests.get("https://sv443.net/jokeapi/v2/joke/Dark?type=twopart")
            json = response.json()
            await message.channel.send(str(json["setup"]) + "\n" + str(json["delivery"]))


client = MyClient()
client.run('XXXXXX')

