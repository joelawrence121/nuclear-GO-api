from pydantic import BaseModel


class GeocacheRequest(BaseModel):
    long: str
    lat: str


class Item:
    def __init__(self):
        # TODO define item object
        pass


class GeocacheResponse:

    def __init__(self, long: str, lat: str, item: Item, image_url: str):
        self.long = long
        self.lat = lat
        self.item = item
        self.image_url = image_url
