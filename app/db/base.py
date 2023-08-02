from datetime import datetime
from pydantic import BaseModel, validator

class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """
    is_active: bool

class DateTimeModelMixin(BaseModel):
    created_at: datetime
    updated_at: datetime


    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.datetime.now()

class IDModelMixin(BaseModel):
    id: int
