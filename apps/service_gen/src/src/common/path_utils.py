import sys
from os import path


def convert_path_for_build(filepath):
    if hasattr(sys, "frozen"):
        filepath = path.join(sys.prefix, filepath)
    return filepath
