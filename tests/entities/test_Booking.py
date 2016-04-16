from tests.context import bookingsynclord
from bookingsynclord.entities.Booking import Booking
import simplejson as json
from bookingsynclord import config
import datetime
import unittest

class BookingTest(unittest.TestCase):

  def setUp(self):
    self.booking_unav = Booking()
    self.booking_unav.start_at = datetime.datetime(2015,02,02,12,11,20).replace(microsecond=0).isoformat()
    self.booking_unav.end_at = datetime.datetime(2015,02,04,12,11,20).replace(microsecond=0).isoformat()
    self.booking_unav.unavailable = True
    self.booking_unav.rental_id = 10

  def test_json_serialize(self):
    json_booking = self.booking_unav._to_json()
    self.assertTrue("start_at" in json_booking)
    self.assertTrue("end_at" in json_booking)
    self.assertTrue("unavailable" in json_booking)
    self.assertTrue("rental_id" in json_booking)
    self.assertFalse("id" in json_booking)


  def test_json_serialize_list(self):
    json_booking = self.booking_unav._to_json_list()
    self.assertTrue("bookings" in json_booking)
    self.assertIs(type(json_booking['bookings']),list)


if __name__ == '__main__':
    unittest.main()
