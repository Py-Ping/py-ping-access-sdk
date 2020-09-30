import os
from pprint import pprint
from helpers import get_auth_session
from docker_generate import Container

from pingaccesssdk.apis.license import License
from pingaccesssdk.apis.key_pairs import KeyPairs
from pingaccesssdk.apis.acme import Acme
from pingaccesssdk.apis.engines import Engines
from pingaccesssdk.apis.auth import Auth
from pingaccesssdk.models.admin_basic_web_session_view import AdminBasicWebSessionView

home = os.environ["HOME"]
ping_user = os.environ["PING_IDENTITY_DEVOPS_USER"]
ping_key = os.environ["PING_IDENTITY_DEVOPS_KEY"]
endpoint = "https://localhost:9000/pa-admin-api/v3"
session = get_auth_session()
session.verify = False
session.auth = ('administrator', '2Access')

with Container(home, ping_user, ping_key) as container:
    version = __import__("pingaccesssdk.apis.version", fromlist=[""])
    response = version.Version(endpoint, session).versionCommand()
    print(f"Ping Access, version: {response.version}")

    license_obj = License(endpoint, session)

    pprint(license_obj.getLicenseCommand())

    keypairs = KeyPairs(endpoint, session)
    pprint(keypairs.keyAlgorithms())
    pprint(keypairs.getKeyPairsCommand(1, 10, '', '', '', ''))

    acme = Acme(endpoint, session)
    pprint(acme.getDefaultAcmeServerCommand())

    engines = Engines(endpoint, session)
    pprint(engines.getEnginesCommand(1, 10, '', '', '', ''))

    auth = Auth(endpoint, session)
    pprint(auth.getBasicAuthCommand())

    response = auth.getAdminBasicWebSessionCommand()
    print(type(response.to_dict()['cookieType']))
    pprint(response.to_dict())

    print(AdminBasicWebSessionView.from_dict(response.to_dict()))
