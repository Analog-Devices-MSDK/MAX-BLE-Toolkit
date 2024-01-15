MAX_CHANNEL = 39
MIN_CHANNEL = 0
AVAILABLE_TX_POWERS = ["-15dbm", "-10dbm", "-5dbm", "0dbm", "2dbm", "4dbm", "6dbm"]
AVAILABLE_PHYS = ["1M", "2M", "S8", "S2"]
TX_PACKET_TYPES = {
    "PRBS9": 0,
    "11110000": 1,
    "10101010": 2,
    "PRBS15": 3,
    "11111111": 4,
    "00000000": 5,
    "00001111": 6,
    "01010101": 7,
}

TX_PHY_TYPES = {"1M": 1, "2M": 2, "S8": 3, "S2": 4}

TX_PACKET_TYPE_OPTIONS = list(TX_PACKET_TYPES.keys())
TX_PHY_TYPE_OPTIONS = list(TX_PHY_TYPES.keys())


def channel_to_freq(channel):
    return 2.402e9 * (channel + 1)
