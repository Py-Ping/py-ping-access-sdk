
from unittest import TestCase
from overrides import Override, IncorrectVersion


class TestOverrides(TestCase):
    def setUp(self):
        self.override = Override(delta_file_path="tests/overrides/test_api.delta", current_version="7.0.2.0")
        self.api_json = {
            "apiVersion": "7.0.2.0",
            "apis": [
                {
                    "operations": [
                        {
                            "parameters": [
                                {
                                    "allowMultiple": "false",
                                    "description": "Certificate to import",
                                    "name": "X509File",
                                    "paramType": "body",
                                    "required": "true",
                                    "type": "X509FileImportDocView"
                                }
                            ],
                            "summary": "Import a Certificate",
                            "type": "void"
                        }
                    ],
                    "path": "/test/path"
                }
            ]
        }

    def test_apply_patch(self):
        self.assertEqual(
            self.override.apply_patch(self.api_json),
            self.api_json
        )

    def test_apply_patch_incorrect_version(self):
        self.api_json["apiVersion"] = "6.3.3.0"
        with self.assertRaises(IncorrectVersion):
            self.override.apply_patch(self.api_json)
