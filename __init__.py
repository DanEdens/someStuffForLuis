import argparse
import os
import sys

# import devices

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent)

parser = argparse.ArgumentParser(
        description="useage: python main.py --device randomname --package randompackage --tests randomtests",
        prog='someStuffForLuis',
        formatter_class=argparse.RawDescriptionHelpFormatter
        )

parser.add_argument(
        '-v',
        '--debug', action='store_true',
        default=os.environ.get("testkit_debug", False),
        help='Print debug information to terminal'
        )

parser.add_argument(
        '-p',
        '--package',
        default=os.environ.get("cdrouter_package",
                               os.environ.get("cdrouter_tests")),
        help='The name of the package(s) to be created'
        )

parser.add_argument(
        # '-t',
        '--tests',
        default=os.environ.get("cdrouter_tests", 'cdrouter'),
        # choices=devices.testList,
        help='The name of the file containing a list of tests that define the package'
        )

parser.add_argument(
        # '-d',
        '--device',
        default=os.environ.get("cdrouter_device", 'cdrouter'),
        # choices=devices.deviceList,
        help='The name of the device under test'
        )

parser.add_argument(
        '-c',
        '--config',
        default=os.environ.get("cdrouter_config"),
        # choices=devices.configList,
        help='The name of the file containing the device configuration'
        )

parser.add_argument(
        '-m',
        '--message',
        default=os.environ.get("cdrouter_message", 'Created by addpackage'),
        help='The name of the package(s) to be created'
        )

parser.add_argument(
        '--output',
        default=os.environ.get("cdrouter_output",
                               "CDRouter/results.xml"),
        # choices=devices.configList,
        help='The name of the Results file'
        )

parser.add_argument(
        '--restart',
        action='store_true',
        default=os.environ.get("cdrouter_restart", False),
        # choices=devices.configList,
        help='Force Network restart after Interface switch, '
             'Otherwise default to device specific'
        )

parser.add_argument(
        '--skipcleanup',
        action='store_true',
        default=os.environ.get("skipcleanup", False),
        help='Skip cleanup for debugging'
        )

args = parser.parse_args()

# Jenkins parameter Boolean conversions
if args.skipcleanup == 'false':
    args.skipcleanup = False
if args.skipcleanup == 'true':
    args.skipcleanup = True

if args.restart == 'false':
    args.restart = False
if args.restart == 'true':
    args.restart = True

if args.debug == 'false':
    args.debug = False
if args.debug == 'true':
    args.debug = True
