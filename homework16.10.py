
import asyncio


# async def fetch_data():
#     await asyncio.sleep(1)
#     return "Данные загружены"








async def fetch_data_1():
    data = await fetch_data()
    print("fetch_data_1:", data)
    return data

async def fetch_data_2():
    data = await fetch_data()
    print("fetch_data_2:", data)
    return data

async def main():
    results = await asyncio.gather(fetch_data_1(), fetch_data_2())
    print("Результаты:", results)


asyncio.run(main())









# import aiohttp
#
# async def fetch_api_data():
#     url = "https://jsonplaceholder.typicode.com/todos/1"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             print("Данные API:", data)
#             return data
#
#
# asyncio.run(fetch_api_data())