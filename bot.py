import discord
import responses

async def send_message(message,user_message,is_private):
    try:
        response = responses.handle_response(user_message)
        #TODO Delete usermessage if they send a tweet
        if response != None:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = 'MTE2MzU4MDIxMTMwOTMyMjMyMQ.Gs5aty.e8Uu5YcEaJpAZm67dPGg4rv08Fs6jiF1r-UGQ4'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async  def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print (f"{username} said : '{user_message}' in channel: {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message,user_message,is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        if "x.com" in user_message:
            await message.delete()

    client.run(TOKEN)