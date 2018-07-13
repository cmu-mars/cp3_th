import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.price_estimate import PriceEstimate  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def estimates_price_get(start_latitude, start_longitude, end_latitude, end_longitude):  # noqa: E501
    """Price Estimates

    The Price Estimates endpoint returns an estimated price range for each product offered at a given location. The price estimate is provided as a formatted string with the full price range and the localized currency symbol.&lt;br&gt;&lt;br&gt;The response also includes low and high estimates, and the [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency code for situations requiring currency conversion. When surge is active for a particular product, its surge_multiplier will be greater than 1, but the price estimate already factors in this multiplier.  # noqa: E501

    :param start_latitude: Latitude component of start location.
    :type start_latitude: float
    :param start_longitude: Longitude component of start location.
    :type start_longitude: float
    :param end_latitude: Latitude component of end location.
    :type end_latitude: float
    :param end_longitude: Longitude component of end location.
    :type end_longitude: float

    :rtype: List[PriceEstimate]
    """
    return 'do some magic!'


def estimates_time_get(start_latitude, start_longitude, customer_uuid=None, product_id=None):  # noqa: E501
    """Time Estimates

    The Time Estimates endpoint returns ETAs for all products offered at a given location, with the responses expressed as integers in seconds. We recommend that this endpoint be called every minute to provide the most accurate, up-to-date ETAs. # noqa: E501

    :param start_latitude: Latitude component of start location.
    :type start_latitude: float
    :param start_longitude: Longitude component of start location.
    :type start_longitude: float
    :param customer_uuid: Unique customer identifier to be used for experience customization.
    :type customer_uuid: dict | bytes
    :param product_id: Unique identifier representing a specific product for a given latitude &amp; longitude.
    :type product_id: str

    :rtype: List[Product]
    """
    if connexion.request.is_json:
        customer_uuid = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
