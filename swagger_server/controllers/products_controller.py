import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def products_get(latitude, longitude):  # noqa: E501
    """Product Types

    The Products endpoint returns information about the *Uber* products offered at a given location. The response includes the display name and other details about each product, and lists the products in the proper display order.  # noqa: E501

    :param latitude: Latitude component of location.
    :type latitude: float
    :param longitude: Longitude component of location.
    :type longitude: float

    :rtype: List[Product]
    """
    return 'do some magic!'
