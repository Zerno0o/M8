import telebot
from bot_logic import   # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("токен")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Здесь вы можете узнать что такое глобальное потепление, почему оно может начаться, как уменьшить вероятность появления глобального потепления ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file) 
    cat = classify_cat(message)
    if cat == 'Настоящиe':
        bot.reply_to(message, "Вы проходите на конкурс")
    if cat == 'Сгенерированные':
        bot.reply_to(message,"Вы не проходите на конкурс")
    else:
        bot.reply_to(message, 'Произошла ошибка')
# Запускаем бота
bot.polling()
