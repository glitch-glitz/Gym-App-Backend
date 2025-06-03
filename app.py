from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload
from typing import List

from models import get_db, Member, Subscription
from schemas import (
    MemberSchema,
    MemberCreateSchema,
    SubscriptionSchema,
    SubscriptionCreateSchema,
)


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Welcome to my first backend app"}


@app.get("/member", response_model=List[MemberSchema])
def get_members(session: Session = Depends(get_db)):
    members = session.query(Member).options(joinedload(Member.subscriptions)).all()
    return members


@app.post("/member")
def add_member(member: MemberCreateSchema, session: Session = Depends(get_db)):
    try:
        new_member = Member(**member.dict())
        session.add(new_member)
        session.commit()
        session.refresh(new_member)  # to get updated id etc.
        return {"message": "Member added successfully", "id": new_member.id}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/member/{member_id}", response_model=MemberSchema)
def get_member(member_id: int, session: Session = Depends(get_db)):
    member = (
        session.query(Member)
        .options(joinedload(Member.subscriptions))
        .filter(Member.id == member_id)
        .first()
    )
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@app.patch("/member/{id}")
def update_member(id: int):
    print(f"Member of id {id} updated")
    return {"message": "Member updated successfully"}


@app.delete("/member/{id}")
def delete_member(id: int):
    print(f"Member of id {id} deleted")
    return {"message": "Member deleted successfully"}


@app.post("/subscription")
def add_subscription(
    subscription: SubscriptionCreateSchema, db: Session = Depends(get_db)
):
    try:
        new_subscription = Subscription(**subscription.dict())
        db.add(new_subscription)
        db.commit()
        db.refresh(new_subscription)
        return {
            "message": "Subscription created successfully",
            "id": new_subscription.id,
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/subscription", response_model=List[SubscriptionSchema])
def get_subscription(db: Session = Depends(get_db)):
    subscriptions = db.query(Subscription).all()
    return subscriptions
