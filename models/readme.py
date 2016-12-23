import os
import inspect

def is_readme(path):
    files = os.listdir(path)
    ignored = [file_ for file_ in files if ]
    readme = []
    for title in []
    if 'README.MD' in l:
        if l.count('README.MD') == 1:
            return True
        print 'WARNING: {path} contains multiple readme'.format(path=path)
    return False

def get_readme(path):
    for file_ in os.listdir(path):
        if file_.upper() == 'README.MD':
            return file_

class Readme(object):
    
    def __init__(self, path):
        self.root = path
        if is_readme(path):
            self.parse_readme(path)
        else:
            self.make_readme(path)

    def parse_readme(self, path):
        readme = get_readme(path)
        if readme != 'README.md':
            print 'WARNING: {path}/{readme}: readme file should be called README.md'.format(path=path, readme=readme)

    def make_readme(self, path):
        pass
