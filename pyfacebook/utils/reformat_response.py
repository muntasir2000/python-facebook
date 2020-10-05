import json
from typing import Optional, Union, Dict


def replace_from_keyword_in_json(
        data, # type: Optional[Dict]
):
    # type: (...) -> Dict
    """
    Rename the 'from' field coming from the Graph API. As 'from' is a Python keyword, we cannot use this as an
    attribute with 'attrs' package. So renaming the 'from' field to 'object_creator'
    """
    json_str = json.dumps(data)
    replaced_json_str = json_str.replace('"from":', '"object_creator":')
    replaced_json_obj = json.loads(replaced_json_str)
    return replaced_json_obj
