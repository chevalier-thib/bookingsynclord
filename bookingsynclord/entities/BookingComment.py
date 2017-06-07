from Entity import Entity
class BookingComment(Entity):
    """Represent a BookingComment element.

    Documentation : http://developers.bookingsync.com/reference/endpoints/booking_comments/
    """
    ENTITY_TYPE = "bookings_comments"
    def __init__(self,id = None):
        return super(BookingComment,self).__init__("bookings_comments",id)

