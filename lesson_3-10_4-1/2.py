import asyncio
from asyncio.tasks import create_task


async def count_even_numbers(n: int) -> int:
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
        if i % 500_000 == 0:
            await asyncio.sleep(0.0001)

    print(len(result))


numbers = (100_000, 50_000_000, 1_000_000)

loop = asyncio.get_event_loop()
tasks = [count_even_numbers(i) for i in numbers]
loop.run_until_complete(asyncio.gather(*tasks))

# tasks = [
#     loop.create_task(count_even_numbers(100_000)),
#     loop.create_task(count_even_numbers(50_000_000)),
#     loop.create_task(count_even_numbers(1_000_000))
# ]
# loop.run_until_complete(asyncio.wait(tasks))