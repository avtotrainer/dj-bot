import os
import django
import telebot
from telebot import types

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot.settings')
django.setup()

from reservation.models import Person, PersonStatus, Role, BotSetting  # Импортируйте модели Django

bot_token = BotSetting.objects.get(name='telegram_bot_token').value
message_registred = BotSetting.objects.get(name='message_registred').value
message_registration = BotSetting.objects.get(name='message_registration').value
#bot = telebot.TeleBot("6785734167:AAENBclXa3ufO638knZoZh-xrHWhoE_24is")  # Замените на токен вашего бота
bot = telebot.TeleBot(bot_token)  # Замените на токен вашего бота

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = str(message.from_user.id)
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # Проверка, существует ли пользователь
    if not Person.objects.filter(user_id=user_id).exists():
        # Создание нового пользователя
        person = Person(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            name=f"{first_name} {last_name}"
        )
        person.save()
        bot.reply_to(message, message_registred)
    else:
        bot.reply_to(message, message_registration)

@bot.message_handler(commands=['status'])
def user_status(message):
    user_id = str(message.from_user.id)

    try:
        person = Person.objects.get(user_id=user_id)
        roles = ", ".join([role.name for role in person.roles.all()])  # Получение всех ролей пользователя
        status = person.person_status.status if person.person_status else "Не определен"  # Получение статуса пользователя

        response_message = f"Роли: {roles}\nСтатус: {status}"
    except Person.DoesNotExist:
        response_message = "Вы не зарегистрированы в системе."

    bot.reply_to(message, response_message)

@bot.message_handler(commands=['list_roles'])
def list_all_roles(message):
    roles = Role.objects.all()
    response = "Список всех ролей:\n"
    response += "\n".join([f"ID: {role.id}, Название: {role.name}" for role in roles])

    bot.reply_to(message, response)

@bot.message_handler(commands=['list_statuses'])
def list_all_statuses(message):
    statuses = PersonStatus.objects.all()
    response = "Список всех статусов:\n"
    response += "\n".join([f"ID: {status.id}, Статус: {status.status}" for status in statuses])

    bot.reply_to(message, response)

@bot.message_handler(commands=['button'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton("Нажми на меня")
    markup.add(button)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Нажми на меня":
        bot.reply_to(message, "Вы нажали на кнопку!")


@bot.message_handler(commands=['button_inline'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Нажми на меня", callback_data="test")
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Это тестовая кнопка:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "test":
        bot.answer_callback_query(callback_query_id=call.id, text="Вы нажали на кнопку!")
        bot.send_message(call.message.chat.id, "Вы выбрали 'Нажми на меня'")



bot.polling()
