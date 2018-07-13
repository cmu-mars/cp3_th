import connexion
import six

import subprocess
import os

from swagger_server.models.corridor import Corridor  # noqa: E501
from swagger_server.models.element import Element  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.parameters import Parameters  # noqa: E501
from swagger_server.models.parameters1 import Parameters1  # noqa: E501
from swagger_server.models.parameters2 import Parameters2  # noqa: E501
from swagger_server.models.start_configuration import StartConfiguration as SC # noqa: E501
from swagger_server import util

from swagger_client import DefaultApi
from swagger_client import Parameters2 as TA_Parameters2
from swagger_client import Parameters as TA_Parameters

ready=None
info=InlineResponse2002('not-running', 'Waiting for experiment to come up', -1, -1, 0, 'amcl-kinect', [], -1, -1)
ta = None

def done_post(Parameters):  # noqa: E501
    """done_post

    indicates that the test is completed # noqa: E501

    :param Parameters: 
    :type Parameters: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Parameters = Parameters2.from_dict(connexion.request.get_json())  # noqa: E501
    info.status = "finished"
    info.message = "The robot finished"
    return 'do some magic!'


def error_post(Parameters):  # noqa: E501
    """error_post

    indicates that the SUT has encountered an error in configuration data, parameters, system start, or any other less specified problem # noqa: E501

    :param Parameters: 
    :type Parameters: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Parameters = Parameters.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def info_get():  # noqa: E501
    """info_get

    Gets information about the running system # noqa: E501


    :rtype: InlineResponse2002
    """
    global info, ta
    if ta is not None:
        obs = ta.observe_get()
        info.robot_x = obs.x 
        info.robot_y = obs.y
        info.robot_charge = obs.battery
    return info


def ready_post():  # noqa: E501
    """ready_post
s
    indicates that the SUT is ready to recieve configuration data to continue start up # noqa: E501


    :rtype: InlineResponse200
    """
    global ready
    return ready


def start_post(StartConfiguration):  # noqa: E501
    """start_post

     # noqa: E501

    :param StartConfiguration: 
    :type StartConfiguration: dict | bytes

    :rtype: InlineResponse2001
    """
    global ready
    if connexion.request.is_json:
        sc = SC.from_dict(connexion.request.get_json())  # noqa: E501
    ready = InlineResponse200(sc.start_loc, sc.target_loc, True, sc.configuration, sc.utility)
    global info
    info.robot_configuration = sc.configuration
    # launch docker-compose -f ui-th.yml
    s = subprocess.Popen(["./launch.sh"])

    return 'Starting th'


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
    global info, ta
    info.status = Parameters.status
    print(info.status)
    if info.status == 'live':
        ta = DefaultApi()
        ta.api_client.configuration.host = 'http://localhost:8000'
        ta.start_post()
        info.message = 'Starting the robot...'
        info.robot_path = Parameters.plan
    elif info.status == 'mission-running':
        info.message = 'Mission is running'
    else:
        info.message = Parameters.message
    node = "xxxx-xxxxx"
    sensor = "xxxxx"
    if Parameters.config is not None and len(Parameters.config) > 0:
        node = Parameters.config[0]
    # if Parameters.sensors is not None and len(Parameters.sensors) > 0:
    #     sensors = Parameters.sensors[0]
    # info.robot_configuration = "%s-%s" %(node,sensor)
    info.robot_configuration = node
    return 'do some magic!'

def lightsoff_post(Corridor):  # noqa: E501
    """lightsoff_post

    Turn lights off in corridor # noqa: E501

    :param Corridor: 
    :type Corridor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Corridor = Corridor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def nodefail_post(Node):  # noqa: E501
    """nodefail_post

    Causes the node to be killed # noqa: E501

    :param Node: 
    :type Node: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Node = Element.from_dict(connexion.request.get_json())  # noqa: E501
    global ta
    print("====> Killing node %s" %Node.id)
    resp = ta.perturb_nodefail_post(TA_Parameters2(Node.id))
    return "ok"


def sensorfail_post(Sensor):  # noqa: E501
    """sensorfail_post

    Causes the sensor to be killed # noqa: E501

    :param Sensor: 
    :type Sensor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Sensor = Element.from_dict(connexion.request.get_json())  # noqa: E501
    print("====> Killing sensor %s" %Sensor.id)
    rest = ta.perturb_nodefail_post(TA_Parameters(Sensor.id, False))
    return 'ok'

def stop_post():  # noqa: E501
    """stop_post

     # noqa: E501
    

    :rtype: None
    """
    s = subprocess.Popen(["./stop.sh"])

    return 'System stopped'