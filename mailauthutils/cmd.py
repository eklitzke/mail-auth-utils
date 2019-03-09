# Copyright (C) 2019  Evan Klitzke <evan@eklitzke.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import base64
import logging
import getpass
from typing import Tuple


def cmd_get_userhost_and_password(description: str) -> Tuple[bytes, bytes]:
    """Command to get a username, domain, and password."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '-u', '--username', default=getpass.getuser(), help='IMAP user name')
    parser.add_argument('-p', '--password', type=str, help='IMAP password')
    parser.add_argument(
        '-v', '--verbose', help='Increase log verbosity', action='store_true')
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(levelname)s: %(message)s')

    user = args.username
    passwd = args.password
    if not passwd:
        passwd = getpass.getpass('Password for {}: '.format(user))

    return user.encode('utf8'), passwd.encode('utf8')


def b64encode(authstring: bytes) -> str:
    """Print a base64 encoded string."""
    return base64.encodebytes(authstring).decode('utf8').strip()
