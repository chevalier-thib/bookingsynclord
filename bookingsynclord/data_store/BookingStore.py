from GenericStore import GenericStore

class BookingStore(GenericStore):
    """Store used to manage Bookings entities.

    http://developers.bookingsync.com/reference/endpoints/bookings/
    """

    def __init__(self,credential_manager):
        super(BookingStore, self).__init__(credential_manager,"BOOKING")
