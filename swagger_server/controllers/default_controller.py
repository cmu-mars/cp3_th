import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.parameters import Parameters  # noqa: E501
from swagger_server.models.parameters1 import Parameters1  # noqa: E501
from swagger_server.models.parameters2 import Parameters2  # noqa: E501
from swagger_server import util


def done_post(Parameters):  # noqa: E501
    """done_post

    indicates that the test is completed # noqa: E501

    :param Parameters: 
    :type Parameters: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Parameters = Parameters2.from_dict(connexion.request.get_json())  # noqa: E501
        print(Parameters)
    return None


def error_post(Parameters):  # noqa: E501
    """error_post

    indicates that the SUT has encountered an error in configuration data, parameters, system start, or any other less specified problem # noqa: E501

    :param Parameters: 
    :type Parameters: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Parameters = Parameters.from_dict(connexion.request.get_json())  # noqa: E501
        print(Parameters)
    return None


def ready_post():  # noqa: E501
    """ready_post

    indicates that the SUT is ready to recieve configuration data to continue start up # noqa: E501


    :rtype: InlineResponse200
    """
    return InlineResponse200("l1","l2",False,"amcl-kinect","FAVOR_TIMELINESS")


def status_post(Parameters):  # noqa: E501
    """status_post

    indicate important state changes in the SUT to the TH. posted periodically as the described events occur. # noqa: E501

    :param Parameters: 
    :type Parameters: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Parameters = Parameters1.from_dict(connexion.request.get_json())  # noqa: E501
        print(Parameters)
    return None
