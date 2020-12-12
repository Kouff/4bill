from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.routing import Route

from limiter import Limiter


@Limiter
class Request(HTTPEndpoint):
    async def get(self, request):
        return JSONResponse({'result': 'OK'})


async def http_exception(request, exc):
    return JSONResponse({"error": exc.detail}, status_code=exc.status_code)


exception_handlers = {
    HTTPException: http_exception
}
routes = [
    Route('/request/{amount:int}', Request),
]

app = Starlette(debug=True, routes=routes, exception_handlers=exception_handlers)
