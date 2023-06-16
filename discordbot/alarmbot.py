import reponses
import discord


async def send_message(message, user_message, is_private): 
    try:
        response = reponses.handle_reponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
        
def run_discordbot():
    TOKEN = "enter token here"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(command_prefix = '!', intents = intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now runnning!')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message,user_message, is_private= True)    
        else:
            await send_message(message,user_message, is_private= False)   
        
        
    client.run(TOKEN)
