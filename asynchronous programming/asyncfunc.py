import asyncio
import time

async def wait(sleeptime):
    time.sleep(sleeptime)


async def fetch_data(id, sleeptime):
    print("fetching data..., id:", id)
    await wait(sleeptime)
    # await asyncio.sleep(sleeptime)  # simulate an I/O operation with a sleep
    print("Data fetched id: ", id)
    return {"data": "Some Data", "id": id}


async def main():
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 10))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)


asyncio.run(main())