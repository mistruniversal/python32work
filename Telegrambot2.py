# import time
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
#
# API_TOKEN = '8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M'
# chat_id = 123
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# async def send_random_cat():
#     url = f'https://cataas.com/cat?t={time.time()}'
#     await bot.send_photo(chat_id, url)
#
# @dp.message_handler(commands="start")
# async def send_cat(message: types.Message):
#     await send_random_cat()
#     await message.reply('Cat has been sent')
#
# if __name__ == '__main__':
#     executor.start_polling(dp,skip_updates=True)
#
#
#
#
#
#
# # import time
# # from aiogram import Bot, Dispatcher, types
# # from aiogram import executor
# #
# # chat_id = 123 #замените на свое значение, подробнее ниже
# # bot = Bot('8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M')
# # dp=Dispatcher(bot)
# #
# #
# #
# # def send_random_cat():
# #     url = f'https://cataas.com/cat?t=${time.time()}'
# #     bot.send_photo(chat_id, url)
# #
# #
# # def main() -> None:
# #     send_random_cat()
# #     print('Cat has been sent')
# #
# #
# # if __name__ == "__main__":
# #     main()


















import requests
import datetime
# from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor


bot = Bot(token="8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Напиши город я покажу погоду")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={'8a48e94703ccbe939da5e899ff6ab714'}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                            f"***Хорошего дня!***"
                            )

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)















'8a48e94703ccbe939da5e899ff6ab714'
# import asyncio
# import logging
# import time
# import aiogram
# # from aiogram import Bot, Dispatcher, types
# # from aiogram.fi import Command
#
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = aiogram.Bot(token="7756383804:AAHcpfy2ht900bQokKFRQNwV-qiuX4RqbPY")
# # Диспетчер
# dp = aiogram.Dispatcher(bot)
# chat_id = 1271362249
#
#
# # Хэндлер на команду /start
# async def send_random_cat():
#     url = f'https://cataas.com/cat?t={time.time()}'
#     await bot.send_photo(chat_id, url)
# @dp.message_handler(commands='cat')
# async def command_send_cat(message: aiogram.types.Message):
#     await send_random_cat()
#     await message.reply('Cat has been sent')
#
#
# async def main():
#     await aiogram.Dispatcher(bot).start_polling(bot)
#
# if __name__ == "__main__":
#     aiogram.asyncio.run(main())



# "8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M"
# import asyncio
# import logging
# import time
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command
#
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token="8022034258:AAEv5Tw7P4NRyWSP93rAZ8hczAush1rub1M")
# # Диспетчер
# dp = Dispatcher()
# chat_id = 1271362249
#
#
# # Хэндлер на команду /start
# async def send_random_cat():
#     url = f'https://cataas.com/cat?t={time.time()}'
#     await bot.send_photo(chat_id, url)
# @dp.message(Command("cat"))
# async def command_send_cat(message: types.Message):
#     await send_random_cat()
#     await message.reply('Cat has been sent')
#
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())



