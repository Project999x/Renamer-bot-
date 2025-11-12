from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({
        "status": "success",
    })


@routes.get("/health")
async def health_check(request):
    return web.json_response({"status": "ok", "uptime": "💤 alive"})
