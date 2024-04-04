from typing import Final, Dict, List
import datetime
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Embed
from dolist import get_todo_list, get_what_to_do

load_dotenv()

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN") #Get token

intents: Intents = Intents.default() #Get intents
intents.message_content = True #NOQA #Get message content
client: Client = Client(intents=intents) #Get client



#Generate an embed based on the day
def generate_embed(todo_list: List[str], day: str) -> Embed:

    def parse_activity(string: str):
        parts = string.split('-')
        return parts

    what_to_do = get_what_to_do()
    assignments: Dict[str, str] = what_to_do[0]
    upcoming_exams: Dict[str, str] = what_to_do[1]
    current_projects: List[str] = what_to_do[2]
    get_smarter: List[str] = what_to_do[3]

    assignment_str: str = "**Current Assignments Due:**\n"
    for key,value in assignments.items():
        assignment_str += f"{key}: {value}\n"
    assignment_str += "\n"

    exam_str: str = "**Upcoming Exams: **\n"
    for key,value in upcoming_exams.items():
        exam_str += f"{key}: {value}\n"
    exam_str += "\n"

    project_str: str = "**Current Active Projects:** \n"
    for project in current_projects:
        project_str += f"{project}\n"
    project_str += "\n"
    

    smarter_str: str = "**Improve Mentally:** \n"
    for smarter in get_smarter:
        smarter_str += f"{smarter}\n"
    smarter_str += "\n"

    embed = Embed(title=f"{day}'s Schedule", 
                    description=f"--------------------------------\n\n{assignment_str} {exam_str} {project_str} {smarter_str}--------------------------------\n",
                    color=0x315b9e, timestamp=datetime.datetime.now())
    
    embed.set_author(name="DotBot")

    embed.set_thumbnail(url="https://dan.onl/images/emptysong.jpg")

    for act in todo_list:
        parts = parse_activity(act)
        if len(parts) == 2:
            embed.add_field(name=f"{parts[0]} - {parts[1]}", value="", inline=False) 
        else:
            embed.add_field(name=f"{parts[0]}-->{parts[1]} - {parts[2]}", value="", inline=False) 

    return embed

#Send the embed daily at 7am to the user
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intent was not enabled, most likely")
        return
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]
    
    try: 
        if user_message.lower() == "test":
            response: Embed = generate_embed(get_todo_list(), datetime.datetime.now().strftime("%A"))   
            await message.author.send(embed=response) if is_private else await message.channel.send(embed=response)
    except NotImplementedError as e:
        await message.channel.send(str(e))
        print(e)

#When the bot is ready, print that it is connected to Discord
@client.event
async def on_ready() -> None:
    print(f"{client.user} has connected to Discord!")

#When a message is sent, check if the message is from the bot, if not, print the message
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"User: {username} said: {user_message} in channel: {channel}")
    await send_message(message, message.content)

def main()->None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()