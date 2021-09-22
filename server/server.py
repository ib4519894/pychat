from aiohttp import web

routes = web.RouteTableDef()

messages = []

@routes.post("/new-msg")
async def new_message(request):
    global messages
    sender = (await request.post())["sender"]
    content = (await request.post())["content"]
    print(f"""
{sender["username"]}:
     {content["body"]}
""")
    messages.append((sender, content))
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
