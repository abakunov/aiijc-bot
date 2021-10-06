from django.core.management.base import BaseCommand

import telebot
from telebot import types
import re
from core.models import User, Position, Tag

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
            bot.send_message(call.message.chat.id, 'Отлично! Какие вакансии тебя интересуют? Напиши через запятую теги \n[ссылка на теги]')
            bot.register_next_step_handler(call.message, get_tags)

    @bot.message_handler(commands=['start'])
    def start_message(message):

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Давай)', callback_data='yes')
        keyboard.add(key_yes)

        bot.send_message(message.chat.id, 'Привет! Этот бот помогает найти работу. Я задам тебе несколько вопросов, чтобы быть максимально полезным. Начнем?', reply_markup=keyboard)


    def get_tags(message):

        tags = re.split('[^a-zа-яё]+', message.text.lower(), flags=re.IGNORECASE)
        print(tags)
        bot.send_message(message.from_user.id, 'Напиши нижнюю границу зарплатных ожиданий')
        bot.register_next_step_handler(message, get_salary_from)

        user = get_user_insance(message)
        for tag in tags:
            user.tags.add(Tag.objects.get(name=tag))
        user.save()

    def get_salary_from(message):
        
        salary_from = int(message.text)
        print(salary_from)
        bot.send_message(message.from_user.id, 'Сколько вакансий в день тебе присылать?')
        bot.register_next_step_handler(message, get_message_count)

        user = get_user_insance(message)
        user.salary_from = salary_from
        user.save()
    
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
        