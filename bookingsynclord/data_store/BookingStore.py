from GenericStore import GenericStore

class BookingStore(GenericStore):
    def __init__(self,credential_manager):
        super(RentalStore, self).__init__(credential_manager,"BOOKING")
