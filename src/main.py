from fastapi import FastAPI
from api.router import router

app = FastAPI(title="Card Search API", version="1.0.0")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)