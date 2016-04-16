from tests.context import bookingsynclord
from bookingsynclord.entities import entity_generator
import unittest

class EntityTest(unittest.TestCase):

  def test_valid_entity_type(self):
    self.assertEqual(entity_generator("bookings"),bookingsynclord.entities.Booking.Booking)

  def test_unvalid_entity_type(self):
    self.assertIsNone(entity_generator("invalid"),bookingsynclord.entities.Booking.Booking)


if __name__ == '__main__':
    unittest.main()
