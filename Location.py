import geoplotlib


class Location:
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        self.__longitude = longitude

    def visualize(self):
        geoplotlib.dot(
            {'lat': [self.latitude], 'lon': [self.longitude]},
            color='green',
            point_size=10)

        geoplotlib.show()

    def __str__(self):
        return "[{latitude:.3f}; {longitude:.3f}]" \
            .format(latitude=self.latitude, longitude=self.longitude)

    def __add__(self, other):
        return Location(self.latitude + other.latitude,
                        self.longitude + other.longitude)
