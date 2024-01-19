# BLE_DTM_TX
Simple GUI App to drive BLE_hci.py found in Analog-Devices-MSDK

# Dependencies
The BLE-HCI backend is not available on PyPi and needs to be installed from source
The HCI can be found at [MAX-BLE-HCI](https://github.com/Analog-Devices-MSDK/MAX-BLE-HCI)

## Running from python directly

```bash
pip install -r requirements.txt
python3 dtm_tool.py
```

## Creating Binary

```bash
pip install pyinstaller
pyinstaller dtm_tool.py
```
