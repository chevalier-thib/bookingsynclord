APIURL_ENDPOINT = "https://www.bookingsync.com/api/v3"
APIURL_TOKEN = "https://www.bookingsync.com/oauth/token"
REQUEST_DEFAULT_TIMEOUT=30
REQUESTED_SCOPE="bookings_write%20booking_read%20rentals_read%20rentals_read"
REDIRECT_URI="urn:ietf:wg:oauth:2.0:oob"



BOOKINGSYNC_ENDPOINT = {
    "rentals" : {"LIST"    : "/rentals"},
    "bookings" : {"LIST"   : "/bookings",
                  "GET"    : "/bookings/{id}",
                  "POST"   : "/rentals/{rental_id}/bookings",
                  "DELETE" : "/bookings/{id}",
                  "PUT"    : "/bookings/{id}"},
    "tests" : {"LIST" : "/tests",#UnitTest entity
               "GET" : "/test/{id}/",
               "PUT" : "/tests/{id}"},

}
