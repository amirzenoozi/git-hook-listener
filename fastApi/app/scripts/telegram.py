"""
Telegram Bot Scripts
"""
import os
import telebot

from telebot import types

telegram = telebot.TeleBot(os.getenv('BOT_TOKEN'))


def send_message_to_user(chat_id, request, req_type):
    """
    Send Message To User On Telegram

    Args:
        chat_id (int): Telegram Chat ID
        request (object): Request Payload
        req_type (str): GitHub Payload Type
    """
    message_body = ''

    if req_type in ('release', 'Release Hook'):
        link_button = types.InlineKeyboardButton(text='Open It!', url=request["url"])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(link_button)
        message_body = f'''New Release On Your Repo `{request["project"]["name"]}` 🦊.
        \n\nRelease Name: {request["name"]}
        \nTag Name: {request["tag"]}
        \n\n{request["description"]}'''
    else:
        link_button = types.InlineKeyboardButton(text='Open It!', url=request["repository"]["homepage"])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(link_button)
        message_body = f'''New {req_type} On Your Repo `{request["repository"]["name"]}` 🦊.'''


    telegram.send_message(
        chat_id,
        message_body,
        parse_mode='Markdown',
        reply_markup=keyboard,
    )
def send_message_to_single_topic(chat_id, request, req_type, thread_id):
    """
    Send Message To Topic

    Args:
        chat_id (int): Telegram Chat ID
        request (object): Request Payload
        req_type (str): GitHub Payload Type
        thread_id (int): Topic ThreadId
    """
    message_body = ''

    if req_type in ('release', 'Release Hook'):
        link_button = types.InlineKeyboardButton(text='Open It!', url=request["url"])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(link_button)
        message_body = f'''New Release On Your Repo `{request["project"]["name"]}` 🦊.
        \n\nRelease Name: {request["name"]}
        \nTag Name: {request["tag"]}
        \n\n{request["description"]}'''
    else:
        link_button = types.InlineKeyboardButton(text='Open It!', url=request["repository"]["homepage"])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(link_button)
        message_body = f'''New {req_type} On Your Repo `{request["repository"]["name"]}` 🦊.'''


    telegram.send_message(
        chat_id=chat_id,
        text=message_body,
        parse_mode='Markdown',
        reply_markup=keyboard,
        message_thread_id=thread_id,
    )
