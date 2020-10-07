import os
from pprint import pprint
from helpers import get_auth_session
from docker_generate import Container

from pingaccesssdk.apis.license import License
from pingaccesssdk.apis.key_pairs import KeyPairs
from pingaccesssdk.apis.acme import Acme
from pingaccesssdk.apis.engines import Engines
from pingaccesssdk.apis.auth import Auth
from pingaccesssdk.apis.virtualhosts import Virtualhosts
from pingaccesssdk.apis.applications import Applications
from pingaccesssdk.apis.sites import Sites
from pingaccesssdk.apis.https_listeners import HttpsListeners
from pingaccesssdk.models.admin_basic_web_session_view import AdminBasicWebSessionView
from pingaccesssdk.models.virtual_host_view import VirtualHostView
from pingaccesssdk.models.site_view import SiteView
from pingaccesssdk.models.application_view import ApplicationView
from pingaccesssdk.apis.agents import Agents
from pingaccesssdk.apis.config import Config
from pingaccesssdk.apis.users import Users
from pingaccesssdk.models.user_password_view import UserPasswordView
from pingaccesssdk.apis.web_sessions import WebSessions
from pingaccesssdk.models.hidden_field_view import HiddenFieldView
from pingaccesssdk.models.hidden_field_view import HiddenFieldView
from pingaccesssdk.models.o_auth_client_credentials_view import OAuthClientCredentialsView
from pingaccesssdk.models.web_session_view import WebSessionView


home = os.environ["HOME"]
ping_user = os.environ["PING_IDENTITY_DEVOPS_USER"]
ping_key = os.environ["PING_IDENTITY_DEVOPS_KEY"]
endpoint = "https://localhost:9000/pa-admin-api/v3"
session = get_auth_session()
session.verify = False
session.auth = ("administrator", "2Access")

with Container(home, ping_user, ping_key) as container:
    version = __import__("pingaccesssdk.apis.version", fromlist=[""])
    response = version.Version(endpoint, session).versionCommand()
    print(f"Ping Access, version: {response.version}")

    users = Users(endpoint, session)

    upv = UserPasswordView('2Access', '2AccessM0re')
    pprint(users.updateUserPasswordCommand('1', upv))

    session.auth = ("administrator", "2AccessM0re")

    license_obj = License(endpoint, session)

    pprint(license_obj.getLicenseCommand())

    keypairs = KeyPairs(endpoint, session)
    pprint(keypairs.keyAlgorithms())
    blah = keypairs.getKeyPairsCommand(1, 10, "", "", "", "")

    keypair = blah.items[0]
    keypairs.deleteKeyPairCommand(keypair.id)

    acme = Acme(endpoint, session)
    pprint(acme.getDefaultAcmeServerCommand())

    engines = Engines(endpoint, session)
    pprint(engines.getEnginesCommand(1, 10, "", "", "", ""))

    auth = Auth(endpoint, session)
    pprint(auth.getBasicAuthCommand())

    response = auth.getAdminBasicWebSessionCommand()
    print(type(response.to_dict()["cookieType"]))
    pprint(response.to_dict())

    print(AdminBasicWebSessionView.from_dict(response.to_dict()))

    agents = Agents(endpoint, session)
    print(agents.getAgentsCommand(1, 1, "", "", "", ""))

    virtual_host_ids = []
    virtual_host_view = VirtualHostView(host="test", port=443, agentResourceCacheTTL=900)
    virtual_host = Virtualhosts(endpoint, session).addVirtualHostCommand(virtual_host_view)
    virtual_host_ids.append(virtual_host.id)

    targets = ["pf-access.test.internal:80"]
    site_view = SiteView(name="PingFederate", targets=targets, secure=False)
    site = Sites(endpoint, session).addSiteCommand(site_view)

    application = Applications(endpoint, session)
    application_view = ApplicationView(
        agentId=0, contextRoot="/identity", defaultAuthType="API",
        name="test", siteId=site.id, spaSupportEnabled="true",
        virtualHostIds=virtual_host_ids, applicationType="Web", destination="Site"
    )
    print(application.addApplicationCommand(application_view))

    web_session = WebSessions(endpoint, session)
    client_secret = HiddenFieldView(encryptedValue="secret", value="secret")
    client_credentials = OAuthClientCredentialsView(clientId="esign-sgb-test",clientSecret=client_secret)
    web_session_view = WebSessionView(
        audience="esign-test",
        clientCredentials=client_credentials,
        failOnUnsupportedPreservationContentType=False,
        name="Test",
        webStorageType="SessionStorage",
        requestPreservationType="POST",
        sessionTimeoutInMinutes=3,
        pfsessionStateCacheInSeconds=60,
        sameSite="Lax",
        idleTimeoutInMinutes=3,
        pkceChallengeType="SHA256",
        cookieType="Encrypted",
        oidcLoginType="Code"
    )

    web_session.addWebSessionCommand(web_session_view)

    https_listeners = HttpsListeners(endpoint, session)
    https_listeners.getHttpsListenersCommand(sortKey="", order="")
