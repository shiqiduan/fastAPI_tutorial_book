import requests
import time
import aiohttp, asyncio, time


def take_up_time(func):
    def wrapper(*args, **kwargs):
        print("Start to run --->")
        now = time.time()
        result = func(*args, **kwargs)
        cost = (time.time() - now) * 1000
        print("End to run. Cost time: {} ms".format(cost))
        return result

    return wrapper


def request_sync(url):
    response = requests.get(url)
    return response


async def request_async():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://www.baidu.com") as response:
            pass


@take_up_time
def run_sync():
    for i in range(0, 50):
        request_sync("http://www.baidu.com")


@take_up_time
def run_async():
    tasks = [asyncio.ensure_future(request_async()) for x in range(0, 49)]
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)


if __name__ == "__main__":
    run_sync()
    run_async()
