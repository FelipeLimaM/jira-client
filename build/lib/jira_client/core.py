"""Jira client core."""

import json
import logging
import urllib

import requests


LOGGER = logging.getLogger(__name__)


class JiraRestAPI:
    """Jira REST API."""
    # pylint: disable=too-few-public-methods

    _host = None
    _user = None
    _passwd = None

    def __init__(self, host=None, user=None, passwd=None):
        if host:
            self.host(host)
        if user:
            self._user = user
        if passwd:
            self._passwd = passwd

    @staticmethod
    def _join_url(start, end):
        if start and end:
            if end.startswith('/'):
                end = end[1:]
            return start + ('' if start.endswith('/') else '/') + end
        return start + end

    @staticmethod
    def _is_json(headers):
        if headers['Accept'] == 'application/json':
            return True
        return False

    @staticmethod
    def _json_headers():
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def _auth_request(self):
        if self._user and self._passwd:
            return requests.auth.HTTPBasicAuth(self._user, self._passwd)
        return None

    @staticmethod
    def _body_request(data):
        return json.dumps(data)

    def _raw_execution(self, method='GET', path=None, auth=None, headers=None, data=None):
        # pylint: disable=too-many-arguments
        headers = self._json_headers() if not headers else headers
        auth = self._auth_request() if not auth else auth
        if method == 'GET' and data:
            path = str(path) + '?' + urllib.parse.urlencode(data)
            data = None
        data = self._body_request(data) if isinstance(data, dict) else data
        response = requests.request(method, self._join_url(self._host, path), headers=headers, auth=auth, data=data)
        try:
            return response.ok, json.loads(response.text)
        except:
            return response.ok, response.raw

    @staticmethod
    def _mandatory_variable(kwargs_dict, variables):
        try:
            data = {key: kwargs_dict[key] for key in variables}
            return data
        except KeyError as error:
            raise KeyError(f'Variable {error} not found!') from None

    @staticmethod
    def _optional_variable(kwargs_dict, variables):
        data = {}
        try:
            data = {key: kwargs_dict[key] for key in kwargs_dict if key in variables}
        except KeyError:
            pass
        return data

    def host(self, host):
        """Setup and get the host URL."""
        self._host = self._join_url(host, '/rest/api/3/')
        return self._host
