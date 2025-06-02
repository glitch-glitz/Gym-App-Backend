# import fastapi package
from fastapi import FastAPI

# initialize it
app = FastAPI()


# define routes
@app.get('/')
def index():
    return {"message": "Welcome to my first backend app"}
