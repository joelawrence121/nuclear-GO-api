import configparser
import uuid
from urllib.request import urlretrieve

import requests


class ImageService(object):
    radius = 100
    style_image = "fiery-wasteland"
    google_street_view_ep = "https://maps.googleapis.com/maps/api/streetview?location={lat},{long}&size=456x456&key={key}&radius={radius}"

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        credentials = config['DB_CREDENTIALS']
        self.ai_api_key = credentials['ai_api_key']
        self.google_api_key = credentials['google_api_key']

    def get_image_at(self, long, lat):
        r = requests.get(
            self.google_street_view_ep.format(lat=lat, long=long, radius=str(self.radius), key=self.google_api_key)
        )
        img_uuid = str(uuid.uuid4())
        with open("images/fetched/image" + img_uuid + ".jpg", 'wb') as img:
            img.write(r.content)
        return self.get_apocalyptic_image(img_uuid)

    def get_apocalyptic_image(self, img_uuid):
        r = requests.post(
            "https://api.deepai.org/api/fast-style-transfer",
            files={
                'content': open('images/fetched/image' + img_uuid + '.jpg', 'rb'),
                'style': open('service/images/' + self.style_image + '.jpg', 'rb'),
            },
            headers={'api-key': self.ai_api_key}
        )
        urlretrieve(r.json()['output_url'], "images/generated/image" + img_uuid + ".jpg")
        return r.json()
