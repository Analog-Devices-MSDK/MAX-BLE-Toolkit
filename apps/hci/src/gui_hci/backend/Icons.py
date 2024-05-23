from __future__ import annotations
from dataclasses import dataclass
from collections import namedtuple
from PySide6.QtCore import QFileInfo, Qt
from PySide6.QtGui import QIcon, QPixmap

_ICON_FILEPATH = QFileInfo(__file__).absoluteDir()
_ICON_FILEPATH.cdUp()
_ICON_FILEPATH.cd("assets/images")

# IconProvider = namedtuple("IconProvider", ['Light', 'Dark', 'NoIcon'])
Light: IconProvider = None
Dark: IconProvider = None
NoIcon: QIcon = None
WindowIcon: QIcon = None


@dataclass
class IconProvider:
    Explorer: QIcon
    Reference: QIcon
    Settings: QIcon
    Delete: QIcon
    Logo: QPixmap
    NewTab: QIcon
    RunCode: QIcon
    StopCode: QIcon
    SaveNeeded: QIcon


def initIcons():
    global Light
    global Dark
    global NoIcon
    global WindowIcon

    _explorer = QIcon()
    _reference = QIcon()
    _settings = QIcon()
    _delete = QIcon()
    _newTab = QIcon()
    _runCode = QIcon()
    _stopCode = QIcon()
    _saveNeeded = QIcon()
    _logo = QPixmap(_ICON_FILEPATH.filePath("analog-inv.png"))
    _logo = _logo.scaledToHeight(100, Qt.SmoothTransformation)

    _explorer.addPixmap(_ICON_FILEPATH.filePath("icons/cil-folder.png"))
    _reference.addPixmap(_ICON_FILEPATH.filePath("icons/cil-library.png"))
    _settings.addPixmap(_ICON_FILEPATH.filePath("icons/cil-settings.png"))
    _delete.addPixmap(_ICON_FILEPATH.filePath("icons/cil-x.png"))
    _newTab.addPixmap(_ICON_FILEPATH.filePath("icons/cil-plus.png"))
    _runCode.addPixmap(_ICON_FILEPATH.filePath("icons/cil-media-play.png"))
    _stopCode.addPixmap(_ICON_FILEPATH.filePath("icons/cil-media-stop.png"))
    _saveNeeded.addPixmap(_ICON_FILEPATH.filePath("icons/save-needed.png"))

    Dark = IconProvider(
        _explorer,
        _reference,
        _settings,
        _delete,
        _logo,
        _newTab,
        _runCode,
        _stopCode,
        _saveNeeded,
    )

    _explorer = QIcon()
    _reference = QIcon()
    _settings = QIcon()
    _delete = QIcon()
    _newTab = QIcon()
    _runCode = QIcon()
    _saveNeeded = QIcon()
    _stopCode = QIcon()
    _logo = QPixmap(_ICON_FILEPATH.filePath("analog.png"))

    _explorer.addPixmap(_ICON_FILEPATH.filePath("icons/cil-folder-inv.png"))
    _reference.addPixmap(_ICON_FILEPATH.filePath("icons/cil-library-inv.png"))
    _settings.addPixmap(_ICON_FILEPATH.filePath("icons/cil-settings-inv.png"))
    _delete.addPixmap(_ICON_FILEPATH.filePath("icons/cil-x-inv.png"))
    _newTab.addPixmap(_ICON_FILEPATH.filePath("icons/cil-plus-inv.png"))
    _runCode.addPixmap(_ICON_FILEPATH.filePath("icons/cil-media-play-inv.png"))
    _stopCode.addPixmap(_ICON_FILEPATH.filePath("icons/cil-media-stop-inv.png"))
    _saveNeeded.addPixmap(_ICON_FILEPATH.filePath("icons/save-needed-inv.png"))
    _logo = _logo.scaledToHeight(100, Qt.SmoothTransformation)

    Light = IconProvider(
        _explorer,
        _reference,
        _settings,
        _delete,
        _logo,
        _newTab,
        _runCode,
        _stopCode,
        _saveNeeded,
    )

    NoIcon = QIcon()
    WindowIcon = QIcon(_ICON_FILEPATH.filePath("adi_logo_icon.ico"))
