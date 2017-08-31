import Entity, Fee, RentalFee, Client, Payment, Booking, Review, BookingComment, BookingPayment, BookingFee, Rental, \
    Source, Rate, Period, RateRule, RateTable, Season, NightlyRateMap, Photo


def entity_generator(entity_type):
    """Return class element corresponding to Entity type."""
    types = Entity.Entity.__subclasses__()
    for class_e in types:
        if entity_type == class_e.ENTITY_TYPE:
            return class_e
