'''
    generate readme
'''

import os
from Readme import Readme, is_readme

UNWANTED_DIR = [
        '.git'
]

def wanted(path):
    for unwanted in UNWANTED_DIR:
        if unwanted in path:
            return False
    return True

for root, dirs, files in os.walk('.', topdown=False):
    for d in dirs:
        path = root + '/' + d
        if wanted(path):
            readme = Readme(path)
#            Readme.write(path)
