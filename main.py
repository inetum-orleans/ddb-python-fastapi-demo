from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

app = FastAPI(title="Test", description="test")

# Configure your CORS using https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware

load_dotenv()

API_KEY = os.getenv("X_API_KEY")

async def validate_key(request_api_key: str):
    if request_api_key == API_KEY:
        return True
    else:
        return False


@app.middleware("http")
async def api_key_validator(request: Request, call_next):
    request_api_key = request.headers.get("X-API-KEY")

    is_key_valid = await validate_key(request_api_key)
    if not is_key_valid:
        return JSONResponse(
            status_code=401,
            content={"Message": "Your API key is incorrect."},
        )

    response = await call_next(request)

    return response


@app.get("/")
def hello():
    return {"Message": "Hello world !"}
