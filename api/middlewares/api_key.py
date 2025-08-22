from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from starlette.middleware.base import BaseHTTPMiddleware

load_dotenv()

API_KEY = os.getenv("X_API_KEY")


async def validate_key(request_api_key: str):
    if request_api_key == API_KEY:
        return True
    else:
        return False


# APIKeyValidator is a child of BaseHTTPMiddleware
class APIKeyValidator(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow OPTIONS preflight requests to pass through
        if request.method == "OPTIONS":
            response = await call_next(request)
            return response

        request_api_key = request.headers.get("X-API-KEY")

        is_key_valid = await validate_key(request_api_key)
        if not is_key_valid:
            return JSONResponse(
                status_code=401,
                content={"Message": "Your API key is incorrect."},
            )

        response = await call_next(request)
        return response


def add_api_key_middleware(app: FastAPI):
    app.add_middleware(APIKeyValidator)
