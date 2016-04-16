from tests.context import bookingsynclord
from bookingsynclord.data_store.BookingStore import BookingStore
from bookingsynclord import config
from datetime import datetime
import unittest

class BookingStoreTest(unittest.TestCase):
    def setUp(self):
        self.booking_store = BookingStore(None)

    def test_create_unavailable_booking(self):
        b = self.booking_store.create_unavailable_booking(10,datetime(2015,10,11,12,13,14),
            datetime(2015,10,14,10,10,10))

        self.assertEqual(b.start_at, '2015-10-11T12:13:14')
        self.assertEqual(b.end_at, '2015-10-14T10:10:10')
        self.assertTrue(b.unavailable)
        self.assertEqual(b.rental_id,10)

if __name__ == '__main__':
    unittest.main()
