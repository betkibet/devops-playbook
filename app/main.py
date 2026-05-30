from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Trial 3 done"}

@app.post("/test")
def root():
    return {"message": "Trial 3 done"}