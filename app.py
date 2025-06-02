# import fastapi package
from fastapi import FastAPI

# initialize it
app = FastAPI()


# define routes
@app.get('/')
def index():
    return {"message": "Welcome to my first backend app"}

# member
# http://localhost:8000/member
@app.get('/member')
def member():
    # use sqlalchemy to retrieve all member from the db
    return[]

# http://localhost:8000/member
@app.post('/member')
def member():
    return{"message": "Member added successfully"}

# http://localhost:8000/member/3
@app.get('/member/{member_id}')
def get_member(member_id: int):
    print("Member id:", member_id)
    return {}

# http://localhost:8000/member/3
@app.patch('/member/{id}')
def get_member(id: int):
    print(f"product of id {id} updatedd")
    return {"message": "Member updated successfully"}

# http://localhost:8000/member/3
@app.delete('/member/{id}')
def get_member(id: int):
    print(f"Member of id {id} deleted")
    return {"message": "Member deleted successfully"}