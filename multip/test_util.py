import sys
import os

def get_tmp_dir():
    if sys.platform.startswith('win'):
        return os.getenv('TEMP')
    else:
        return '/tmp'