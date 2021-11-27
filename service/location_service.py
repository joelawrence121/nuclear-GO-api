import math
import random


class LocationService(object):

    def __init__(self):
        self.radius = 10000

    def get_location(self, latitude: float, longitude: float):
        r = self.radius / 111300
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = r * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)

        return latitude + x, longitude + y
