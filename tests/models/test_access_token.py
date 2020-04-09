import json
import unittest

import pyfacebook.models as models


class AccessTokenModelTest(unittest.TestCase):
    BASE_PATH = "testdata/models/access_token/"

    with open(BASE_PATH + 'auth_access_token_info.json', 'rb') as f:
        AUTH_ACCESS_TOKEN = json.loads(f.read().decode('utf-8'))
    with open(BASE_PATH + 'access_token_info.json', 'rb') as f:
        ACCESS_TOKEN_CORRECT = json.loads(f.read().decode('utf-8'))
    with open(BASE_PATH + 'access_token_error.json', 'rb') as f:
        ACCESS_TOKEN_WRONG = json.loads(f.read().decode('utf-8'))

    def testAuthAccessToken(self) -> None:
        m: models.AuthAccessToken = models.AuthAccessToken.new_from_json_dict(self.AUTH_ACCESS_TOKEN)

        self.assertEqual(m.access_token, "access_token")
        self.assertEqual(m.expires_in, 3600)

    def testCorrectAccessToken(self) -> None:
        m: models.AccessToken = models.AccessToken.new_from_json_dict(self.ACCESS_TOKEN_CORRECT)

        self.assertEqual(m.app_id, "1234567890")
        self.assertIsNone(m.metadata)
        self.assertEqual(len(m.scopes), 8)
        self.assertEqual(m.scopes[0], "email")
        self.assertEqual(len(m.granular_scopes), 5)
        self.assertEqual(m.granular_scopes[0].scope, "manage_pages")
        self.assertEqual(m.granular_scopes[3].target_ids[0], "123456789")
        self.assertEqual(
            repr(m),
            "AccessToken(app_id=1234567890,application=FacebookApp,type=USER)"
        )

    def testWrongAccessToken(self) -> None:
        m: models.AccessToken = models.AccessToken.new_from_json_dict(self.ACCESS_TOKEN_WRONG)

        self.assertEqual(m.error.code, 190)
        self.assertEqual(m.is_valid, False)
        self.assertEqual(
            repr(m),
            "AccessToken(Error(code=190,message=The access token could not be decrypted))"
        )
