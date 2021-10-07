from django.core.management.base import BaseCommand

import telebot
from telebot import types
import re
from core.models import User, Position, Tag

BASE_URL = 'http://80.78.246.198:3000'

def create_link(tg_id):
    return BASE_URL + '?tg_id=' + str(tg_id)

def get_user_insance(message) -> User:
    user_id = message.from_user.id
    username = message.from_user.username
    user, _ = User.objects.get_or_create(tg_id=user_id, username=username)
    return user

def start_bot():
    bot = telebot.TeleBot('2040176965:AAHk1imMOdXlI_67w8fquf0MZjs5EkL7ujw')

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":
            link = create_link(call.message.chat.id)
            bot.send_message(call.message.chat.id, 'Отлично! Выбери интересующие тебя теги по ссылке - \n {link}'.format(link=link))
            bot.register_next_step_handler(call.message, get_tags)
        if call.data == '20':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 20000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '40':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 40000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '60':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 60000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '80':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 80000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '100':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 100000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '120':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 120000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '140':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 140000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '160':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 160000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)
        if call.data == '200':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.salary_from = 200000
            user.save()
            keyboard = types.InlineKeyboardMarkup()
            key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
            key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
            key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
            keyboard.add(key_3, key_5, key_7)
            bot.send_message(call.message.chat.id, 'Круто! Сколько вакансий в день ты хочешь получать?', reply_markup=keyboard)
            bot.register_next_step_handler(call.message, get_message_count)

        if call.data == '3':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.messages_count_per_day = 3
            user.save()
            bot.send_message(call.message.chat.id, 'Я знаю что тебе нужно! Уже совсем скоро я пришлю тебе подборку вакансий)')
        if call.data == '5':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.messages_count_per_day = 5
            user.save()
            bot.send_message(call.message.chat.id, 'Я знаю что тебе нужно! Уже совсем скоро я пришлю тебе подборку вакансий)')
        if call.data == '7':
            user = User.objects.get(tg_id=call.message.chat.id)
            user.messages_count_per_day = 7
            user.save()
            bot.send_message(call.message.chat.id, 'Я знаю что тебе нужно! Уже совсем скоро я пришлю тебе подборку вакансий)')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Давай)', callback_data='yes')
        keyboard.add(key_yes)
        bot.send_message(message.chat.id, 'Привет! Этот бот помогает найти работу. Я задам тебе несколько вопросов, чтобы быть максимально полезным. Начнем?', reply_markup=keyboard)

    def get_tags(message):
        keyboard = types.InlineKeyboardMarkup()
        key_20 = types.InlineKeyboardButton(text='20.000р', callback_data='20')
        key_40 = types.InlineKeyboardButton(text='40.000р', callback_data='40')
        key_60 = types.InlineKeyboardButton(text='60.000р', callback_data='60')
        key_80 = types.InlineKeyboardButton(text='80.000р', callback_data='80')
        key_100 = types.InlineKeyboardButton(text='100.000р', callback_data='100')
        key_120 = types.InlineKeyboardButton(text='120.000р', callback_data='120')
        key_140 = types.InlineKeyboardButton(text='140.000р', callback_data='140')
        key_160 = types.InlineKeyboardButton(text='160.000р', callback_data='160')
        key_200 = types.InlineKeyboardButton(text='200.000р', callback_data='200')
        keyboard.add(key_20, key_40, key_60, key_80, key_100, key_120, key_140, key_160, key_200)
        bot.send_message(message.chat.id, 'Выбери нижнюю границу зарплатных ожиданий', reply_markup=keyboard)
    
    def get_message_count(message):

        message_count_per_day = int(message.text)
        print(message_count_per_day)

        user = get_user_insance(message)
        user.messages_count_per_day = message_count_per_day
        user.save()

    bot.polling(none_stop=True, interval=0)

class Command(BaseCommand):
    help = 'Bot'

    def handle(self, *args, **options):
        start_bot()
        