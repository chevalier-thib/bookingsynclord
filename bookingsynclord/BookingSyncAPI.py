import config
import logger
logger = logging.getLogger(__name__)

class BookingSyncAPI:
    def __init__(self,client_id,client_secret,access_token,refresh_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token

    def use_refresh_token(self,refresh_token):
        """Send a POST request using the refresh_token and
        generate a new access token.
        Set the current access_token to the new token
        and return new access_token and refresh_token
        :param refresh_token: oAuth refresh_token
        :type  refresh_token: unicode or string

        :rtype: (<String:new_access_token>,<String:new_refresh_token)>
        """
        url_request = config.APIU_ENDPOINT + config.APIURL_REFRESH_TOKEN

        refresh_param="client_id={}&client_secret={}&refresh_token={}&expires_in=1234&grant_type=refresh_token&redirect_uri=urn:ietf:wg:oauth:2.0:oob".format(self.client_id,self.client_secret, refresh_token)
        r = request.post(url_request,params=refresh_param,timeout=config.REQUEST_DEFAULT_TIMEOUT)
        json_response = r.json()
        refresh_token = json_response["refresh_token"]
        access_token = json_response["access_token"]
        self.access_token = access_token
        self.refresh_token = refresh_token
        return access_token,refresh_token


    def roll_token(self):
        """Call refresh_token method with currently
        set refresh_token

        :rtype: (<String:new_access_token>,<String:new_refresh_token)>
        """
        if self.refresh_token is not None:
            return self.refresh_token()
        else:
            raise LookupError('No refresh_token set')

    def generate_authorize_url(self):
        """Print and return URL link used to request authorization
        for an account.
        By default, it will request scope set in the config.
        """
        url = """https://www.bookingsync.com/oauth/authorize?
        client_id={}
        &redirect_uri={}
        &response_type=code
        &scope={}
        """.format(self.client_id,config.REDIRECT_URI,config.REQUESTED_SCOPE)
        print url
        return url
