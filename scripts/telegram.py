import os
import telebot

from telebot import types
from dotenv import load_dotenv

config = load_dotenv(".env")
telegram = telebot.TeleBot(os.getenv('BOT_TOKEN'))


def send_message_to_user(chatId, request):
    link_button = types.InlineKeyboardButton(text='Open It!', url=request.json["web_url"])
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(link_button)

    telegram.send_message(
        chatId,
        f'New Commit On Your Ripo 🦊. \n\nCommit Message:\n`{request.json["name"]}`',
        parse_mode='Markdown',
        reply_markup=keyboard,
    )