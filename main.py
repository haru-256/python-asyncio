import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(3, "hello"))
    task2 = asyncio.create_task(say_after(3, "world"))
    task3 = asyncio.create_task(say_after(3, "haru256"))
    await task1
    await task2
    await task3


if __name__ == "__main__":
    asyncio.run(main())
