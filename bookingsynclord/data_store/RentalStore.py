from GenericStore import GenericStore

class RentalStore(GenericStore):
    def __init__(self,credential_manager):
        super(RentalStore, self).__init__(credential_manager,"RENTAL")
