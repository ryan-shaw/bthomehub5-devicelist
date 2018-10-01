import bthomehub6_devicelist
from pprint import pprint


def main():

    # If an IP Address is not specified, it will default as 192.169.1.254
    devicelist = bthomehub6_devicelist.get_devicelist('192.168.1.254')

    pprint(devicelist)


if __name__ == '__main__':
    main()
