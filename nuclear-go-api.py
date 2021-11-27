import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.client_json import GenerateRequest
from service import image_service
from service.image_service import ImageService
from service.location_service import LocationService

app = FastAPI()
image_service = ImageService()
location_service = LocationService()

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


@app.post("/generate")
async def get_image_blend(request: GenerateRequest):
    try:
        lat, long = location_service.get_location(float(request.lat), float(request.long))
        return image_service.get_image_at(long, lat)
    except RuntimeError as e:
        logger.warning(e)


if __name__ == "__main__":
    uvicorn.run("nuclear-go-api:app", host="127.0.0.1", port=5001, log_level="info", workers=1)
