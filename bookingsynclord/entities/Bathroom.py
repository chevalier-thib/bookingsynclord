from Entity import Entity


class Bathroom(Entity):
    ENTITY_TYPE = "bathrooms"
    """Represent a bedroom element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/bathrooms/
    """
    def __init__(self, id=None):
        return super(Bathroom, self).__init__("bathrooms", id)
