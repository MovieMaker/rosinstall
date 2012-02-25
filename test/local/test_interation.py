#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import copy
import yaml
import subprocess
import tempfile

import rosinstall
import rosinstall.multiproject_cmd
import rosinstall.ui
        
from test.scm_test_base import AbstractFakeRosBasedTest, _create_yaml_file, _create_config_elt_dict

class FakeUi:
    def __init__(self, path = '', mode='skip'):
        self.path = path
        self.mode = mode
    def get_backup_path(self):
        return path
    def prompt_del_abort_retry(self, prompt, allow_skip = False):
        return mode


class RosinstallInteractive(AbstractFakeRosBasedTest):
    """tests with possible User Interaction, using mock to simulate user input"""

    def setUp(self):
        rosinstall.ui.Ui.set_ui(FakeUi())
    
    def test_twice_with_relpath(self):
        """runs rosinstall with generated self.simple_rosinstall to create local rosinstall env
        and creates a directory for a second local rosinstall env"""
        AbstractFakeRosBasedTest.setUp(self)


        self.rel_uri_rosinstall = os.path.join(self.test_root_path, "rel_uri.rosinstall")
        _create_yaml_file([_create_config_elt_dict("git", "ros", self.ros_path),
                           _create_config_elt_dict("git", "gitrepo", os.path.relpath(self.git_path))],
                          self.rel_uri_rosinstall)



        config = rosinstall.multiproject_cmd.get_config(self.directory, [self.rel_uri_rosinstall, self.ros_path])
        rosinstall.multiproject_cmd.cmd_install_or_update(config)

        config = rosinstall.multiproject_cmd.get_config(self.directory, [self.rel_uri_rosinstall, self.ros_path])
        rosinstall.multiproject_cmd.cmd_install_or_update(config)