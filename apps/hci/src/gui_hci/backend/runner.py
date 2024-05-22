import logging
from PySide6.QtCore import QObject, Signal
from .hci_script import hci_parse, HciInterpreter

def create_runner(codeTxt: str, loggerName: str) -> HciInterpreter:
    if not codeTxt.endswith('\n'):
            codeTxt += '\n'
    prog = hci_parse.parse(codeTxt)
    return HciInterpreter(prog, logger_name=loggerName)

    
