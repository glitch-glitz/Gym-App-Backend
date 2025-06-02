# contains classes acting as blueprints for post/patch methods

from pydantic import BaseModel

class MemberSchema(BaseModel):
    full_name: str
    weight: str
    passport: str
    subscription_id: int


class SubscriptionSchema(BaseModel)
    plan_name: str