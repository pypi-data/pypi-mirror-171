"""
tests.ipify.ipify
~~~~~~~~~~~~~~~~~

All tests for our ipify.ipify module.
"""

from socket import AF_INET, AF_INET6, inet_pton
from unittest import TestCase

from requests.models import Response

from ipify.exceptions import ConnectionError, IpifyException, ServiceError
from ipify.ipify import _get_ip_resp, get_ip


class BaseTest(TestCase):
    """A base test class."""

    def setUp(self):
        import ipify
        self._api_uri = ipify.ipify.API_URI

    def tearDown(self):
        import ipify
        ipify.ipify.API_URI = self._api_uri


class GetIpRespTest(BaseTest):
    """Tests for our helper function: ``_get_ip_resp``."""

    def test_returns_response(self):
        self.assertIsInstance(_get_ip_resp(), Response)


class GetIpTest(BaseTest):
    """Tests for our ``get_ip`` function."""

    def test_raises_connection_error_on_connection_error(self):
        import ipify

        ipify.ipify.API_URI = 'https://api.asdgasggasgdasgdsasgdasdfadfsda.com'
        self.assertRaises(ConnectionError, get_ip)

    def test_raises_ipify_exception_on_error(self):
        import ipify

        ipify.ipify.API_URI = 'https://api.asdgasggasgdasgdsasgdasdfadfsds.com'
        self.assertRaises(IpifyException, get_ip)

    def test_raises_service_error_on_error(self):
        import ipify

        ipify.ipify.API_URI = 'https://api.ipify.org/woo'
        self.assertRaises(ServiceError, get_ip)

    def test_returns_ip_address(self):
        from ipify import get_ip

        def is_valid_ip(ip):
            # IPv4
            try:
                inet_pton(AF_INET, ip)
                return True
            except OSError:
                pass

            # IPv6
            try:
                inet_pton(AF_INET6, ip)
                return True
            except OSError:
                pass

            return False

        self.assertTrue(is_valid_ip(get_ip()))
