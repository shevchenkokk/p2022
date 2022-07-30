from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from datetime import datetime
import os
from parser import *
from settings import *

TELEGRAM_TOKEN = SECRET_TOKEN

def start_handler(update, context):
    text = 'Привет! Выбери желаемую команду:'
    keyboard = [
        [InlineKeyboardButton(text='Получить расписание электричек', callback_data='get_schedule')],
        [InlineKeyboardButton(text='Получить информацию о задержках поездов', callback_data='get_delays_info')],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text=text, reply_markup=markup)

def help_handler(update, context):
    text = 'Данный бот предназначен для получения результата парсинга расписания электричек по направлению '\
    'Тушинская-Стрешнево на сегодняшний день. Данные получены с сайта tutu.ru\n'\
    'Получить данные о расписании можно в формате JSON и XLSX.\n'\
    'Также вы можете получить информацию о возможных задержках/отменах поездов по данному направлению.\n'\
    'Просто введите команду \start и попробуйте сами.'
    update.message.reply_text(text=text)

def callback_handler(update, context):
    query = update.callback_query
    query.answer()
    main()
    filenames = {
        'get_json': json_result_filename,
        'get_xlsx': xlsx_result_filename,
    }
    if query.data == 'get_schedule':
        text = 'Выбери, в каком формате прислать расписание:'
        keyboard = [
            [InlineKeyboardButton(text='Получить JSON', callback_data='get_json')],
            [InlineKeyboardButton(text='Получить XLSX', callback_data='get_xlsx')],
        ]
        markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(query.message.chat.id, text=text, reply_markup=markup)
    elif query.data in ('get_json', 'get_xlsx'):
        filename = filenames[query.data]
        date = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')
        caption = 'Данные получены: {}'.format(date)
        with open(filename, 'rb') as file:
            context.bot.send_document(query.message.chat.id, document=file, caption=caption)
    elif query.data == 'get_delays_info':
        for id in map:
            text = ''
            if map[id]['delaysInfo'] is not None:
                text += map[id]
        if not text:
            text = 'На текущий момент задержек поездов по направлению Тушинская - Стрешнево нет.'
        context.bot.send_message(query.message.chat.id, text=text)    

updater = Updater(TELEGRAM_TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))

updater.start_polling()
updater.idle()