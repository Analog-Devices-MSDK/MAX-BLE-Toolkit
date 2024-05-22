from PySide6.QtGui import QColor, QTextCharFormat, QFont
from PySide6.QtCore import QRegularExpression

_bool_vals = ["TRUE", "FALSE"]
_cblocks_vals = ["FOR", "TO", "STEP", "IF", "ELSE", "WHILE"]
_logic_vals = ["AND", "OR", "NOT"]
_func_vals = ["ADD_DEV", "WAIT", "PRINT"]
_cmd_vals = [
    "DISCONNECT",
    "READ_REMOTE_VER_INFO",
    "SET_EVENT_MASK",
    "RESET",
    "READ_TX_PWR_LVL",
    "SET_CONTROLLER_TO_HOST_FC",
    "HOST_BUFFER_SIZE",
    "HOST_NUM_CMPL_PKTS",
    "SET_EVENT_MASK_PAGE2",
    "READ_AUTH_PAYLOAD_TO",
    "WRITE_AUTH_PAYLOAD_TO",
    "CONFIG_DATA_PATH",
    "READ_LOCAL_VER_INFO",
    "READ_LOCAL_SUP_CMDS",
    "READ_LOCAL_SUP_FEAT",
    "READ_BUF_SIZE",
    "READ_BD_ADDR",
    "READ_LOCAL_SUP_CODECS",
    "READ_LOCAL_SUP_CODEC_CAP",
    "READ_LOCAL_SUP_CONTROLLER_DLY",
    "READ_RSSI",
    "LE_SET_EVENT_MASK",
    "LE_READ_BUF_SIZE",
    "LE_READ_LOCAL_SUP_FEAT",
    "LE_SET_RAND_ADDR",
    "LE_SET_ADV_PARAM",
    "LE_READ_ADV_TX_POWER",
    "LE_SET_ADV_DATA",
    "LE_SET_SCAN_RESP_DATA",
    "LE_SET_ADV_ENABLE",
    "LE_SET_SCAN_PARAM",
    "LE_SET_SCAN_ENABLE",
    "LE_CREATE_CONN",
    "LE_CREATE_CONN_CANCEL",
    "LE_READ_WHITE_LIST_SIZE",
    "LE_CLEAR_WHITE_LIST",
    "LE_ADD_DEV_WHITE_LIST",
    "LE_REMOVE_DEV_WHITE_LIST",
    "LE_CONN_UPDATE",
    "LE_SET_HOST_CHAN_CLASS",
    "LE_READ_CHAN_MAP",
    "LE_READ_REMOTE_FEAT",
    "LE_ENCRYPT",
    "LE_RAND",
    "LE_START_ENCRYPTION",
    "LE_LTK_REQ_REPL",
    "LE_LTK_REQ_NEG_REPL",
    "LE_READ_SUP_STATES",
    "LE_RECEIVER_TEST",
    "LE_TRANSMITTER_TEST",
    "LE_TEST_END",
    "LE_REM_CONN_PARAM_REP",
    "LE_REM_CONN_PARAM_NEG_REP",
    "LE_SET_DATA_LEN",
    "LE_READ_DEF_DATA_LEN",
    "LE_WRITE_DEF_DATA_LEN",
    "LE_READ_LOCAL_P256_PUB_KEY",
    "LE_GENERATE_DHKEY",
    "LE_ADD_DEV_RES_LIST",
    "LE_REMOVE_DEV_RES_LIST",
    "LE_CLEAR_RES_LIST",
    "LE_READ_RES_LIST_SIZE",
    "LE_READ_PEER_RES_ADDR",
    "LE_READ_LOCAL_RES_ADDR",
    "LE_SET_ADDR_RES_ENABLE",
    "LE_SET_RES_PRIV_ADDR_TO",
    "LE_READ_MAX_DATA_LEN",
    "LE_READ_PHY",
    "LE_SET_DEF_PHY",
    "LE_SET_PHY",
    "LE_ENHANCED_RECEIVER_TEST",
    "LE_ENHANCED_TRANSMITTER_TEST",
    "LE_SET_ADV_SET_RAND_ADDR",
    "LE_SET_EXT_ADV_PARAM",
    "LE_SET_EXT_ADV_DATA",
    "LE_SET_EXT_SCAN_RESP_DATA",
    "LE_SET_EXT_ADV_ENABLE",
    "LE_READ_MAX_ADV_DATA_LEN",
    "LE_READ_NUM_SUP_ADV_SETS",
    "LE_REMOVE_ADV_SET",
    "LE_CLEAR_ADV_SETS",
    "LE_SET_PER_ADV_PARAM",
    "LE_SET_PER_ADV_DATA",
    "LE_SET_PER_ADV_ENABLE",
    "LE_SET_EXT_SCAN_PARAM",
    "LE_SET_EXT_SCAN_ENABLE",
    "LE_EXT_CREATE_CONN",
    "LE_PER_ADV_CREATE_SYNC",
    "LE_PER_ADV_CREATE_SYNC_CANCEL",
    "LE_PER_ADV_TERM_SYNC",
    "LE_ADD_DEV_PER_ADV_LIST",
    "LE_REMOVE_DEV_PER_ADV_LIST",
    "LE_CLEAR_PER_ADV_LIST",
    "LE_READ_PER_ADV_LIST_SIZE",
    "LE_READ_TX_POWER",
    "LE_READ_RF_PATH_COMP",
    "LE_WRITE_RF_PATH_COMP",
    "LE_SET_PRIVACY_MODE",
    "LE_RECEIVER_TEST_V3",
    "LE_TRANSMITTER_TEST_V3",
    "LE_SET_CONNLESS_CTE_TX_PARAMS",
    "LE_SET_CONNLESS_CTE_TX_ENABLE",
    "LE_SET_CONNLESS_IQ_SAMP_ENABLE",
    "LE_SET_CONN_CTE_RX_PARAMS",
    "LE_SET_CONN_CTE_TX_PARAMS",
    "LE_CONN_CTE_REQ_ENABLE",
    "LE_CONN_CTE_RSP_ENABLE",
    "LE_READ_ANTENNA_INFO",
    "LE_SET_PER_ADV_RCV_ENABLE",
    "LE_PER_ADV_SYNC_TRANSFER",
    "LE_PER_ADV_SET_INFO_TRANSFER",
    "LE_SET_PAST_PARAM",
    "LE_SET_DEFAULT_PAST_PARAM",
    "LE_GENERATE_DHKEY_V2",
    "LE_MODIFY_SLEEP_CLK_ACC",
    "LE_READ_BUF_SIZE_V2",
    "LE_READ_ISO_TX_SYNC",
    "LE_SET_CIG_PARAMS",
    "LE_SET_CIG_PARAMS_TEST",
    "LE_CREATE_CIS",
    "LE_REMOVE_CIG",
    "LE_ACCEPT_CIS_REQ",
    "LE_REJECT_CIS_REQ",
    "LE_CREATE_BIG",
    "LE_CREATE_BIG_TEST",
    "LE_TERMINATE_BIG",
    "LE_BIG_CREATE_SYNC",
    "LE_BIG_TERMINATE_SYNC",
    "LE_REQUEST_PEER_SCA",
    "LE_SETUP_ISO_DATA_PATH",
    "LE_REMOVE_ISO_DATA_PATH",
    "LE_ISO_TX_TEST",
    "LE_ISO_RX_TEST",
    "LE_ISO_READ_TEST_COUNTERS",
    "LE_ISO_TEST_END",
    "LE_SET_HOST_FEATURE",
    "LE_READ_ISO_LINK_QUAL",
    "LE_READ_ENHANCED_TX_POWER",
    "LE_READ_REMOTE_TX_POWER",
    "LE_SET_PATH_LOSS_REPORTING_PARAMS",
    "LE_SET_PATH_LOSS_REPORTING_ENABLE",
    "LE_SET_TX_POWER_REPORT_ENABLE",
    "LE_SET_DATA_RELATED_ADDRESS_CHANGES",
    "LE_SET_DEF_SUBRATE",
    "LE_SUBRATE_REQ",
    "VS_SET_SCAN_CH_MAP",
    "VS_SET_EVENT_MASK",
    "VS_ENA_ACL_SINK",
    "VS_GENERATE_ACL",
    "VS_ENA_AUTO_GEN_ACL",
    "VS_SET_TX_TEST_ERR_PATT",
    "VS_SET_CONN_OP_FLAGS",
    "VS_SET_P256_PRIV_KEY",
    "VS_GET_PER_CHAN_MAP",
    "VS_GET_ACL_TEST_REPORT",
    "VS_SET_LOCAL_MIN_USED_CHAN",
    "VS_GET_PEER_MIN_USED_CHAN",
    "VS_VALIDATE_PUB_KEY_MODE",
    "VS_SET_BD_ADDR",
    "VS_GET_RAND_ADDR",
    "VS_SET_LOCAL_FEAT",
    "VS_SET_OP_FLAGS",
    "VS_SET_ADV_TX_PWR",
    "VS_SET_CONN_TX_PWR",
    "VS_SET_ENC_MODE",
    "VS_SET_CHAN_MAP",
    "VS_SET_DIAG_MODE",
    "VS_SET_SNIFFER_ENABLE",
    "VS_GET_PDU_FILT_STATS",
    "VS_GET_SYS_STATS",
    "VS_GET_ADV_STATS",
    "VS_GET_SCAN_STATS",
    "VS_GET_CONN_STATS",
    "VS_GET_TEST_STATS",
    "VS_GET_POOL_STATS",
    "VS_SET_AUX_DELAY",
    "VS_SET_EXT_ADV_FRAG_LEN",
    "VS_SET_EXT_ADV_PHY_OPTS",
    "VS_SET_EXT_ADV_DEF_PHY_OPTS",
    "VS_GENERATE_ISO",
    "VS_GET_ISO_TEST_REPORT",
    "VS_ENA_ISO_SINK",
    "VS_ENA_AUTO_GEN_ISO",
    "VS_GET_CIS_STATS",
    "VS_GET_AUX_ADV_STATS",
    "VS_GET_AUX_SCAN_STATS",
    "VS_GET_PER_SCAN_STATS",
    "VS_SET_CONN_PHY_TX_PWR",
    "VS_REG_WRITE",
    "VS_REG_READ",
    "VS_RESET_CONN_STATS",
    "VS_TX_TEST",
    "VS_RESET_TEST_STATS",
    "VS_RX_TEST",
    "VS_GET_RSSI",
    "VS_BB_EN",
    "VS_BB_DIS",
]

BOOL_PATTERN = QRegularExpression(f'(?i)\\b({"|".join(_bool_vals)})\\b')
CBLOCK_PATTERN = QRegularExpression(f'(?i)\\b({"|".join(_cblocks_vals)})\\b')
LOGIC_PATTERN = QRegularExpression(f'(?i)\\b({"|".join(_logic_vals)})\\b')
FUNC_PATTERN = QRegularExpression(f'(?i)\\b({"|".join(_func_vals)})\\b')
CMD_PATTERN = QRegularExpression(f'(?i)\\b({"|".join(_cmd_vals)})\\b')
HEX_PATTERN = QRegularExpression("\\b0x")
STR_PATTERN = QRegularExpression("(?s)\\\".*?\\\"|\\'.*?\\'")
DEV_PATTERN = QRegularExpression("[a-zA-Z_]+[a-zA-Z_0-9]*:")
ID_PATTERN = QRegularExpression("\\b[a-zA-Z_]+[a-zA-Z_0-9]*\\b")
NUM_PATTERN = QRegularExpression("\\b(\\d+\\.\\d+|0x[a-fA-F0-9]+|\\d+)\\b")
COMMENT_PATTERN = QRegularExpression("(//.*)")
MULTILINE_PATTERN_START = QRegularExpression("/\\*")
MULTILINE_PATTERN_END = QRegularExpression("\\*/")

_colors_lightTheme = {
    "BOOL": QColor(29, 29, 194),
    "LOGIC": QColor(29, 29, 194),
    "CBLOCK": QColor(126, 3, 224),
    "FUNC": QColor(128, 104, 2),
    "CMD": QColor(137, 2, 31),
    "HEX": QColor(68, 68, 70),
    "STR": QColor(92, 3, 3),
    "DEV": QColor(17, 80, 166),
    "ID": QColor(6, 48, 106),
    "GROUP_1": QColor(103, 73, 4),
    "GROUP_2": QColor(90, 42, 127),
    "GROUP_3": QColor(113, 4, 22),
    "NUM": QColor(12, 88, 74),
    "COMMENT": QColor(80, 126, 21),
}

_colors_darkTheme = {
    "BOOL": QColor(16, 97, 252),
    "LOGIC": QColor(16, 97, 252),
    "CBLOCK": QColor(179, 54, 251),
    "FUNC": QColor(228, 241, 142),
    "CMD": QColor(251, 35, 82),
    "HEX": QColor(153, 153, 165),
    "STR": QColor(194, 112, 45),
    "DEV": QColor(18, 181, 237),
    "ID": QColor(209, 209, 248),
    "GROUP_1": QColor(248, 183, 35),
    "GROUP_2": QColor(119, 17, 195),
    "GROUP_3": QColor(218, 1, 37),
    "NUM": QColor(240, 251, 212),
    "COMMENT": QColor(90, 140, 28),
}

_boolFmt_lightTheme = QTextCharFormat()
_boolFmt_lightTheme.setForeground(_colors_lightTheme["BOOL"])

_logicFmt_lightTheme = QTextCharFormat()
_logicFmt_lightTheme.setForeground(_colors_lightTheme["LOGIC"])

_cblockFmt_lightTheme = QTextCharFormat()
_cblockFmt_lightTheme.setForeground(_colors_lightTheme["CBLOCK"])

_funcFmt_lightTheme = QTextCharFormat()
_funcFmt_lightTheme.setForeground(_colors_lightTheme["FUNC"])

_cmdFmt_lightTheme = QTextCharFormat()
_cmdFmt_lightTheme.setForeground(_colors_lightTheme["CMD"])

_hexFmt_lightTheme = QTextCharFormat()
_hexFmt_lightTheme.setForeground(_colors_lightTheme["HEX"])

_strFmt_lightTheme = QTextCharFormat()
_strFmt_lightTheme.setForeground(_colors_lightTheme["STR"])

_devFmt_lightTheme = QTextCharFormat()
_devFmt_lightTheme.setForeground(_colors_lightTheme["DEV"])
_devFmt_lightTheme.setFontWeight(QFont.Bold)

_idFmt_lightTheme = QTextCharFormat()
_idFmt_lightTheme.setForeground(_colors_lightTheme["DEV"])

_groupFmt1_lightTheme = QTextCharFormat()
_groupFmt1_lightTheme.setForeground(_colors_lightTheme["GROUP_1"])

_groupFmt2_lightTheme = QTextCharFormat()
_groupFmt2_lightTheme.setForeground(_colors_lightTheme["GROUP_2"])

_groupFmt3_lightTheme = QTextCharFormat()
_groupFmt3_lightTheme.setForeground(_colors_lightTheme["GROUP_3"])

_numFmt_lightTheme = QTextCharFormat()
_numFmt_lightTheme.setForeground(_colors_lightTheme["NUM"])

_commentFmt_lightTheme = QTextCharFormat()
_commentFmt_lightTheme.setForeground(_colors_lightTheme["COMMENT"])
_commentFmt_lightTheme.setFontItalic(True)


_boolFmt_darkTheme = QTextCharFormat()
_boolFmt_darkTheme.setForeground(_colors_darkTheme["BOOL"])

_logicFmt_darkTheme = QTextCharFormat()
_logicFmt_darkTheme.setForeground(_colors_darkTheme["LOGIC"])

_cblockFmt_darkTheme = QTextCharFormat()
_cblockFmt_darkTheme.setForeground(_colors_darkTheme["CBLOCK"])

_funcFmt_darkTheme = QTextCharFormat()
_funcFmt_darkTheme.setForeground(_colors_darkTheme["FUNC"])

_cmdFmt_darkTheme = QTextCharFormat()
_cmdFmt_darkTheme.setForeground(_colors_darkTheme["CMD"])

_hexFmt_darkTheme = QTextCharFormat()
_hexFmt_darkTheme.setForeground(_colors_darkTheme["HEX"])

_strFmt_darkTheme = QTextCharFormat()
_strFmt_darkTheme.setForeground(_colors_darkTheme["STR"])

_devFmt_darkTheme = QTextCharFormat()
_devFmt_darkTheme.setForeground(_colors_darkTheme["DEV"])
_devFmt_darkTheme.setFontWeight(QFont.Bold)

_idFmt_darkTheme = QTextCharFormat()
_idFmt_darkTheme.setForeground(_colors_darkTheme["ID"])

_groupFmt1_darkTheme = QTextCharFormat()
_groupFmt1_darkTheme.setForeground(_colors_darkTheme["GROUP_1"])

_groupFmt2_darkTheme = QTextCharFormat()
_groupFmt2_darkTheme.setForeground(_colors_darkTheme["GROUP_2"])

_groupFmt3_darkTheme = QTextCharFormat()
_groupFmt3_darkTheme.setForeground(_colors_darkTheme["GROUP_3"])

_numFmt_darkTheme = QTextCharFormat()
_numFmt_darkTheme.setForeground(_colors_darkTheme["NUM"])

_commentFmt_darkTheme = QTextCharFormat()
_commentFmt_darkTheme.setForeground(_colors_darkTheme["COMMENT"])
_commentFmt_darkTheme.setFontItalic(True)


LIGHT_THEME_TEXTFORMATS = {
    "BOOL": _boolFmt_lightTheme,
    "LOGIC": _logicFmt_lightTheme,
    "CBLOCK": _cblockFmt_lightTheme,
    "FUNC": _funcFmt_lightTheme,
    "CMD": _cmdFmt_lightTheme,
    "HEX": _hexFmt_lightTheme,
    "STR": _strFmt_lightTheme,
    "DEV": _devFmt_lightTheme,
    "ID": _idFmt_lightTheme,
    "GROUP_1": _groupFmt1_lightTheme,
    "GROUP_2": _groupFmt2_lightTheme,
    "GROUP_3": _groupFmt3_lightTheme,
    "NUM": _numFmt_lightTheme,
    "COMMENT": _commentFmt_lightTheme,
}

DARK_THEME_TEXTFORMATS = {
    "BOOL": _boolFmt_darkTheme,
    "LOGIC": _logicFmt_darkTheme,
    "CBLOCK": _cblockFmt_darkTheme,
    "FUNC": _funcFmt_darkTheme,
    "CMD": _cmdFmt_darkTheme,
    "HEX": _hexFmt_darkTheme,
    "STR": _strFmt_darkTheme,
    "DEV": _devFmt_darkTheme,
    "ID": _idFmt_darkTheme,
    "GROUP_1": _groupFmt1_darkTheme,
    "GROUP_2": _groupFmt2_darkTheme,
    "GROUP_3": _groupFmt3_darkTheme,
    "NUM": _numFmt_darkTheme,
    "COMMENT": _commentFmt_darkTheme,
}
