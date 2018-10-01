from pyjsparser import PyJsParser
import requests
import urllib.parse
import logging

_LOGGER = logging.getLogger(__name__)


def get_devicelist(home_hub_ip='192.168.1.254'):
    """Retrieve data from BT Home Hub 6 and return parsed result.
    """

    url = 'http://{}/cgi/cgi_myNetwork.js'.format(home_hub_ip)

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        _LOGGER.exception("Connection to the router timed out")
        return
    if response.status_code == 200:
        return parse_devicelist(response.text)
    else:
        _LOGGER.error("Invalid response from Home Hub: %s", response)


def parse_devicelist(data_str):
    """Parse the BT Home Hub 6 data format."""
    # print(data_str);
    p = PyJsParser()
    parsed = p.parse(data_str)
    known_devices = {}
    for ele in parsed['body'][1]['declarations'][0]['init']['elements']:
        kv = {}
        if 'properties' not in ele:
            continue
        for prop in ele['properties']:
            kv[prop['key']['name']] = prop['value']['value']
        known_devices[urllib.parse.unquote(kv['mac'])] = urllib.parse.unquote(kv['hostname'])
    print(known_devices)

    devices = {}

    return devices
