"""REST API Client for Jira."""

import logging

from .core import JiraRestAPI
from .utils import get_if_exists


LOGGER = logging.getLogger(__name__)


class JiraClient(JiraRestAPI):
    """Interface to communicate with Jira."""

    def create_field(self, **kwargs):
        """
            Creates a new field.
            {
                "searcherKey": "plugin.CustomFieldTypes.EXAMPLE",
                "name": "example",
                "description": "Custom field",
                "type": "plugin.CustomFieldTypesSearcher.EXAMPLE"
            }
        """
        data = self._mandatory_variable(kwargs, ['name', 'type', 'searcherKey'])
        data.update(self._optional_variable(kwargs, ['description']))
        if 'unique' in kwargs and kwargs.get('unique') is True:
            verification = get_if_exists(self.search_field(query=data['name'])[1]['values'], 'name', data['name'])
            if verification:
                return True, verification
        return self._raw_execution(path='field', method='POST', data=data)

    def search_field(self, **kwargs):
        """Searches for a field."""
        data = self._optional_variable(kwargs, ['type', 'id', 'query', 'orderBy', 'expand'])
        return self._raw_execution(path='/field/search', data=data)

    def get_field(self, field_id, **kwargs):  # pylint: disable=unused-argument
        """Get a field."""
        info = {}
        context = self._raw_execution(path=f'/field/{field_id}/context')
        info['context'] = context[1]['values'] if context[0] else None
        default_value = self._raw_execution(path=f'/field/{field_id}/context/defaultValue')
        info['defaultValue'] = default_value[1]['values'] if default_value[0] else None
        return True, info

    def get_field_option(self, field_id, context_id, **kwargs):
        """Get a field option."""
        data = self._optional_variable(kwargs, ['optionId', 'onlyOptions', 'startAt', 'maxResults'])
        return self._raw_execution(path=f'/field/{field_id}/context/{context_id}/option', data=data)

    def add_field_option(self, field_id, context_id, **kwargs):
        """Add a field option."""
        data = self._mandatory_variable(kwargs, ['options'])
        return self._raw_execution(path=f'/field/{field_id}/context/{context_id}/option', method='POST', data=data)

    def set_field_option(self, field_id, context_id, **kwargs):
        """Set a field option."""
        data = self._mandatory_variable(kwargs, ['options'])
        return self._raw_execution(path=f'/field/{field_id}/context/{context_id}/option', method='PUT', data=data)

    def del_field_option(self, field_id, context_id, option_id, **kwargs):  # pylint: disable=unused-argument
        """Delete a field option."""
        return self._raw_execution(path=f'/field/{field_id}/context/{context_id}/option/{option_id}', method='DELETE')
