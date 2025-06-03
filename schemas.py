# contains classes acting as blueprints for post/patch methods

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MemberSchema(BaseModel):
    full_name: str
    weight: str
    passport: str
    subscription_id: int


class SubscriptionSchema(BaseModel):
    plan_name: str
    member_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    is_active: bool