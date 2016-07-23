import config
import logging
from tools.CredentialManager import CredentialManager
from data_store.RentalStore import RentalStore
from data_store.BookingStore import BookingStore
from data_store.SourceStore import SourceStore
from data_store.BookingCommentStore import BookingCommentStore
from data_store.BookingFeeStore import BookingFeeStore
from data_store.ClientStore import ClientStore
from data_store.PeriodStore import PeriodStore
from data_store.RateStore import RateStore
from data_store.RateTableStore import RateTableStore
from data_store.RateRuleStore import RateRuleStore
from data_store.SeasonStore import SeasonStore

logger = logging.getLogger(__name__)

class BookingSyncAPI:
    def __init__(self,client_id,client_secret,access_token,refresh_token=None):
        self.credential_manager = CredentialManager(client_id,client_secret,access_token,refresh_token)
        self.rentals_store = RentalStore(self.credential_manager)
        self.booking_store = BookingStore(self.credential_manager)
        self.source_store = SourceStore(self.credential_manager)
        self.booking_comment_store = BookingCommentStore(self.credential_manager)
        self.booking_fee_store = BookingFeeStore(self.credential_manager)
        self.client_store = ClientStore(self.credential_manager)
        self.rate_store = RateStore(self.credential_manager)
        self.period_store = PeriodStore(self.credential_manager)
        self.rate_rule_store = RateRuleStore(self.credential_manager)
        self.rate_table_store = RateTableStore(self.credential_manager)
        self.season_store = SeasonStore(self.credential_manager)
