from Entity import Entity


class LivingRoom(Entity):
    ENTITY_TYPE = "living_rooms"
    """Represent a bedroom element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/living_stores/
    """
    def __init__(self, id=None):
        return super(LivingRoom, self).__init__("living_rooms", id)
