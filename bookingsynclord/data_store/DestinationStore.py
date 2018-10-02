from GenericStore import GenericStore

class DestinationStore(GenericStore):
    """Store used to manage BookingFee entities.

    BookingSync doc :     Documentation : http://developers.bookingsync.com/reference/endpoints/destinations/
    """
    def __init__(self,credential_manager):
        super(DestinationStore, self).__init__(credential_manager, "destinations")
