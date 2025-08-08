from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cheri's Closet Backend Running"}
