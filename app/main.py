from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
while True:
        
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='4133', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to Database failed")
        print("Error: ", error)
        time.sleep(2)
    
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2 }]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
        
        
def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "welcome to my api????"}


    