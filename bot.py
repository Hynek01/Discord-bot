import discord
import responses
import datetime
import subprocess

TOKEN = "MTE1MjAyODA4MTMzNTMwODI5OQ.GUebT7.97XRnPuOOUM0PudHQdwF8xbe_CTJUpolw3bRoo"


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(
            response
        ) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


async def send_dm_to_user(user, message_content):
    try:
        await user.send(message_content)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message.startswith("$send_dm"):
            # Extract the message content after "!send_dm"
            message_parts = user_message.split()
            if len(message_parts) >= 3:
                user_id_mention = message_parts[1]
                try:
                    # Extract the user ID from the mention
                    user_id = int(user_id_mention.strip("<@!>"))
                    # Construct the message content
                    message_content = " ".join(message_parts[2:])
                    if message_content:
                        target_user = await client.fetch_user(user_id)
                        if target_user:
                            await send_dm_to_user(target_user, message_content)
                            await message.channel.send("dm sent, jit.")
                        else:
                            await message.channel.send("User not found.")
                    else:
                        await message.channel.send("wtf is the message jit")
                except ValueError:
                    await message.channel.send("the user id is invalid jit")
            else:
                await message.channel.send("Usage: $send_dm <@user_id> <message>")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
            file_path = "C:/Users/Computer/Desktop/Discord bot/private_messages.txt"
            current_time = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )  # Format the current time
            with open(file_path, "a") as file:
                file.write(
                    f"{current_time} - {message.author.name} ({message.author.id}): {message.content}\n"
                )
            subprocess.Popen(
                [
                    "cmd.exe",
                    "/c",
                    f"echo {current_time} - {message.author.name} ({message.author.id}): {message.content}",
                ]
            )

    client.run(TOKEN)
