#! /usr/bin/env python
import lxml.etree as et
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError
from Queue import Queue
import threading
import os
import pprint
import time

PAYLOADS = [
    '''
<login>
<user>admin</user>
<password>admin</password>
</login>
''',
]

class NetconfManager:
    def __init__(self, host, port, username, password, vendor):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.vendor = vendor
        self.tests = dict()

    def add_test(self, test, rpcs):
        self.tests[test]=rpcs

    def dispatch(self, rpc, is_file=True):
        # connect to netconf agent
        with manager.connect(host=self.host,
                             port=self.port,
                             username=self.username,
                             password=self.password,
                             timeout=90,
                             hostkey_verify=False,
                             look_for_keys=False,
                             allow_agent=False,
                             device_params={'name': self.vendor.lower()}
                             ) as m:

             #TODO: Remove this code hack for Nokia session openning.
             if str(self.vendor) == 'NOKIA':
                # Open NETCONF session
                for payload in PAYLOADS:
                    try:
                        response = m.dispatch(et.fromstring(payload))
                        print('Session opened')
                    except RPCError as e:
                        print("Exception when initializing the session: %s\n" % e)
             try:
                 if is_file:
                     with open(rpc) as f:
                         rpc_data = f.read()
                 else:
                     rpc_data = rpc
                 print(rpc_data)
                 response = m.dispatch(et.fromstring(rpc_data))
             except RPCError as e:
                 raise Exception("Exception when sending the rpc : %s\n, \%s" % (rpc_data,e))
        return response

class Managers:
    def __init__(self):
        self._managers = dict()

    def add_manager(self, host, port, username, password, vendor):
        m = NetconfManager(host, port, username, password, vendor)
        self._managers[host+':'+str(port)] = m

    def get_manager(self, host, port):
        if host+':'+str(port) in self._managers:
            return self._managers[host+':'+str(port)]
        return None

    @property
    def managers(self):
        return self._managers


if __name__ == '__main__':

    parser = ArgumentParser(description='Usage:')

    # script arguments
    parser.add_argument('-a', '--host', type=str, required=True,
                        help="Device IP address or Hostname")
    parser.add_argument('-u', '--username', type=str, required=True,
                        help="Device Username (netconf agent username)")
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Device Password (netconf agent password)")
    parser.add_argument('--port', type=int, default=830,
                        help="Netconf agent port")
    parser.add_argument('--datastore', type=str, default='running',
                        help="Netconf agent port")
    parser.add_argument('--vendor', type=str, default='NOKIA',
                        help="Netconf agent port")
    parser.add_argument('-t', '--test-suite-folder', action='append',
                        help="Netconf agent port")
    args = parser.parse_args()

    # Create results directory if neccesary
    directory = 'results_' + args.vendor
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Initialize managers
    m = Managers()
    # Create NetconfServer
    m.add_manager(args.host, args.port, args.username, args.password, args.vendor)
