from aiohttp import web
import time 

get_timestamp = time.time

routes = web.RouteTableDef()

messages = [
    {
        "sender":"Server",
        "content":"Welcome to pychat"
        }
    ]

@routes.post("/new-msg")
async def new_message(request):
    global messages
    data = (await request.post())
    sender = data["sender"]
    content = data["content"]
    print(sender)
    print(content)
    print(f"""
{sender}:
     {content}
""")
    messages.append(
        {
            "sender":sender,
            "content":content
        }
        )
    if len(messages) > 100:
        messages = messages[10:]

@routes.get("/get-msg")
async def get_message(request):
    data = {
        "messages":messages
    }
    return web.json_response(data)


app = web.Application()
app.add_routes(routes)

web.run_app(app, port=9999)
