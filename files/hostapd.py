#!/usr/bin/env python

import json
import os
import re
import subprocess
import sys

content=dict()

version_re = re.compile('^hostapd\s+v(?P<version>[^ ]+)$')
try:
    result = subprocess.Popen(['/usr/bin/env', 'hostapd', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    (stdout, stderr) = result.communicate()
    output = stdout + stderr
    for line in output.split('\n'):
        match = version_re.search(line)
        if match:
            content['version_full'] = match.group('version')
            break
except subprocess.CalledProcessError as e:
    content['error'] = str(e)

if len(content) == 0:
    content = None

print(json.dumps(content))
sys.exit(0)
