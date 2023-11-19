from . import console_log
import bleak
import asyncio
import logging
from asyncio import Queue
from bleak import BleakScanner
from PySide6.QtCore import QThread, Signal, QMutex, QMutexLocker, Qt , QTimer

class BleScanner(QThread):
    # class variables
    scan_timeout = 0
    is_scanning = False
    discovered_devices = Signal(tuple)
    logger = logging.getLogger("gattLogger")

    def run(self):
        # Need to run the async function in a thread otherwise it will block the main thread
        asyncio.run(self.BLE_discoverDevices())

    async def BLE_discoverDevices(self):
        try:
            # if scan timeout is 0, scan forever
            if self.scan_timeout == 0 and self.is_scanning == False:
                
                self.logger.info("Scanning indefinitely")
                self.is_scanning = True
                while self.is_scanning == True:
                    devices = await BleakScanner.discover(
                        return_adv=True,timeout=0.1)
                    for item, adv in devices.values():
                        self.discovered_devices.emit((item,adv))
                self.logger.info("Scan stopped")
            elif self.is_scanning == False:

                # in in half second intervals until timeout is met
                self.logger.info("Scanning for " + str(self.scan_timeout) + " seconds")
                self.is_scanning = True
                while self.scan_timeout >= 0.5 and self.is_scanning == True:

                    scanTime = 0.1  
                    devices = await BleakScanner.discover(
                    return_adv=True,timeout=scanTime)
                    for item in devices.values():
                        
                        self.discovered_devices.emit(item)
                    self.scan_timeout -= scanTime
                    
                self.logger.info("Scan stopped")
                self.is_scanning = False
                self.scanning_stoped.emit()

        except Exception as err:
            self.is_scanning = False
            self.logger.setLevel(logging.WARNING)
            self.logger.warning(err)
            self.logger.setLevel(logging.INFO)
            self.logger.info("Scan stopped")
            self.scanning_stoped.emit()
    

