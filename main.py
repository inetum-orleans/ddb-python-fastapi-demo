from fastapi import FastAPI
from api.middlewares.api_key import add_api_key_middleware
from api.routers import hello_world

app = FastAPI(
    title="ddb-python-fastapi-demo",
    description="Test Api for Python FastAPI with ddb",
)


# Configure your CORS using https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware

# add middlewares here
add_api_key_middleware(app)

# add routes here
app.include_router(hello_world.router)
