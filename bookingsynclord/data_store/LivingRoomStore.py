from GenericStore import GenericStore


class LivingRoomStore(GenericStore):
    """Store used to manage Source entities.

    BookingSync doc : http://developers.bookingsync.com/reference/endpoints/living_rooms/
    """
    def __init__(self,credential_manager):
        super(LivingRoomStore, self).__init__(credential_manager, "living_rooms")
