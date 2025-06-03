# contains classes acting as blueprints for post/patch methods

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# class MemberSchema(BaseModel):
#     full_name: str
#     weight: str
#     passport: str
#     subscription_id: int


# class SubscriptionSchema(BaseModel):
#     plan_name: str
#     member_id: int
#     start_date: datetime
#     end_date: Optional[datetime] = None
#     is_active: bool

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


# For creating/updating members (input)
class MemberCreateSchema(BaseModel):
    full_name: str
    weight: Optional[float] = None
    passport: Optional[str] = None
    subscription_id: int


# For creating/updating subscriptions (input)
class SubscriptionCreateSchema(BaseModel):
    plan_name: str
    member_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool



class SubscriptionSchema(BaseModel):
    id: int
    plan_name: str
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True


class MemberSchema(BaseModel):
    id: int
    full_name: str
    weight: Optional[float] = None
    passport: Optional[str] = None
    bmi: Optional[float] = None
    created_at: datetime
    subscriptions: Optional[List[SubscriptionSchema]] = None  

    class Config:
        orm_mode = True
