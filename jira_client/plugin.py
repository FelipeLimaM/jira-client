"""Jira client plugin."""

class CustomFieldTypes:
    """Custom field types."""
    # pylint: disable=too-few-public-methods
    CASCADINGSELECT = 'com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect'
    DATEPICKER = 'com.atlassian.jira.plugin.system.customfieldtypes:datepicker'
    DATETIME = 'com.atlassian.jira.plugin.system.customfieldtypes:datetime'
    FLOAT = 'com.atlassian.jira.plugin.system.customfieldtypes:float'
    GROUPPICKER = 'com.atlassian.jira.plugin.system.customfieldtypes:grouppicker'
    IMPORTID = 'com.atlassian.jira.plugin.system.customfieldtypes:importid'
    LABELS = 'com.atlassian.jira.plugin.system.customfieldtypes:labels'
    MULTICHECKBOXES = 'com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes'
    MULTIGROUPPICKER = 'com.atlassian.jira.plugin.system.customfieldtypes:multigrouppicker'
    MULTISELECT = 'com.atlassian.jira.plugin.system.customfieldtypes:multiselect'
    MULTIUSERPICKER = 'com.atlassian.jira.plugin.system.customfieldtypes:multiuserpicker'
    MULTIVERSION = 'com.atlassian.jira.plugin.system.customfieldtypes:multiversion'
    PROJECT = 'com.atlassian.jira.plugin.system.customfieldtypes:project'
    RADIOBUTTONS = 'com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons'
    READONLYFIELD = 'com.atlassian.jira.plugin.system.customfieldtypes:readonlyfield'
    SELECT = 'com.atlassian.jira.plugin.system.customfieldtypes:select'
    TEXTAREA = 'com.atlassian.jira.plugin.system.customfieldtypes:textarea'
    TEXTFIELD = 'com.atlassian.jira.plugin.system.customfieldtypes:textfield'
    URL = 'com.atlassian.jira.plugin.system.customfieldtypes:url'
    USERPICKER = 'com.atlassian.jira.plugin.system.customfieldtypes:userpicker'
    VERSION = 'com.atlassian.jira.plugin.system.customfieldtypes:version'


class CustomFieldTypesSearcher:
    """Custom field types searcher."""
    # pylint: disable=too-few-public-methods
    CASCADINGSELECTSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher'
    DATERANGE = 'com.atlassian.jira.plugin.system.customfieldtypes:daterange'
    DATETIMERANGE = 'com.atlassian.jira.plugin.system.customfieldtypes:datetimerange'
    EXACTNUMBER = 'com.atlassian.jira.plugin.system.customfieldtypes:exactnumber'
    EXACTTEXTSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher'
    GROUPPICKERSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher'
    LABELSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher'
    MULTISELECTSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher'
    NUMBERRANGE = 'com.atlassian.jira.plugin.system.customfieldtypes:numberrange'
    PROJECTSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher'
    TEXTSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:textsearcher'
    USERPICKERGROUPSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher'
    VERSIONSEARCHER = 'com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher'
