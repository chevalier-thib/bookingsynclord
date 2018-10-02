from Entity import Entity
class Destination(Entity):
    """Represent a Destination element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/destinations/
    """
    ENTITY_TYPE = "destinations"
    def __init__(self,id = None):
        return super(Payment, self).__init__("destinations",id)

