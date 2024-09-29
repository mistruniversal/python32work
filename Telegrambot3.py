# import psycopg2
# import aiogram
# conn=psycopg2.connect(dbname='Person', user='postgres',password='user',host='127.0.0.1',port='5432')
# Bot=aiogram.Bot('8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M')



# import telebot
# import psycopg2
#
# # Подключение к базе данных PostgreSQL
# conn = psycopg2.connect(
#     dbname="person",
#     user="postgres",
#     password="user",
#     host="localhost"
# )
# cursor = conn.cursor()
#
# # Инициализация бота
# bot = telebot.TeleBot('8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M')
#
# # Обработчик команды /add для добавления человека
# @bot.message_handler(commands=['add'])
# def add_person(message):
#     msg = bot.send_message(message.chat.id, "Введите имя, фамилию и возраст через запятую:")
#     bot.register_next_step_handler(msg, process_add_command)
#
# def process_add_command(message):
#     try:
#         data = message.text.split(',')
#         first_name = data[0].strip()
#         last_name = data[1].strip()
#         age = int(data[2].strip())
#
#         cursor.execute('INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)', (first_name, last_name, age))
#         conn.commit()
#         bot.send_message(message.chat.id, f'{first_name} {last_name} добавлен в базу данных.')
#     except Exception as e:
#         bot.send_message(message.chat.id, "Ошибка при добавлении человека.")
#
#
# @bot.message_handler(commands=['show'])
# def show_people(message):
#     cursor.execute('SELECT * FROM person')
#     people = cursor.fetchall()
#     response = ''
#     if not people:
#         bot.send_message(message.chat.id, 'База данных пуста.')
#     else:
#         for person in people:
#             response += f"Имя: {person[1]}, Фамилия: {person[2]}, Возраст: {person[3]}\n"
#         bot.send_message(message.chat.id, response)
#
#
# # Обработчик команды /delete для удаления человека по ID
# @bot.message_handler(commands=['delete'])
# def delete_person(message):
#     msg = bot.send_message(message.chat.id, "Введите ID человека для удаления:")
#     bot.register_next_step_handler(msg, process_delete_command)
#
# def process_delete_command(message):
#     try:
#         person_id = int(message.text.strip())
#         cursor.execute('DELETE FROM person WHERE id = %s', (person_id,))
#         conn.commit()
#         bot.send_message(message.chat.id, f'Человек с ID {person_id} удален из базы данных.')
#     except Exception as e:
#         bot.send_message(message.chat.id, "Ошибка при удалении человека.")
#
# # Запуск бота
# bot.polling()







# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext, State, StatesGroup
# from aiogram.utils import executor
#
# API_TOKEN = '8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M'
#
# # Определяем состояния
# class Form(StatesGroup):
#     waiting_for_repeat = State()
#
# # Инициализация бота и диспетчера
# bot = Bot(API_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot)
#
# # Обработчик команды /start
# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer("Привет, пользователь!")
#
# # Обработчик команды /again
# @dp.message_handler(commands=['again'])
# async def again_command(message: types.Message):
#     await message.answer("Повторю за тобой:")
#     await Form.waiting_for_repeat.set()  # Переход в состояние ожидания
#
# # Обработчик для повторения сообщения
# @dp.message_handler(state=Form.waiting_for_repeat)
# async def repeat_message(message: types.Message, state: FSMContext):
#     user_message = message.text.strip()
#     await message.answer(f'Вы сказали: "{user_message}"')
#     await state.finish()  # Завершаем состояние
#
# # Запуск бота
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)










# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#
# # Замените на ваш токен
# API_TOKEN = '8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M'
#
# # Функция для обработки команды /start
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Привет, пользователь!")
#
# # Функция для обработки команды /again
# def again(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Повторю за тобой:")
#     context.user_data['waiting_for_repeat'] = True  # Устанавливаем флаг ожидания
#
# # Функция для обработки текстовых сообщений
# def repeat_message(update: Update, context: CallbackContext) -> None:
#     if context.user_data.get('waiting_for_repeat'):
#         user_message = update.message.text.strip()
#         update.message.reply_text(f'Вы сказали: "{user_message}"')
#         context.user_data['waiting_for_repeat'] = False  # Сбрасываем флаг ожидания
#
# def main() -> None:
#     # Создаем Updater и передаем ему токен вашего бота
#     updater = Updater('8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M')
#
#     # Получаем диспетчер для регистрации обработчиков
#     dispatcher = updater.dispatcher
#
#     # Регистрация обработчиков команд
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("again", again))
#
#     # Регистрация обработчика текстовых сообщений
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, repeat_message))
#
#     # Запускаем бота
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()










from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from create_bot import bot
from db_handler.db_funk import get_user_data
from keyboards.all_kb import main_kb, gender_kb
from my_anketa import Form

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        user_info = await get_user_data(user_id=message.from_user.id)

    if user_info:
        await message.answer('Привет. Я вижу, что ты зарегистрирован, а значит тебе можно '
                             'посмотреть, как выглядит твой профиль.', reply_markup=main_kb(message.from_user.id))
    else:
        await message.answer('Привет. Для начала выбери свой пол:', reply_markup=gender_kb())
        await state.set_state(Form.gender)