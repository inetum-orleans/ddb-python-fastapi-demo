from fastapi import FastAPI

app = FastAPI(title="Test", description="test")

@app.get("/hello-world")
def hello():
    return {"Message": "Hello world !"}