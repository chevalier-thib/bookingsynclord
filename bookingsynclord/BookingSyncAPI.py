import config
import logging
from tools.CredentialManager import CredentialManager
from data_store.RentalStore import RentalStore
from data_store.BookingStore import BookingStore
from data_store.SourceStore import SourceStore

logger = logging.getLogger(__name__)

class BookingSyncAPI:
    def __init__(self,client_id,client_secret,access_token,refresh_token=None):
        self.credential_manager = CredentialManager(client_id,client_secret,access_token,refresh_token)
        self.rentals_store = RentalStore(self.credential_manager)
        self.booking_store = BookingStore(self.credential_manager)
        self.source_store = SourceStore(self.credential_manager)
