APIURL_ENDPOINT = "https://www.bookingsync.com/api/v3"
APIURL_TOKEN = "https://www.bookingsync.com/oauth/token"
REQUEST_DEFAULT_TIMEOUT=30
REQUESTED_SCOPE="bookings_write%20rentals_read%20rentals_read"
REDIRECT_URI="urn:ietf:wg:oauth:2.0:oob"



BOOKINGSYNC_ENDPOINT = {
    "RENTAL" : {"LIST" : "/rentals"},
    "BOOKING" : {"LIST" : "/bookings", "GET" : "/bookings/{id}/"},
    "TEST" : {"LIST" : "/tests", "GET" : "/test/{id}/"}, #UnitTest entity

}
