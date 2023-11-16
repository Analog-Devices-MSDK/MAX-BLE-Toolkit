from os import path
import sys

def convert_path_for_build(filepath):
    if hasattr(sys, "frozen"):
        filepath = path.join(sys.prefix, filepath)
    return filepath