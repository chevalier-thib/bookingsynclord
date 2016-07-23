import Entity, Client, Booking, BookingComment, BookingFee, Rental, Source, Rate, Period, RateRule, RateTable,Season

def entity_generator(entity_type):
    """Return class element corresponding to Entity type."""
    types = Entity.Entity.__subclasses__()
    for class_e in types:
        if entity_type == class_e.ENTITY_TYPE:
            return class_e
