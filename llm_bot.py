import telebot
from telebot import types
from model_wrapper import ModelWrapper


TOKEN = "..."
bot = telebot.TeleBot(TOKEN)

model_wrapper = ModelWrapper()


def main_menu():
    """Создает основное меню с кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.KeyboardButton("📜 Помощь"),
        types.KeyboardButton("🤖 Загрузить модель"),
        types.KeyboardButton("✅ Проверить модель"),
        types.KeyboardButton("✍ Генерировать текст")
    ]
    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Рада видеть тебя в моем боте для генерации шуток. "
        "Из названия уже понятно, что шутки могут быть обидными, нетолерантными, "
        "не совпадать с твоей жизненной позицией или вообще не получаться. "
        "Такова их специфика, и я за это ответственности не несу. "
        "Если ты с этим согласен, выбери действие ниже, и мы продолжим! 🚀",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda message: message.text == "📜 Помощь")
def help_command(message):
    help_message = """Доступны следующие команды:
📜 Помощь — список доступных команд
🤖 Загрузить модель — загрузка модели StatLM
✅ Проверить модель — посмотреть, загружен ли модель
✍ Генерировать текст — создать шутку по введенному контексту
"""
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(func=lambda message: message.text == "🤖 Загрузить модель")
def model_command(message):
    """Сразу загружаем StatLM без выбора"""
    bot.send_message(message.chat.id, "Загружаем модель StatLM... ⏳")
    
    if model_wrapper:
        status, result = model_wrapper.load("StatLM", test_inference=True)
        if status:
            bot.send_message(message.chat.id, "✅ StatLM успешно загружена!", reply_markup=main_menu())
        else:
            bot.send_message(message.chat.id, f"Ошибка загрузки модели:\n{result}")
    else:
        bot.send_message(message.chat.id, "Ошибка: модельный модуль не инициализирован.")


@bot.message_handler(func=lambda message: message.text == "✅ Проверить модель")
def check_model_command(message):
    if model_wrapper:
        bot.send_message(message.chat.id, f"Текущая модель: {str(model_wrapper.current_model_name)}")
    else:
        bot.send_message(message.chat.id, "Модель не загружена.")


@bot.message_handler(func=lambda message: message.text == "✍ Генерировать текст")
def generate_command(message):
    bot.send_message(message.chat.id, "Введите текст для генерации.")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Обработка текстовых сообщений (генерация)"""
    print(f'New message <{message.text}>')

    if model_wrapper:
        status, result = model_wrapper.generate(message.text)
        if status:
            bot.send_message(message.chat.id, result, reply_markup=main_menu())
        else:
            bot.send_message(message.chat.id, f"Ошибка генерации:\n{result}")
    else:
        bot.send_message(message.chat.id, "Ошибка: модельный модуль не инициализирован.")


bot.polling(none_stop=True, interval=0)
