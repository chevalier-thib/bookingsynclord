APIURL_ENDPOINT = "https://www.bookingsync.com/api/v3"
APIURL_TOKEN = "https://www.bookingsync.com/oauth/token"
REQUEST_DEFAULT_TIMEOUT=30
REQUESTED_SCOPE="bookings_write%20booking_read%20rentals_read%20rentals_write%20clients_read%20clients_write%20rates_write%20rates_read%20rates_read%20clients_read%20clients_write"
REDIRECT_URI="urn:ietf:wg:oauth:2.0:oob"



BOOKINGSYNC_ENDPOINT = {
    "rentals" : {"LIST"    : "/rentals"},
    "bookings" : {"LIST"   : "/bookings",
                  "GET"    : "/bookings/{id}",
                  "POST"   : "/rentals/{rental_id}/bookings",
                  "DELETE" : "/bookings/{id}",
                  "PUT"    : "/bookings/{id}"},
    "sources"  : {"LIST"   : "/sources",
                  "GET"    : "/sources/{id}",
                  "POST"   : "/sources",
                  "PUT"    : "/sources/{id}"},
    "clients" :  {"LIST"   : "/clients",
                  "GET"    : "/clients/{id}",
                  "POST"   : "/clients",
                  "PUT"    : "/clients/{id}"},
    "booking_comments" :
                 {"LIST": "/booking_comments",
                  "GET"    : "/booking_comments/{id}",
                 },
    "booking_fees" :
                 {"LIST": "/bookings_fees",
                  "GET"    : "/bookings_fees/{id}",
                 },
    "tests" : {"LIST" : "/tests",#UnitTest entity
               "GET" : "/test/{id}/",
               "PUT" : "/tests/{id}"},

}
