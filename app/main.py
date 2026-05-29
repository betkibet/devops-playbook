from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Trial 1 done"}