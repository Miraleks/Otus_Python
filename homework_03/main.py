from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from starlette import status
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


from api.items import router as items_router
from api.users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping")
def ping_page():
    return {
        "message": "pong"
    }

@app.get("/hello")
def hello_page():
    return {
        "message": "Now you on 'Hello' page",
    }


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    if isinstance(exception, StarletteHTTPException):
        return await http_exception_handler(request, exception)
    return JSONResponse(
        {
            "request url": request.url.path,
            "exception": str(exception),
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )


