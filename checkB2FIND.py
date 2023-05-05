#!/usr/bin/env python

"""checkB2FIND.py  performs checks according different probes and
returns the appropriate messages and codes.

Copyright (c) 2016 Heinrich Widmann (DKRZ)

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import argparse
import socket
import sys
import time

import requests


def check_url(url, timeout):
    """
    Checks and validates URL using requests module
    param url: URL being tested
    param timeout: timeout in seconds
    """

    rta = 0
    resplen = '--'
    try:
        start = time.time()
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        rta = time.time() - start

    except requests.exceptions.Timeout as e:
        msg = "    [Socket Timeout] %s" % e
        retcode = 2    # caught

    except requests.exceptions.HTTPError as e:
        msg = "    [HTTPError] %s" % e
        retcode = 2

    except IOError as e:
        msg = "    [IOError] %s" % e
        retcode = 1

    except ValueError as e:
        msg = "    [ValueError] %s" % e
        retcode = 1    # caught

    except Exception as e:
        msg = "    [Unknown Error] %s" % e
        retcode = 3    # caught

    else:
        msg = '[OK]'
        retcode = 0

    return retcode, msg, resplen, rta


def check_ckan_action(actionreq, data, timeout, rows):
    resplen = 0
    rta = 0
    try:
        start = time.time()
        response = requests.get(actionreq, timeout=timeout, params=data)
        result = response.json()['result']
        rta = time.time()-start

    except socket.timeout as e:
        msg = " [TIMEOUT] %s " % e
        retcode = 2
    except IOError as e:
        msg = " [IOError] %s " % e
        retcode = 1
    except ValueError as e:
        msg = " [ValueError] %s " % e
        retcode = 1    # caught
    except Exception as e:
        msg = "  [Error] %s " % e
        retcode = 3    # caught
    else:
        msg = '[OK]'
        retcode = 0
        assert response.status_code == 200

        if actionreq.endswith('organization_show'):
            resplen = result['package_count']

        else:
            resplen = len(result)

    return retcode, msg, resplen, rta


def main():
    B2FIND_version = '2.4'
    CKAN_version = '2.7'

    # # Get options and arguments
    args = get_args()

    if args.version:
        print('B2FIND %s :: CKAN %s' % (B2FIND_version, CKAN_version))
        sys.exit(0)

    sys.exit(checkProbes(args))


def checkProbes(args):
    # # Settings for CKAN client and API
    b2find_url = 'http://' + args.hostname
    if args.port:
        b2find_url += ':' + args.port

    ckanapi3act = b2find_url+'/api/3/action/'
    ckan_limit = 100

    suppProbes = [
        'URLcheck', 'ListDatasets', 'ListCommunities', 'ShowGroupENES'
    ]

    if args.action == 'all':
        probes = suppProbes

    else:
        if args.action in suppProbes:
            probes = [args.action]

        else:
            print('Action %s is not supported' % args.action)
            sys.exit(-1)

    totretcode = 0
    for probe in probes:
        data_dict = {}
        if probe == 'URLcheck':
            answer = check_url(b2find_url, args.timeout)

        else:
            if probe == 'ListDatasets':
                action = 'package_list'

            elif probe == 'ListCommunities':
                action = 'organization_list'

            elif probe == 'ShowGroupENES':
                action = 'organization_show'
                data_dict = {'id': 'darus'}

            actionreq = ckanapi3act + action

            answer = check_ckan_action(
                actionreq, data_dict, args.timeout, ckan_limit
            )

        print(
                ' %-15s is %-7s - %-20s - %-7s - %-7.2f ' % (
                    probe, answer[1], answer[0], answer[2], answer[3]
                )
        )

        print(' on service %s' % b2find_url)

        if answer[0] > totretcode:
            totretcode = answer[0]

    return totretcode


def ValidateValues(arguments):
    """ Validate values - input values """

    if arguments.timeout <= 0:
        print("\nInvalid timeout value: %s\n" % arguments.timeout)
        print_help()
        exit()

    if arguments.hostname is None:
        print("\nNo hostname provided\n")
        print_help()
        exit()


def print_help():
    """ Print help values."""

    print("usage: checkB2FIND.py -H -p")
    print("--- ---- ---- ---- ---- ---- ----\n")
    print("main arguments:")
    print(
        "-H hostname, URL of the B2FIND service, to which probes are submitted "
        "(default is b2find.eudat.eu)"
    )
    print("\n")
    print("optional arguments:")
    print(" -h, --help  show this help message and exit")
    print("-p port, The B2FIND server port.")
    print("-t timeout, Time threshold to wait before timeout (in second).")
    print("-v verbose")
    print("-e version, Prints the B2FIND and CKAN version and exits.")
    print(
        "-a action,Action which has to be excecuted and checked. "
        "Supported actions are URLcheck, ListDatasets, ListCommunities, "
        "ShowGroupENES or all "
    )


def get_args():
    p = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Description: Performs checks according different probes "
                    "and returns the appropriate messages and codes."
    )

    p.add_argument(
        '--version', '-v', help="prints the B2FIND and CKAN version and exits",
        action='store_true'
    )
    p.add_argument(
        '--timeout', '-t', default=1000, type=float,
        help="time out : After given number of seconds excecution terminates."
    )
    p.add_argument(
        '--action', '-a', default='all', metavar='STRING',
        help="Action which has to be excecuted and checked. "
             "Supported actions are URLcheck, ListDatasets, ListCommunities, "
             "ShowGroupENES or all (default)"
    )
    p.add_argument(
        '--hostname', '-H', default='b2find.eudat.eu', metavar='URL',
        help='Hostname of the B2FIND service, to which probes are submitted '
             '(default is b2find.eudat.eu)'
    )
    p.add_argument(
        '--port', '-p', default=None, metavar='URL',
        help='(Optional) Port of the B2FIND service, to which probes are '
             'submitted (default is None)'
    )

    args = p.parse_args()
    ValidateValues(args)

    return args


if __name__ == "__main__":
    main()
