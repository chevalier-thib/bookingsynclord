from abc import ABCMeta
import bookingsynclord.config
import requests
import logging
logger = logging.getLogger(__name__)

class GenericStore:
    """Abstract class with common properties for all Store."""
    __metaclass__ = ABCMeta

    def __init__(self,credential_manager,entity_type):
        self.credential_manager = credential_manager
        self.entity_type = entity_type

    @staticmethod
    def build_url(endpoint):
        """used to build url parameter of request done to API
        :param endpoint: endpoint details defined by BookingSync(for example /bookings to list booking)
        :type  endpoin : string or unicode

        :rtype: <string:absolute URL of the endpoint
        """
        return bookingsynclord.config.APIURL_ENDPOINT + endpoint

    @staticmethod
    def get_endpoint(entity,action):
        """Get the value of the endpoint for an entity/action.

        For example, to get the endpoint to list all bookings (/bookings)
        you would use this function with entity=BOOKING and action=LIST.

        All API endpoints usable are defined in the config.

        :param entity: bookingsync entity type
        :type  entity: string or unicode
        :param action: Action you intend to do (CREATE,LIST,GET)
        :type  action: String
        :rtype: <string:endpoint value>
        """

        return bookingsynclord.config.BOOKINGSYNC_ENDPOINT[entity][action]


    def get_request_bookingsync(self,url):
        """Send request to bookingSync and return Json format object.
        Pass the credential in the header.

        :param url: url to post request to.
        """
        headers = {'Authorization': 'Bearer {}'.format(self.credential_manager.access_token)}
        json_r = requests.get(url=url,headers=headers)
        json_r.raise_for_status()
        return json_r.text


    def list_json(self):
        """return json containing the result of list call.
        :rtype: dict / Json loaded object
        """
        logger.debug("Calling list_json for entity : {}".format(self.entity_type))
        endpoint = GenericStore.get_endpoint(self.entity_type,"LIST")
        url = GenericStore.build_url(endpoint)
        logger.debug("URL generated : {}".format(url))

        json = self.get_request_bookingsync(url)
        return json

    def get_json_by_id(self,id):
        """return a single element of entity in JSON format
        :param id: ID of the element queried
        :type  id: string or integer
        :rtype: dict / Json loaded object
        """
        logger.debug("Calling get_json_by_id for entity : {}".format(self.entity_type))
        endpoint = GenericStore.get_endpoint(self.entity_type,"GET")
        url = GenericStore.build_url(endpoint.format(id=str(id)))
        logger.debug("URL generated : {}".format(url))

        json = self.get_request_bookingsync(url)
        return json

