from Entity import Entity


class Bedroom(Entity):
    ENTITY_TYPE = "bedrooms"
    """Represent a bedroom element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/bedrooms/
    """
    def __init__(self, id=None):
        return super(Bedroom, self).__init__("bedrooms", id)
