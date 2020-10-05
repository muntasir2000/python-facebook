import logging

import arrow

from pyfacebook import Api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FB_ACCESS_TOKEN = "1330160143827784|XNa7iu-8NuHjiHxta3PoFwD_05s"

graph_api = Api(long_term_token=FB_ACCESS_TOKEN, sleep_on_rate_limit=True)

def crawl_posts(page_id, since_timestamp, until_timestamp):
    posts = graph_api.get_page_posts(page_id=page_id, since_time=since_timestamp, until_time=until_timestamp,
                                     count=3,  return_json=False)
    for p in posts:
        print((p.object_creator.name))


crawl_posts('135237519825044', arrow.get("2020-10-01").timestamp, arrow.get('2020-10-03'))
