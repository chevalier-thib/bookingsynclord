from tests.context import bookingsynclord
from bookingsynclord.tools.CredentialManager import CredentialManager
from bookingsynclord import config

import unittest

class CredentialManagerTest(unittest.TestCase):

  def setUp(self):
    self.credential_manager = CredentialManager("","","")

  def test_generate_authorize_url(self):
    return_value = CredentialManager.generate_authorize_url("valid_client_id")
    exepted_url = "https://www.bookingsync.com/oauth/authorize?client_id=valid_client_id&redirect_uri={}&response_type=code&scope={}".format(config.REDIRECT_URI,
      config.REQUESTED_SCOPE)



if __name__ == '__main__':
    unittest.main()
