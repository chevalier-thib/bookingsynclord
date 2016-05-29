from Entity import Entity
class BookingFee(Entity):
    """Represent a BookingFee element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/bookings_fees/
    """
    ENTITY_TYPE = "booking_fees"
    def __init__(self,id = None):
        return super(BookingFee,self).__init__("booking_fees",id)
