"""
Telegram Bot Scripts
"""
import os
import telebot

from telebot import types

telegram = telebot.TeleBot(os.getenv('BOT_TOKEN'))


def send_message_to_user(chat_id, request, type):
    """
    Send Message To User On Telegram

    Args:
        chat_id (int): Telegram Chat ID
        request (object): Request Payload
        type (str): Github Payload Type
    """
    link_button = types.InlineKeyboardButton(text='Open It!', url=request["commits"][0]["url"])
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(link_button)
    message_body = ''

    if type in ('push', 'Push Hook'):
        message_body = f'''New Commit On Your Ripo `{request["repository"]["name"]}` 🦊.
        \n\nCommit Message:
        \n`{request["commits"][0]["message"]}`'''
    elif type in ('tag_push', 'Tag Push Hook'):
        message_body = f'''New Tag Push On Your Ripo `{request["repository"]["name"]}` 🦊.
        \n\nTag Message:
        \n`{request["message"]}`'''
    else:
        message_body = f'''New {type} On Your Ripo `{request["repository"]["name"]}` 🦊.'''


    telegram.send_message(
        chat_id,
        message_body,
        parse_mode='Markdown',
        reply_markup=keyboard,
    )
