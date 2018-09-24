from Entity import Entity


class ChangeOver(Entity):
    ENTITY_TYPE = "change_overs"
    """Represent a bedroom element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/change_overs/
    """
    def __init__(self, id=None):
        return super(ChangeOver, self).__init__("change_overs", id)
