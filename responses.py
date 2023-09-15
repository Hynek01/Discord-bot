import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "ping":
        return '<@1108520838287859712> <:trollface:1137222003586252890>'
    if p_message == "give me stock trading advice":
        return 'buy 100 shares in shitcoin'
    if p_message == "orc":
        return 'https://tenor.com/view/world-of-warcraft-orc-angry-gif-12083808'
    if p_message == "kim":
        return 'https://cdn.discordapp.com/attachments/473706892057772054/1150242189155237948/09092023093126.MP4'
    if p_message == "ping":
        return ''

