#! /usr/bin/env python3
###############################################################################
#
#
# Copyright (C) 2023 Maxim Integrated Products, Inc., All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL MAXIM INTEGRATED BE LIABLE FOR ANY CLAIM, DAMAGES
# OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name of Maxim Integrated
# Products, Inc. shall not be used except as stated in the Maxim Integrated
# Products, Inc. Branding Policy.
#
# The mere transfer of this software does not imply any licenses
# of trade secrets, proprietary technology, copyrights, patents,
# trademarks, maskwork rights, or any other form of intellectual
# property whatsoever. Maxim Integrated Products, Inc. retains all
# ownership rights.
#
##############################################################################
#
# Copyright 2023 Analog Devices, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
##############################################################################
"""
common_input.py

Description: Common input file

"""

from PySide6.QtWidgets import QComboBox, QLabel, QSlider, QSpinBox
from max_ble_hci import utils as hci_utils


class CommonInputGroup:
    """Internal grouping of common inputs"""

    # pylint: disable=too-many-arguments
    def __init__(
        self, port_select, baud_rate_select, channel_label, channel_select, phy_select
    ) -> None:
        self.port_select: QComboBox = port_select
        self.baud_rate_select: QSpinBox = baud_rate_select
        self.channel_label: QLabel = channel_label
        self.channel_select: QSlider = channel_select
        self.phy_select: QComboBox = phy_select

    def set_channel(self, channel: int):
        """Set channel in input group

        Parameters
        ----------
        channel : int
            0 - 39
        """
        self.channel_select.setValue(channel)
        self.set_channel_label(channel)

    def set_channel_label(self, channel: int):
        """Set channel label

        Parameters
        ----------
        channel : int
            channel to set label to
        """
        assert (
            self.channel_select.minimum() <= channel <= self.channel_select.maximum()
        ), f"Channel out of range {channel}"

        self.channel_label.setText(f"Channel {channel}")

    def refresh_port_select(self):
        """Refresh serial ports"""
        ports = hci_utils.get_serial_ports()
        self.port_select.clear()
        self.port_select.insertItems(0, ports)

    def selected_port(self) -> str:
        """Get Current selected

        Returns
        -------
        str
            Serial port string
        """
        return self.port_select.currentText()

    def set_port(self, port: str):
        """Set the serial port in the input group

        Parameters
        ----------
        port : str
            Serial port
        """
        idx = self.port_select.findText(port)
        self.port_select.setCurrentIndex(idx)

    def selected_baud(self) -> int:
        """Get current selected baud rate

        Returns
        -------
        int
            Baudrate
        """
        return self.baud_rate_select.value()

    def set_baud(self, baud: int):
        """Set baud rate

        Parameters
        ----------
        baud : int
            Baudrate
        """
        self.baud_rate_select.setValue(baud)

    def selected_phy(self) -> str:
        """Get Current Select PHY

        Returns
        -------
        str
            PHY
        """
        return self.phy_select.currentText()

    def set_phy(self, phy: str):
        """Set phy in input group

        Parameters
        ----------
        phy : str
            phy
        """
        self.phy_select.setCurrentText(phy)

    def selected_channel(self) -> int:
        """Get current selected channel

        Returns
        -------
        int
            Channel
        """
        return self.channel_select.value()

    def enable_serial_inputs(self, enable=True):
        """Enable/Disable serial inputs

        Parameters
        ----------
        enable : bool, optional
            Enable or disable, by default True
        """
        self.port_select.setEnabled(enable)
        self.baud_rate_select.setEnabled(enable)
