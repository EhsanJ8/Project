from typing import Text
from telegram import InlineKeyboardButton, InlineKeyboardMarkup , Update
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler , CallbackContext
import requests
import json
from flask import Flask
from flask import request
from flask import Response

question = "'1.Are you German?\nYes, ....\n', 'A)you are German\nB)I am\nC)he is'"

# updater = Updater(token="1882328872:AAGJgHfGutnh6qXzykJVVjyQoIoSMKZObbM")
# dispatcher = updater.dispatcher
def gozine3(update: Update , context:CallbackContext):
    keyboard = [
        [InlineKeyboardButton("A" , callback_data="1"),
        InlineKeyboardButton("B", callback_data="2")],
        [InlineKeyboardButton("C" , callback_data="3")],
        [InlineKeyboardButton("Skip" , callback_data="0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(question, reply_markup=reply_markup)
def gozine4(update: Update , context:CallbackContext):
    keyboard = [
        [InlineKeyboardButton("A" , callback_data="1"),
        InlineKeyboardButton("B", callback_data="2")],
        [InlineKeyboardButton("C" , callback_data="3"),
        InlineKeyboardButton("D" , callback_data="4")]
        [InlineKeyboardButton("Skip" , callback_data="0")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(question, reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option: {query.data}")

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1882328872:AAGJgHfGutnh6qXzykJVVjyQoIoSMKZObbM")

    updater.dispatcher.add_handler(CommandHandler('English_quiz', gozine3))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
