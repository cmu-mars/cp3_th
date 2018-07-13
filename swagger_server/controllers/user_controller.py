import connexion
import six

from swagger_server.models.activities import Activities  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server import util


def history_get(offset=None, limit=None):  # noqa: E501
    """User Activity

    The User Activity endpoint returns data about a user&#39;s lifetime activity with Uber. The response will include pickup locations and times, dropoff locations and times, the distance of past requests, and information about which products were requested.&lt;br&gt;&lt;br&gt;The history array in the response will have a maximum length based on the limit parameter. The response value count may exceed limit, therefore subsequent API requests may be necessary. # noqa: E501

    :param offset: Offset the list of returned results by this amount. Default is zero.
    :type offset: int
    :param limit: Number of items to retrieve. Default is 5, maximum is 100.
    :type limit: int

    :rtype: Activities
    """
    return 'do some magic!'


def me_get():  # noqa: E501
    """User Profile

    The User Profile endpoint returns information about the Uber user that has authorized with the application. # noqa: E501


    :rtype: Profile
    """
    return 'do some magic!'
