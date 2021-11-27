import configparser
import random

import sqlalchemy as db
from sqlalchemy.orm import Session

from domain.entities import Item


class Repository(object):
    connection_string = "mysql://{user}:{password}@{host}/nuclear"

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        credentials = config['DB_CREDENTIALS']
        engine = db.create_engine(
            self.connection_string.format(user=credentials['user'],
                                          password=credentials['password'],
                                          host=credentials['host'])
        )
        self.session = Session(bind=engine)

    def query_get_random_item(self):
        items = self.session.query(Item)
        return random.choice([ob.as_dict() for ob in items])
