from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Trial 2 done"}