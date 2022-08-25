import os
from typing_extensions import runtime
from pyats.easypy import run
SCRIPT_PATH = os.path.dirname(__file__)
def main():
    run(testscript=os.path.join(SCRIPT_PATH,'test_connections.py'))

