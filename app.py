# import fastapi package
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import get_db, Member, Base, Subscription

# initialize it
app = FastAPI()

# (*) allow network requests from all servers
app.add_middleware(CORSMiddleware, allow_origins=["*"])


# define routes
@app.get('/')
def index():
    return {"message": "Welcome to my first backend app"}

# member
# http://localhost:8000/member
@app.get('/member')
def member(session: Session = Depends(get_db)):
    # retrieves all products from the table
    members = session.query(Member).all()
    # subscriptions = session.query(Subscription).all()
    # subscriptions = session.query(Subscriptions).all()
    # use sqlalchemy to retrieve all member from the db
    return members

# http://localhost:8000/member
@app.post('/member')
def add_member():
    return{"message": "Member added successfully"}

# http://localhost:8000/member/3
@app.get('/member/{member_id}')
def get_member(member_id: int, session: Session = Depends(get_db)):
    print("Member id:", member_id)
    return {}

# http://localhost:8000/member/3
@app.patch('/member/{id}')
def update_member(id: int):
    print(f"product of id {id} updatedd")
    return {"message": "Member updated successfully"}

# http://localhost:8000/member/3
@app.delete('/member/{id}')
def delete_member(id: int):
    print(f"Member of id {id} deleted")
    return {"message": "Member deleted successfully"}