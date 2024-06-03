import requests
import yaml
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
APPLICATION_ID = os.getenv('APPLICATION_ID')
URL = f'https://discord.com/api/v10/applications/{APPLICATION_ID}/commands'

with open("discord_commands.yaml", 'r') as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type":"application/json"}

for command in commands:
    response = requests.post(URL, headers=headers, json=command)
    command_name = command["name"]
    print(f"Command {command_name} created with status code {response.status_code}")