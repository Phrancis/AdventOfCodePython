class Coordinates:
    """
    Represents a position's coordinates (latitude, longitude) relative to a starting point 
    where a positive latitude indicates North and negative indicates South,
    and a positive longitude indicates East and negative indicates West.
    """

    def __init__(self, latitude: int, longitude: int) -> "Coordinates":
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other: "Coordinates") -> bool:
        """
        Returns whether 2 Position instances are considered equal
        when using == operator.
        """
        return self.latitude == other.latitude and \
               self.longitude == other.longitude

    def __str__(self) -> str:
        """Returns a human-readable string representation."""
        return f"latitude:{self.latitude}, longitude:{self.longitude}"
