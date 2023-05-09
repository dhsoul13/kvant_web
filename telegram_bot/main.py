import telebot
from telebot import types
import json

data_news = json.load(open('./demo_db/index.json', encoding="UTF-8"))

bot = telebot.TeleBot('5898326650:AAHQEh_W50S-GufKZJBApnDf1vMJ0joADj8')


@bot.message_handler(commands=['start'])
def start(message):
    text = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nПиши /info, чтобы узнать об возможнотях бота'
    bot.send_message(
        message.chat.id, text, parse_mode="html")


@bot.message_handler(commands=['info'])
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    schedule = types.KeyboardButton('/schedule')
    info = types.KeyboardButton('/info')
    news = types.KeyboardButton('/news')
    contact = types.KeyboardButton('/contact')
    type = types.KeyboardButton('/type')
    markup.add(info, schedule, news, contact, type)

    text = f'Основные команды бота:\n/schedule - информация об расписании\n/contact - контакты\n/type - выбор темы\n/news - новости'
    bot.send_message(
        message.chat.id, text, parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=['schedule'])
def schedule(message):
    text = f"Группа: 1\nУчитель: Иванов Иван Иванович\nРасписание:\nкаждые вторник и пятница в 15:00 - 16:30\n\nГруппа: 2\nУчитель: Иванов Иван Иванович\nРасписание:\nкаждые понедельник и пятница в 15:00 - 16:30"
    bot.send_message(
        message.chat.id, text, parse_mode="html")


@bot.message_handler(commands=['contact'])
def contact(message):
    text = f"Учитель: Иван Иванович Иванов\nСсылки на контакты:"
    bot.send_message(
        message.chat.id, text, parse_mode="html")
    links = "https://github.com/dhsoul13"
    bot.send_message(
        message.chat.id, links, parse_mode="html")


@bot.message_handler(commands=['type'])
def type(message):
    markup = types.InlineKeyboardMarkup()

    seo = types.InlineKeyboardButton('SEO', callback_data="seo")
    frontend = types.InlineKeyboardButton('frontend', callback_data="frontend")
    backend = types.InlineKeyboardButton('backend', callback_data="backend")
    web_design = types.InlineKeyboardButton(
        'backend', callback_data="web-design")

    text = "Выбери тему для получения дополнительных ссылок с полезной информацией"
    markup.add(seo, frontend, backend, web_design)

    bot.send_message(
        message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['news'])
def news(message):

    markup = types.InlineKeyboardMarkup()

    learn = types.InlineKeyboardButton('learn', callback_data="learn")
    it = types.InlineKeyboardButton(
        'it', callback_data="it")

    text = "Выбери тему для получения дополнительных ссылок с полезной информацией"
    markup.add(learn, it)

    bot.send_message(
        message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == "seo":
        text = "https://habr.com/ru/articles/469139/"
        bot.send_message(callback.message.chat.id, text)
    elif callback.data == "frontend":
        text = "https://habr.com/ru/companies/otus/articles/674748/"
        bot.send_message(callback.message.chat.id, text)
    elif callback.data == "backend":
        text = "https://habr.com/ru/companies/ruvds/articles/488340/"
        bot.send_message(callback.message.chat.id, text)
    elif callback.data == "web-design":
        text = "https://habr.com/ru/companies/ruvds/articles/420617/"
        bot.send_message(callback.message.chat.id, text)
    elif callback.data == "learn":
        for infoElem in data_news:
            if infoElem['topic'] == 'learn':
                text = f"Новость об обучение:\n\n\n{json.dumps(infoElem['message'], ensure_ascii=False)}"
                bot.send_message(callback.message.chat.id, text)
    elif callback.data == "it":
        for infoElem in data_news:
            if infoElem['topic'] == 'it':
                text = f"Новость об обучение:\n\n\n{json.dumps(infoElem['message'], ensure_ascii=False)}"
                bot.send_message(callback.message.chat.id, text)


bot.polling(non_stop=True)
