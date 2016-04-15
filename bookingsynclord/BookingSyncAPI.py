import config
import logging
import tools
from data_store.RentalStore import RentalStore
from data_store.BookingStore import BookingStore

logger = logging.getLogger(__name__)

class BookingSyncAPI:
    def __init__(self,client_id,client_secret,access_token,refresh_token=None):
        self.credential_manager = tools.CredentialManager.CredentialManager(client_id,client_secret,access_token,refresh_token)
        self.rentals_store = RentalStore(self.credential_manager)
        self.booking_store = BookingStore(self.credential_manager)