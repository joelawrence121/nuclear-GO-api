import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

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


@app.get("/item")
async def get_item():
    try:
        return item_service.get_random_item()
    except RuntimeError as e:
        logger.warning(e)


@app.post("/image")
async def get_image_blend(request: ImageRequest):
    try:
        return image_service.get_blended_image(request)
    except RuntimeError as e:
        logger.warning(e)


if __name__ == "__main__":
    uvicorn.run("nuclear-go-api:app", host="127.0.0.1", port=5000, log_level="info", workers=1)
