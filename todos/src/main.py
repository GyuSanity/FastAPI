from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping" : "pong"}

#src 경로에서, uvicorn main:app --port 8000