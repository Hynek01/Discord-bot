import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if "ping" in p_message:
        return 'https://cdn.discordapp.com/attachments/849750633967910942/1152069744464252998/IMG_2628.png <@1108520838287859712><:trollface:1137222003586252890>'
    if p_message == "give me stock trading advice":
        return 'buy 100 shares in shitcoin'
    if p_message == "orc":
        return 'https://tenor.com/view/world-of-warcraft-orc-angry-gif-12083808'
    if p_message == "kim":
        return 'https://cdn.discordapp.com/attachments/473706892057772054/1150242189155237948/09092023093126.MP4'
    if p_message == "logan":
        return 'https://cdn.discordapp.com/attachments/916437526816907314/970211334337744956/EDP.gif'
    if p_message == "green":
        return 'https://media.discordapp.net/attachments/879126123382976543/879126271387373628/caption.gif'

#204 Queensbury Drive, Winston-Salem, NC
#https://media.discordapp.net/attachments/879126123382976543/879126271387373628/caption.gif