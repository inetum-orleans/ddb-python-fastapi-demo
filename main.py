from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

app = FastAPI(title="Test", description="test")

load_dotenv()

API_KEY = os.getenv("X_API_KEY")

header_scheme = APIKeyHeader(name="X-API-KEY")

async def validate_key(header_scheme: str = Depends(header_scheme)):
    if header_scheme == API_KEY:
        return True
    else:
        return False

@app.get("/")
def hello(is_key_valid: str = Depends(validate_key)):
    if is_key_valid is not True:
        raise HTTPException(status_code=401, detail="Your API key is incorrect.")
    
    return {"Message": "Hello world !"}
