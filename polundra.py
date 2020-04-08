import telebot
import parser
import polundra_markup as markup


TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['polundra'])
def start_handler(message):
    bot.send_message(
        message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот -- парсер хабра.',
                         reply_markup=markup.polundra_markup)
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')


bot.polling(none_stop=True)
