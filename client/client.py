import aiohttp
import asyncio
from aioconsole import ainput, aprint

HOST = "localhost"
PORT = 9999
URL = f"http://{HOST}:{PORT}"
USERNAME = input("Enter your username > ")

async def get_messages(interval):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}/get-msg") as resp:
            data = eval(await resp.text())
            await aprint("\n" * 100)
            for message in data["messages"]:
                m = message["sender"]
                await aprint(m)
                await aprint(f"""     {message["content"]}""")
            
            await asyncio.sleep(interval)

async def send_messages():
    try:
        async with aiohttp.ClientSession() as session:
            new_message = (await ainput("> "))

            data = {
                "sender":{},
                "content":{}
            }
            data["sender"] = USERNAME
            data["content"] = new_message
            if data["content"]:
                await session.post(f"{URL}/new-msg", data=data)
    except:
        pass

async def main():
    while True:
        await get_messages(1)
        await send_messages()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
            