"""Jira client utils."""

def get_if_exists(dict_list, key, value):
    """Get an item if present with a specific value in a list of dicts."""
    for item in dict_list:
        if key in item and item[key] == value:
            return item
    return None
