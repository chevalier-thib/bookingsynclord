from GenericStore import GenericStore


class ChangeOverStore(GenericStore):
    """Store used to manage Source entities.

    BookingSync doc : http://developers.bookingsync.com/reference/endpoints/change_overs/
    """
    def __init__(self,credential_manager):
        super(ChangeOverStore, self).__init__(credential_manager, "change_overs")
