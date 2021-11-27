from pydantic import BaseModel


class GenerateRequest(BaseModel):
    long: str
    lat: str
