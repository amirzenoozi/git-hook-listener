"""
Telegram Bot Scripts
"""
import os
import telebot

from telebot import types

telegram = telebot.TeleBot(os.getenv('BOT_TOKEN'))


def send_message_to_user(chat_id, request):
    """
    Send Message To User On Telegram

    Args:
        chat_id (int): Telegram Chat ID
        request (object): Request Payload
    """
    link_button = types.InlineKeyboardButton(text='Open It!', url=request["web_url"])
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(link_button)

    telegram.send_message(
        chat_id,
        f'New Commit On Your Ripo 🦊. \n\nCommit Message:\n`{request["name"]}`',
        parse_mode='Markdown',
        reply_markup=keyboard,
    )
