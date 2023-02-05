import geopy.distance


class GeoCalculator:

    @staticmethod
    def get_distance_km(point_a: tuple[float, float], point_b: tuple[float, float]) -> float:
        """Calculate distance in kilometers between two points.

        Args:
            point_a (tuple[float, float]): of format (lat, lon)
            point_b (tuple[float, float]): of format (lat, lon)

        Returns:
            float: distance in kilometers
        """
        return geopy.distance.geodesic(point_a, point_b).km
