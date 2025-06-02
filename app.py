# import fastapi package
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import get_db, Member, Base, Subscription
from schemas import MemberSchema, SubscriptionSchema

# initialize it
app = FastAPI()

# (*) allow network requests from all servers
app.add_middleware(CORSMiddleware, allow_origins=["*"])


# define routes
@app.get("/")
def index():
    return {"message": "Welcome to my first backend app"}


# member
# http://localhost:8000/member
@app.get("/member")
def member(session: Session = Depends(get_db)):
    # retrieves all products from the table
    members = session.query(Member).all()
    # subscriptions = session.query(Subscription).all()
    # subscriptions = session.query(Subscriptions).all()
    # use sqlalchemy to retrieve all member from the db
    return members


# http://localhost:8000/member
@app.post("/member")
def add_member(member: MemberSchema, session=Depends(get_db)):
    # 1. create and instance of the member model with the values sent
    #   new_member =  Member(
    #         name = member.name, weight = member.weight,
    #         passport = member.passport,
    #         subscription_id = member.subscription_id
    #     )
    try:
        new_member = Member(**member.model_dump())
        #    2. add the member the transaction
        session.add(new_member)
        # 3. commit the transaction
        session.commit()
        return {"message": "Member added successfully", "id": new_member.id}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


# http://localhost:8000/member/3
@app.get("/member/{member_id}")
def get_member(member_id: int, session: Session = Depends(get_db)):
    print("Member id:", member_id)
    return {}


# http://localhost:8000/member/3
@app.patch("/member/{id}")
def update_member(id: int):
    print(f"product of id {id} updatedd")
    return {"message": "Member updated successfully"}


# http://localhost:8000/member/3
@app.delete("/member/{id}")
def delete_member(id: int):
    print(f"Member of id {id} deleted")
    return {"message": "Member deleted successfully"}


# subscription
@app.post("/suscription")
def add_subscription(subscription: SubscriptionSchema, db: Session = Depends(get_db)):
    new_subscrption = Subscription(**subscription.model_dump())

    db.add(new_subscrption)

    db.commit()

    return {"message": "Subscription created successfully"}
