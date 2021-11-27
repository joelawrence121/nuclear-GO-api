from pydantic import BaseModel


class GeocacheRequest(BaseModel):
    long: str
    lat: str
