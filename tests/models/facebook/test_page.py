import json
import unittest

import pyfacebook.models as models


class PageModelTest(unittest.TestCase):
    BASE_PATH = "testdata/models/facebook/"

    with open(BASE_PATH + 'page_info.json', 'rb') as f:
        PAGE_INFO = json.loads(f.read().decode('utf-8'))

    def testPage(self) -> None:
        m: models.Page = models.Page.new_from_json_dict(self.PAGE_INFO)

        self.assertEqual(m.id, "20531316728")
        self.assertEqual(m.can_checkin, True)
        self.assertEqual(len(m.category_list), 2)
        self.assertEqual(m.category_list[0].id, "2202")
        self.assertEqual(m.cover.id, "10159027219496729")
        self.assertEqual(m.engagement.count, 214840680)
        self.assertEqual(m.picture.width, 50)
        self.assertEqual(m.start_info.date.year, 2004)
        self.assertIsNone(m.whatsapp_number)
