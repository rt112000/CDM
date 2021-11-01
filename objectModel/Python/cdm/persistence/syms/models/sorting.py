# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Sorting(Model):
    """Column sorting.

    :param key_name: Name of column.
    :type key_name: str
    :param sort_order: Possible values include: 'DESC', 'ASC'
    :type sort_order: str or :class:`SortOrder
     <Microsoft.ADF.SyMSAPIClient.models.SortOrder>`
    """ 

    _validation = {
        'key_name': {'required': True},
        'sort_order': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'KeyName', 'type': 'str'},
        'sort_order': {'key': 'SortOrder', 'type': 'SortOrder'},
    }

    def __init__(self, key_name, sort_order):
        self.key_name = key_name
        self.sort_order = sort_order
