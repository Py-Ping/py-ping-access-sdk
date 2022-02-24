"""
overrides.py: class to handle
"""

import json
import json_delta


class IncorrectVersion(Exception):
    pass


class Override:
    def __init__(self, file_path, current_version):
        # 1. read the json file
        # 2. construct dictionary representing the delta
        # 3. track applicable version
        # 4. track applicable file

        self.current_version = current_version
        self.override_patch = json.loads(open(file_path).read())

    def apply_patch(self, api_json):
        if "apiVersion" in api_json and ".".join(api_json["apiVersion"].split(".")[0:2]) in api_json["apiVersion"]:
            return json_delta.patch(api_json, self.override_patch)
        raise IncorrectVersion
