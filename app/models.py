from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    full_name: str
    mob_num: str
    pan_num: str

    @validator("mob_num")
    def validate_mob_num(cls, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid mobile number")
        return value

    @validator("pan_num")
    def validate_pan_num(cls, value):
        value = value.upper()
        pan_format = "^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
        if not value.isalnum() or not value.match(pan_format):
            raise ValueError("Invalid PAN number")
        return value
