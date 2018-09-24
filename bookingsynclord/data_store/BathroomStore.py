from GenericStore import GenericStore


class BathroomStore(GenericStore):
    """Store used to manage Source entities.

    BookingSync doc : http://developers.bookingsync.com/reference/endpoints/bathrooms/
    """
    def __init__(self,credential_manager):
        super(BathroomStore, self).__init__(credential_manager, "bathrooms")
