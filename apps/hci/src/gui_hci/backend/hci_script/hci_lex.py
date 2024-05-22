from .cmd_structs import CMD_OPCODE, CMD_PARAM_LEN
from ply.lex import TOKEN
import ply.lex as lex

keywords = [
    'TRUE',
    'FALSE',
    'FOR',
    'IF',
    'ELSE',
    'WHILE',
    'ADD_DEV',
    'WAIT',
    'AND',
    'OR',
    'NOT',
    'TO',
    'STEP',
    'PRINT'
]

reserved = {
    #'ELSE IF' : 'ELSEIF',
    'NOP' : 'CMD',
    'DISCONNECT' : 'CMD',
    'READ_REMOTE_VER_INFO' : 'CMD',
    'SET_EVENT_MASK' : 'CMD',
    'RESET' : 'CMD',
    'READ_TX_PWR_LVL' : 'CMD',
    'SET_CONTROLLER_TO_HOST_FC' : 'CMD',
    'HOST_BUFFER_SIZE' : 'CMD',
    'HOST_NUM_CMPL_PKTS' : 'CMD',
    'SET_EVENT_MASK_PAGE2' : 'CMD',
    'READ_AUTH_PAYLOAD_TO' : 'CMD',
    'WRITE_AUTH_PAYLOAD_TO' : 'CMD',
    'CONFIG_DATA_PATH' : 'CMD',
    'READ_LOCAL_VER_INFO' : 'CMD',
    'READ_LOCAL_SUP_CMDS' : 'CMD',
    'READ_LOCAL_SUP_FEAT' : 'CMD',
    'READ_BUF_SIZE' : 'CMD',
    'READ_BD_ADDR' : 'CMD',
    'READ_LOCAL_SUP_CODECS' : 'CMD',
    'READ_LOCAL_SUP_CODEC_CAP' : 'CMD',
    'READ_LOCAL_SUP_CONTROLLER_DLY' : 'CMD',
    'READ_RSSI' : 'CMD',
    'LE_SET_EVENT_MASK' : 'CMD',
    'LE_READ_BUF_SIZE' : 'CMD',
    'LE_READ_LOCAL_SUP_FEAT' : 'CMD',
    'LE_SET_RAND_ADDR' : 'CMD',
    'LE_SET_ADV_PARAM' : 'CMD',
    'LE_READ_ADV_TX_POWER' : 'CMD',
    'LE_SET_ADV_DATA' : 'CMD',
    'LE_SET_SCAN_RESP_DATA' : 'CMD',
    'LE_SET_ADV_ENABLE' : 'CMD',
    'LE_SET_SCAN_PARAM' : 'CMD',
    'LE_SET_SCAN_ENABLE' : 'CMD',
    'LE_CREATE_CONN' : 'CMD',
    'LE_CREATE_CONN_CANCEL' : 'CMD',
    'LE_READ_WHITE_LIST_SIZE' : 'CMD',
    'LE_CLEAR_WHITE_LIST' : 'CMD',
    'LE_ADD_DEV_WHITE_LIST' : 'CMD',
    'LE_REMOVE_DEV_WHITE_LIST' : 'CMD',
    'LE_CONN_UPDATE' : 'CMD',
    'LE_SET_HOST_CHAN_CLASS' : 'CMD',
    'LE_READ_CHAN_MAP' : 'CMD',
    'LE_READ_REMOTE_FEAT' : 'CMD',
    'LE_ENCRYPT' : 'CMD',
    'LE_RAND' : 'CMD',
    'LE_START_ENCRYPTION' : 'CMD',
    'LE_LTK_REQ_REPL' : 'CMD',
    'LE_LTK_REQ_NEG_REPL' : 'CMD',
    'LE_READ_SUP_STATES' : 'CMD',
    'LE_RECEIVER_TEST' : 'CMD',
    'LE_TRANSMITTER_TEST' : 'CMD',
    'LE_TEST_END' : 'CMD',
    'LE_REM_CONN_PARAM_REP' : 'CMD',
    'LE_REM_CONN_PARAM_NEG_REP' : 'CMD',
    'LE_SET_DATA_LEN' : 'CMD',
    'LE_READ_DEF_DATA_LEN' : 'CMD',
    'LE_WRITE_DEF_DATA_LEN' : 'CMD',
    'LE_READ_LOCAL_P256_PUB_KEY' : 'CMD',
    'LE_GENERATE_DHKEY' : 'CMD',
    'LE_ADD_DEV_RES_LIST' : 'CMD',
    'LE_REMOVE_DEV_RES_LIST' : 'CMD',
    'LE_CLEAR_RES_LIST' : 'CMD',
    'LE_READ_RES_LIST_SIZE' : 'CMD',
    'LE_READ_PEER_RES_ADDR' : 'CMD',
    'LE_READ_LOCAL_RES_ADDR' : 'CMD',
    'LE_SET_ADDR_RES_ENABLE' : 'CMD',
    'LE_SET_RES_PRIV_ADDR_TO' : 'CMD',
    'LE_READ_MAX_DATA_LEN' : 'CMD',
    'LE_READ_PHY' : 'CMD',
    'LE_SET_DEF_PHY' : 'CMD',
    'LE_SET_PHY' : 'CMD',
    'LE_ENHANCED_RECEIVER_TEST' : 'CMD',
    'LE_ENHANCED_TRANSMITTER_TEST' : 'CMD',
    'LE_SET_ADV_SET_RAND_ADDR' : 'CMD',
    'LE_SET_EXT_ADV_PARAM' : 'CMD',
    'LE_SET_EXT_ADV_DATA' : 'CMD',
    'LE_SET_EXT_SCAN_RESP_DATA' : 'CMD',
    'LE_SET_EXT_ADV_ENABLE' : 'CMD',
    'LE_READ_MAX_ADV_DATA_LEN' : 'CMD',
    'LE_READ_NUM_SUP_ADV_SETS' : 'CMD',
    'LE_REMOVE_ADV_SET' : 'CMD',
    'LE_CLEAR_ADV_SETS' : 'CMD',
    'LE_SET_PER_ADV_PARAM' : 'CMD',
    'LE_SET_PER_ADV_DATA' : 'CMD',
    'LE_SET_PER_ADV_ENABLE' : 'CMD',
    'LE_SET_EXT_SCAN_PARAM' : 'CMD',
    'LE_SET_EXT_SCAN_ENABLE' : 'CMD',
    'LE_EXT_CREATE_CONN' : 'CMD',
    'LE_PER_ADV_CREATE_SYNC' : 'CMD',
    'LE_PER_ADV_CREATE_SYNC_CANCEL' : 'CMD',
    'LE_PER_ADV_TERM_SYNC' : 'CMD',
    'LE_ADD_DEV_PER_ADV_LIST' : 'CMD',
    'LE_REMOVE_DEV_PER_ADV_LIST' : 'CMD',
    'LE_CLEAR_PER_ADV_LIST' : 'CMD',
    'LE_READ_PER_ADV_LIST_SIZE' : 'CMD',
    'LE_READ_TX_POWER' : 'CMD',
    'LE_READ_RF_PATH_COMP' : 'CMD',
    'LE_WRITE_RF_PATH_COMP' : 'CMD',
    'LE_SET_PRIVACY_MODE' : 'CMD',
    'LE_RECEIVER_TEST_V3' : 'CMD',
    'LE_TRANSMITTER_TEST_V3' : 'CMD',
    'LE_SET_CONNLESS_CTE_TX_PARAMS' : 'CMD',
    'LE_SET_CONNLESS_CTE_TX_ENABLE' : 'CMD',
    'LE_SET_CONNLESS_IQ_SAMP_ENABLE' : 'CMD',
    'LE_SET_CONN_CTE_RX_PARAMS' : 'CMD',
    'LE_SET_CONN_CTE_TX_PARAMS' : 'CMD',
    'LE_CONN_CTE_REQ_ENABLE' : 'CMD',
    'LE_CONN_CTE_RSP_ENABLE' : 'CMD',
    'LE_READ_ANTENNA_INFO' : 'CMD',
    'LE_SET_PER_ADV_RCV_ENABLE' : 'CMD',
    'LE_PER_ADV_SYNC_TRANSFER' : 'CMD',
    'LE_PER_ADV_SET_INFO_TRANSFER' : 'CMD',
    'LE_SET_PAST_PARAM' : 'CMD',
    'LE_SET_DEFAULT_PAST_PARAM' : 'CMD',
    'LE_GENERATE_DHKEY_V2' : 'CMD',
    'LE_MODIFY_SLEEP_CLK_ACC' : 'CMD',
    'LE_READ_BUF_SIZE_V2' : 'CMD',
    'LE_READ_ISO_TX_SYNC' : 'CMD',
    'LE_SET_CIG_PARAMS' : 'CMD',
    'LE_SET_CIG_PARAMS_TEST' : 'CMD',
    'LE_CREATE_CIS' : 'CMD',
    'LE_REMOVE_CIG' : 'CMD',
    'LE_ACCEPT_CIS_REQ' : 'CMD',
    'LE_REJECT_CIS_REQ' : 'CMD',
    'LE_CREATE_BIG' : 'CMD',
    'LE_CREATE_BIG_TEST' : 'CMD',
    'LE_TERMINATE_BIG' : 'CMD',
    'LE_BIG_CREATE_SYNC' : 'CMD',
    'LE_BIG_TERMINATE_SYNC' : 'CMD',
    'LE_REQUEST_PEER_SCA' : 'CMD',
    'LE_SETUP_ISO_DATA_PATH' : 'CMD',
    'LE_REMOVE_ISO_DATA_PATH' : 'CMD',
    'LE_ISO_TX_TEST' : 'CMD',
    'LE_ISO_RX_TEST' : 'CMD',
    'LE_ISO_READ_TEST_COUNTERS' : 'CMD',
    'LE_ISO_TEST_END' : 'CMD',
    'LE_SET_HOST_FEATURE' : 'CMD',
    'LE_READ_ISO_LINK_QUAL' : 'CMD',
    'LE_READ_ENHANCED_TX_POWER' : 'CMD',
    'LE_READ_REMOTE_TX_POWER' : 'CMD',
    'LE_SET_PATH_LOSS_REPORTING_PARAMS' : 'CMD',
    'LE_SET_PATH_LOSS_REPORTING_ENABLE' : 'CMD',
    'LE_SET_TX_POWER_REPORT_ENABLE' : 'CMD',
    'LE_SET_DATA_RELATED_ADDRESS_CHANGES' : 'CMD',
    'LE_SET_DEF_SUBRATE' : 'CMD',
    'LE_SUBRATE_REQ' : 'CMD',
    'VS_SET_SCAN_CH_MAP' : 'CMD',
    'VS_SET_EVENT_MASK' : 'CMD',
    'VS_ENA_ACL_SINK' : 'CMD',
    'VS_GENERATE_ACL' : 'CMD',
    'VS_ENA_AUTO_GEN_ACL' : 'CMD',
    'VS_SET_TX_TEST_ERR_PATT' : 'CMD',
    'VS_SET_CONN_OP_FLAGS' : 'CMD',
    'VS_SET_P256_PRIV_KEY' : 'CMD',
    'VS_GET_PER_CHAN_MAP' : 'CMD',
    'VS_GET_ACL_TEST_REPORT' : 'CMD',
    'VS_SET_LOCAL_MIN_USED_CHAN' : 'CMD',
    'VS_GET_PEER_MIN_USED_CHAN' : 'CMD',
    'VS_VALIDATE_PUB_KEY_MODE' : 'CMD',
    'VS_SET_BD_ADDR' : 'CMD',
    'VS_GET_RAND_ADDR' : 'CMD',
    'VS_SET_LOCAL_FEAT' : 'CMD',
    'VS_SET_OP_FLAGS' : 'CMD',
    'VS_SET_ADV_TX_PWR' : 'CMD',
    'VS_SET_CONN_TX_PWR' : 'CMD',
    'VS_SET_ENC_MODE' : 'CMD',
    'VS_SET_CHAN_MAP' : 'CMD',
    'VS_SET_DIAG_MODE' : 'CMD',
    'VS_SET_SNIFFER_ENABLE' : 'CMD',
    'VS_GET_PDU_FILT_STATS' : 'CMD',
    'VS_GET_SYS_STATS' : 'CMD',
    'VS_GET_ADV_STATS' : 'CMD',
    'VS_GET_SCAN_STATS' : 'CMD',
    'VS_GET_CONN_STATS' : 'CMD',
    'VS_GET_TEST_STATS' : 'CMD',
    'VS_GET_POOL_STATS' : 'CMD',
    'VS_SET_AUX_DELAY' : 'CMD',
    'VS_SET_EXT_ADV_FRAG_LEN' : 'CMD',
    'VS_SET_EXT_ADV_PHY_OPTS' : 'CMD',
    'VS_SET_EXT_ADV_DEF_PHY_OPTS' : 'CMD',
    'VS_GENERATE_ISO' : 'CMD',
    'VS_GET_ISO_TEST_REPORT' : 'CMD',
    'VS_ENA_ISO_SINK' : 'CMD',
    'VS_ENA_AUTO_GEN_ISO' : 'CMD',
    'VS_GET_CIS_STATS' : 'CMD',
    'VS_GET_AUX_ADV_STATS' : 'CMD',
    'VS_GET_AUX_SCAN_STATS' : 'CMD',
    'VS_GET_PER_SCAN_STATS' : 'CMD',
    'VS_SET_CONN_PHY_TX_PWR' : 'CMD',
    'VS_REG_WRITE' : 'CMD',
    'VS_REG_READ' : 'CMD',
    'VS_RESET_CONN_STATS' : 'CMD',
    'VS_TX_TEST' : 'CMD',
    'VS_RESET_TEST_STATS' : 'CMD',
    'VS_RX_TEST' : 'CMD',
    'VS_GET_RSSI' : 'CMD',
    'VS_BB_EN' : 'CMD',
    'VS_BB_DIS' : 'CMD'
}

tokens = [
    #'ELSEIF',
    'INT',
    'FLOAT',
    'STR',
    'PLUS',
    'MINUS',
    'POWER',
    'MUL',
    'DIV',
    'MOD',
    'ASSIGN',
    'RETASSIGN',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'EQUAL',
    'NOTEQUAL',
    'BITWISEOR',
    'BITWISEAND',
    'BITWISENOT',
    'BITWISEXOR',
    'BITWISELS',
    'BITWISERS',
    'ID',
    'DEV',
    'STEPIN',
    'STEPOUT',
    'SEP',
    'NEWLINE',
    'RPAREN',
    'LPAREN'
] + list(set(reserved.values())) + keywords

t_PLUS = r'\+'
t_MINUS = r'-'
t_POWER = r'\*\*'
t_MUL = r'\*'
t_MOD = r'%'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_ASSIGN = r'='
t_RETASSIGN = r'->'
t_LT = r'<'
t_LTE =r'<='
t_GT = r'>'
t_GTE = r'>='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_BITWISEOR = r'\|'
t_BITWISEAND = r'&'
t_BITWISENOT = r'~'
t_BITWISEXOR = r'\^'
t_BITWISELS = r'<<'
t_BITWISERS = r'>>'
t_RPAREN = r'\)'
t_LPAREN = r'\('
t_SEP = r','

t_ignore = ' \t'

decimal_int = r'\d+'
hex_int = r'0x([abcdefABCDEF]|\d)+'
integer = hex_int + r'|' + decimal_int

dquote_str = r'\"([^\\\n]|(\\.))*?\"'
squote_str = r'\'([^\\\n]|(\\.))*?\''
string = dquote_str + r'|' + squote_str

def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    t.lexer.lineno += t.value.count('\n')

def t_DIV(t):
    r'/'
    return t

def t_DEV(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*:'
    t.value = t.value.replace(':', '')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in keywords:
        t.type = t.value.upper()
    else:
        t.type = reserved.get(t.value.upper(), 'ID')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STEPIN(t):
    r'\{'
    try:
        t.lexer.level += 1
    except AttributeError:
        t.lexer.level = 1
    return t

def t_STEPOUT(t):
    r'\}'
    t.lexer.level -= 1
    return t

@TOKEN(integer)
def t_INT(t):
    if '0x' in t.value:
        t.value = t.value.replace('0x', '')
        t.value = int(t.value.replace('0x', ''), 16)
        return t
    t.value = int(t.value)
    return t

@TOKEN(string)
def t_STR(t):
    t.value = t.value[1:-1]
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return(t)

def t_error(t):
    print(f'Illegal input at line {t.lineno}')
    t.lexer.skip(1)

lex.lex()