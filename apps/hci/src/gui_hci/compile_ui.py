import os
import subprocess
import argparse
import re

parser = argparse.ArgumentParser(
    description="Converts MAX BLE HCI Editor .ui files to python scripts.")

parser.add_argument(
    'filename',
    type=str,
    nargs='*',
    default=['all'],
    help="Filename(s) to convert. To convert all .ui files, type 'all' or leave blank."
)

FNAME_IN2OUT = {
    'main.ui' : 'ui_main.py',
    'main_alwaysRef.ui' : 'ui_mainAlwaysRef.py'
}

if __name__ == '__main__':
    fnames = parser.parse_args().filename
    compile_defView = False
    compile_refView = False
    if 'all' in fnames:
        compile_defView = True
        compile_refView = True
    else:
        if 'main.ui' in fnames:
            compile_defView = True
        if 'main_alwaysRef' in fnames:
            compile_refView = True

    if compile_defView:
        subprocess.run(['pyside6-uic', 'main.ui', '-o', 'backend/ui_main.py'])

        with open('backend/ui_main.py', 'r', encoding='utf-8') as cFile:
            codeLines = cFile.readlines()
        codeStarted = False

        for idx, line in enumerate(codeLines):
            if not codeStarted:
                if line.startswith('class'):
                    codeStarted = True
                    codeLines.insert(idx-1, 'from .nav_window import QDirectoryTree\n')
                    codeLines.insert(idx-1, 'from .ref_window import QDeselectableTreeView\n')
                continue
            
            if 'self.filetree = QTreeView(' in line:
                codeLines[idx] = line.replace('QTreeView(', 'QDirectoryTree(')
                continue

            if 'self.reftree = QTreeView(' in line:
                codeLines[idx] = line.replace('QTreeView(', 'QDeselectableTreeView(')

        with open('backend/ui_main.py', 'w', encoding='utf-8') as cFile:
            cFile.write(''.join(codeLines))

    if compile_refView:
        subprocess.run(['pyside6-uic', 'main_alwaysRef.ui', '-o', 'backend/ui_mainAlwaysRef.py'])

        with open('backend/ui_mainAlwaysRef.py', 'r', encoding='utf-8') as cFile:
            codeLines = cFile.readlines()
        codeStarted = False

        for idx, line in enumerate(codeLines):
            if not codeStarted:
                if line.startswith('class'):
                    codeStarted = True
                    codeLines[idx] = line.replace('Ui_MainWindow(', 'Ui_MainWindowRef(')
                    codeLines.insert(idx-1, 'from .nav_window import QDirectoryTree\n')
                    codeLines.insert(idx-1, 'from .ref_window import QDeselectableTreeView\n')
                continue

            if 'self.filetree = QTreeView(' in line:
                codeLines[idx] = line.replace('QTreeView(', 'QDirectoryTree(')
                continue

            if 'self.reftree = QTreeView(' in line:
                codeLines[idx] = line.replace('QTreeView(', 'QDeselectableTreeView(')

        with open('backend/ui_mainAlwaysRef.py', 'w', encoding='utf-8') as cFile:
            cFile.write(''.join(codeLines))
