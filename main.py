from typing import Final, Dict, List
import datetime
import schedule
import asyncio
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

    assignment_str: str = "**Current Assignments Due:**\n\n"
    for key,value in assignments.items():
        assignment_str += f"{key}: {value}\n\n"
    assignment_str += "\n"

    exam_str: str = "**Upcoming Exams: **\n\n"
    for key,value in upcoming_exams.items():
        exam_str += f"{key}: {value}\n\n"
    exam_str += "\n"

    project_str: str = "**Current Active Projects:** \n\n"
    for project in current_projects:
        project_str += f"{project}\n\n"
    project_str += "\n"
    
    smarter_str: str = "**Improve Mentally:** \n\n"
    for smarter in get_smarter:
        smarter_str += f"{smarter}\n\n"

    embed = Embed(title=f"{day}'s Schedule", 
                    description=f"--------------------------------\n\n{assignment_str} {exam_str} {project_str} {smarter_str}--------------------------------\n",
                    color=0x315b9e, timestamp=datetime.datetime.now())
    
    embed.set_author(name="DotBot")

    embed.set_thumbnail(url="https://dan.onl/images/emptysong.jpg")
    
    for act in todo_list:
        parts = parse_activity(act)
        if len(parts) == 2:
            embed.add_field(name=f"{parts[0]}", value=f"{parts[1]}", inline=False) 
        else:
            embed.add_field(name=f"{parts[0]}-->{parts[1]}", value=f"{parts[2]}", inline=False) 

    return embed

#Send the embed daily at 7am to the user
async def send_daily_message() -> None:
    channel = client.get_channel(1220445463308664873)
    print("Sent!")
    try:
        response: Embed = generate_embed(get_todo_list(), datetime.datetime.now().strftime("%A"))   
        await channel.send("Good Morning Danny! Here is your schedule for today!")
        await channel.send(embed=response)
    except NotImplementedError as e:
        print(e)
def schedule_send_message():
    asyncio.ensure_future(send_daily_message())

#When the bot is ready, print that it is connected to Discord
@client.event
async def on_ready() -> None:
    print(f"{client.user} has connected to Discord!")
    schedule.every().day.at("07:00").do(schedule_send_message)
    while True:
        schedule.run_pending()
        await asyncio.sleep(10)

def main()->None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()