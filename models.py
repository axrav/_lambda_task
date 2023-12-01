import re
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, validator


# define user model with validation
class User(BaseModel):
    user_id: UUID = Field(
        default_factory=uuid4
    )  # default value for user_id as uuid4
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
        pan_format = (
            "^[A-Z]{5}[0-9]{4}[A-Z]{1}$"  # regex for PAN number
        )
        if not value.isalnum() or not re.match(pan_format, value):
            raise ValueError("Invalid PAN number")
        return value
