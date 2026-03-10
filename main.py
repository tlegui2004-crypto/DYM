from fastapi import FastAPI

app = FastAPI()
app.title = "Hello My Api DyM"
@app.get("/")
def read_root():
    return {"Hello World"}