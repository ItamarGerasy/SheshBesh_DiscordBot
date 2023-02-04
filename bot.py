import discord
import responses
INVITE_LINK = \
    "https://discord.com/api/oauth2/authorize?client_id=1070794822169940029&permissions=534723950656&scope=bot"


async def send_message(message, user_message):
    try:
        response = responses.handle_respons(message=user_message)
        await message.channel.send(response)
    except Exception as e:
        print("something went wrong")
        
        
def run_discord_bot():
    TOKEN = "MTA3MDc5NDgyMjE2OTk0MDAyOQ.GDjZDA.SR3rmUYftNK1BGFiFsQuuHfsVYvih50cW7apvs"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'${client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        userName = str(message.author.name)
        channel = str(message.channel)
        user_message = message.content

        await send_message(message, user_message)

    client.run(TOKEN)
    
    