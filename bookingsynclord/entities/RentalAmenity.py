from Entity import Entity


class RentalAmenitie(Entity):
    ENTITY_TYPE = "rental_amenities"
    """Represent a Rental Amenitie element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/rentals_amenities/
    """
    def __init__(self, id=None):
        return super(RentalAmenitie, self).__init__("rental_amenities", id)
