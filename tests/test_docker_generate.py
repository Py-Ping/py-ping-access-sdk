""" Tests for docker_generate.py """

from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from docker_generate import Container


class TestContainer(TestCase):
    """ Tests for the Container class """

    @patch("docker_generate.docker")
    @patch("docker_generate.logging")
    def setUp(self, logging_mock, docker_mock):
        self.logger = logging_mock.getLogger.return_value
        self.docker_mock = docker_mock
        self.container = Container("/home", "test-user", "test-pass")
        self.container.run()
        self.container.client.containers.run.assert_called_once_with(
            'pingidentity/pingaccess:edge',
            environment=[
                'PING_IDENTITY_ACCEPT_EULA=YES',
                'PING_IDENTITY_DEVOPS_USER=test-user',
                'PING_IDENTITY_DEVOPS_KEY=test-pass',
                'PING_IDENTITY_DEVOPS_HOME=/home/projects/devops',
                'PING_IDENTITY_DEVOPS_REGISTRY=docker.io/pingidentity',
                'PING_IDENTITY_DEVOPS_TAG=edge'
            ],
            name='pingaccess',
            ports={'443/tcp': 443, '9000/tcp': 9000},
            detach=True
        )

    def test_terminate(self):
        self.container.terminate()
        self.container.container.stop.assert_called_once_with()
        self.container.container.wait.assert_called_once_with()
        self.container.container.remove.assert_called_once_with()

    @patch("docker_generate.os.path.isfile")
    def test_get_by_image_name(self, isfile_mock):
        isfile_mock.return_value = False
        container_a = MagicMock()
        container_a.image.tags = ["penguin"]
        container_b = MagicMock()
        container_b.image.tags = ["pelican"]
        self.container.client.containers.list.return_value = [
            container_a, container_b
        ]
        self.assertEqual(
            self.container.get_by_image_name("pelican"),
            container_b
        )

    @patch("docker_generate.sleep")
    def test_wait(self, sleep_mock):
        self.container.container.status.return_value = "starting"
        container_a = MagicMock()
        container_a.status = "starting"
        container_b = MagicMock()
        container_b.status = "running"
        self.container.client.containers.get.side_effect = [container_a, container_b]
        self.container.wait()
        sleep_mock.assert_has_calls([call(5), call(5)])
        self.container.client.containers.get.assert_has_calls([
            call(self.docker_mock.from_env.return_value.containers.run.return_value.id),
            call(container_a.id)
        ])
