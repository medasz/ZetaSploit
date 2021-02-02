#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
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

import os
import sys

from core.jobs import jobs
from core.storage import storage
from core.modules import modules
from core.exceptions import exceptions

class ZetaSploitCommand:
    def __init__(self):
        self.jobs = jobs()
        self.storage = storage()
        self.modules = modules()
        self.exceptions = exceptions()

        self.details = {
            'Category': "module",
            'Name': "back",
            'Description': "Return to the previous module.",
            'Usage': "back",
            'ArgsCount': 0,
            'NeedsArgs': False,
            'Args': list()
        }

    def run(self):
        if self.modules.check_current_module():
            self.storage.set("pwd", self.storage.get("pwd") - 1)
            self.storage.set("current_module", self.storage.get("current_module")[0:-1])
            if not self.storage.get("current_module"):
                self.storage.set("pwd", 0)
