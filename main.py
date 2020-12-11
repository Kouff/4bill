from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.routing import Route


class Request(HTTPEndpoint):
    async def get(self, request):
        return JSONResponse({'result': 'OK'})


routes = [
    Route('/request/{amount:int}', Request),
]

app = Starlette(debug=True, routes=routes)
