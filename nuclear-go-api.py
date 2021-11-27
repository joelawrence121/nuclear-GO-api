import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.client_json import GeocacheRequest
from service import item_service, image_service
from service.image_service import ImageService

app = FastAPI()
image_service = ImageService()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('chapi')


@app.post("/geocache")
async def get_image_blend(request: GeocacheRequest):
    try:
        # TODO
        # TODO get long,lat in viscinity
        item = item_service.get_random_item()
        # TODO get image of that location
        return image_service.get_blended_image(request.image)
    except RuntimeError as e:
        logger.warning(e)


if __name__ == "__main__":
    uvicorn.run("nuclear-go-api:app", host="127.0.0.1", port=5001, log_level="info", workers=1)
