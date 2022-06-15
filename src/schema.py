from pydantic import BaseModel, validator, constr
from typing import Optional
import validators

class URLvalidate(BaseModel):
    long_url: str = None
    custom: Optional[constr(max_length = 5)] = None

    @validator('long_url')
    def validate(cls, v):
        if not validators.url(v['long_url']):
            raise ValueError("URL entered is not valid")
        return v
