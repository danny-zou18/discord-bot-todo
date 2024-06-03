import requests
import yaml

TOKEN = "MTIyMDQ0MzkzMTMwNTU3ODU2Ng.G-GzY3.hwcFUu-7kicv0KkfdAB_9dB786DRCOFNSbscSk"
APPLICATION_ID = "1220443931305578566"
URL = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"

with open("discord_commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

# Send the POST request for each command
for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")