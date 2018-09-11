#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Mateusz Filipowicz <matfilipowicz@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: hassio_addons
author: "Mateusz Filipowicz (@filipowm)"
short_description: Manage Home Assistant (HassIO) addons
version_added: "1.0"
description:
  - Manage Home Assistant (HassIO, hass.io) addons - install, uninstall, start, stop, update addons   
options:
  state:
    description:
      - State of addon
    required: true
    choices: ['present', 'absent', 'started', 'stopped', 'updated']
  name:
    description:
      - Name of addon to install.
    aliases: ['addon']
    required: true
'''

EXAMPLES = '''
# Install Samba share addon
- hassio_addon:
    state: present
    name: core_samba
    
# Uninstall DHCP server and Grafana addons
- hassio_addon:
    state: absent
    name: {{ item }}
  with_items:
    - grafana
    - core_dhcp_server

# Start Samba share addon
- hassio_addon:
    state: started
    addon: core_samba

# Stop Samba share addon
- hassio_addon:
    state: stopped
    name: core_samba

# Update Samba share addon
- hassio_addon:
    state: updated
    name: core_samba
'''

# ===========================================
# Module execution.
#
import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native


def install(ansible, name):
  pass


def uninstall(ansible, name):
  pass


def start(ansible, name):
  pass


def stop(ansible, name):
  pass


def update(ansible, name):
  pass


def __raise(ex):
  raise ex


def main():
  module = AnsibleModule(
    argument_spec=dict(
      state=dict(required=True, choices=['present', 'absent', 'started', 'stopped', 'updated']),
      name=dict(required=True, aliases=['addon'])
    ),
    # TODO
    supports_check_mode=False
  )

  switch = {
    'present': install,
    'absent': uninstall,
    'started': start,
    'stopped': stop,
    'updated': update
  }
  state = module.params['state']
  name = module.params['name']

  try:
    action = switch.get(state, lambda: __raise(Exception('Action is undefined')))
    action(module, name)
    module.fail_json(msg='Not yet implemented')
  except Exception as e:
    module.fail_json(msg=to_native(e), exception=traceback.format_exc())


if __name__ == '__main__':
  main()
