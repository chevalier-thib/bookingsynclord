from GenericStore import GenericStore


class BedroomStore(GenericStore):
    """Store used to manage Source entities.

    BookingSync doc : http://developers.bookingsync.com/reference/endpoints/bedrooms/
    """
    def __init__(self,credential_manager):
        super(BedroomStore, self).__init__(credential_manager, "bedrooms")
