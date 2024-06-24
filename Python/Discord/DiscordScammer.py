import requests

ChannelID = 1174131672296468550
headers = {"authorization": "YOUR_DISCORD_BOT_TOKEN"}

with open("text.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    response = requests.post(
        f"https://discord.com/api/v9/channels/{ChannelID}/messages",
        headers=headers,
        json={"content": line.strip()}
    )
    print(response.status_code, response.json())
