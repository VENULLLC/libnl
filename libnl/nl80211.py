"""802.11 Netlink Interface (uapi/linux/nl80211.h).
http://git.kernel.org/cgit/linux/kernel/git/linville/wireless.git/tree/include/uapi/linux/nl80211.h?id=v3.18

Copyright 2015 Robert Pooley <robpol86@gmail.com>
Copyright 2006-2010 Johannes Berg <johannes@sipsolutions.net>
Copyright 2008 Michael Wu <flamingice@sourmilk.net>
Copyright 2008 Luis Carlos Cobo <luisca@cozybit.com>
Copyright 2008 Michael Buesch <m@bues.ch>
Copyright 2008, 2009 Luis R. Rodriguez <lrodriguez@atheros.com>
Copyright 2008 Jouni Malinen <jouni.malinen@atheros.com>
Copyright 2008 Colin McCabe <colin@cozybit.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""


NL80211_GENL_NAME = b'nl80211'

NL80211_MESH_SETUP_INVALID = 0
NL80211_MESH_SETUP_ENABLE_VENDOR_PATH_SEL = 1
NL80211_MESH_SETUP_ENABLE_VENDOR_METRIC = 2
NL80211_MESH_SETUP_IE = 3
NL80211_MESH_SETUP_USERSPACE_AUTH = 4
NL80211_MESH_SETUP_USERSPACE_AMPE = 5
NL80211_MESH_SETUP_ENABLE_VENDOR_SYNC = 6
NL80211_MESH_SETUP_USERSPACE_MPM = 7
NL80211_MESH_SETUP_AUTH_PROTOCOL = 8
NL80211_MESH_SETUP_ATTR_MAX = 8

NL80211_CMD_UNSPEC = 0
NL80211_CMD_GET_WIPHY = 1
NL80211_CMD_SET_WIPHY = 2
NL80211_CMD_NEW_WIPHY = 3
NL80211_CMD_DEL_WIPHY = 4
NL80211_CMD_GET_INTERFACE = 5
NL80211_CMD_SET_INTERFACE = 6
NL80211_CMD_NEW_INTERFACE = 7
NL80211_CMD_DEL_INTERFACE = 8
NL80211_CMD_GET_KEY = 9
NL80211_CMD_SET_KEY = 10
NL80211_CMD_NEW_KEY = 11
NL80211_CMD_DEL_KEY = 12
NL80211_CMD_GET_BEACON = 13
NL80211_CMD_SET_BEACON = 14
NL80211_CMD_START_AP = 15
NL80211_CMD_NEW_BEACON = NL80211_CMD_START_AP
NL80211_CMD_STOP_AP = 16
NL80211_CMD_DEL_BEACON = NL80211_CMD_STOP_AP
NL80211_CMD_GET_STATION = 17
NL80211_CMD_SET_STATION = 18
NL80211_CMD_NEW_STATION = 19
NL80211_CMD_DEL_STATION = 20
NL80211_CMD_GET_MPATH = 21
NL80211_CMD_SET_MPATH = 22
NL80211_CMD_NEW_MPATH = 23
NL80211_CMD_DEL_MPATH = 24
NL80211_CMD_SET_BSS = 25
NL80211_CMD_SET_REG = 26
NL80211_CMD_REQ_SET_REG = 27
NL80211_CMD_GET_MESH_CONFIG = 28
NL80211_CMD_SET_MESH_CONFIG = 29
NL80211_CMD_SET_MGMT_EXTRA_IE = 30
NL80211_CMD_GET_REG = 31
NL80211_CMD_GET_SCAN = 32
NL80211_CMD_TRIGGER_SCAN = 33
NL80211_CMD_NEW_SCAN_RESULTS = 34
NL80211_CMD_SCAN_ABORTED = 35
NL80211_CMD_REG_CHANGE = 36
NL80211_CMD_AUTHENTICATE = 37
NL80211_CMD_ASSOCIATE = 38
NL80211_CMD_DEAUTHENTICATE = 39
NL80211_CMD_DISASSOCIATE = 40
NL80211_CMD_MICHAEL_MIC_FAILURE = 41
NL80211_CMD_REG_BEACON_HINT = 42
NL80211_CMD_JOIN_IBSS = 43
NL80211_CMD_LEAVE_IBSS = 44
NL80211_CMD_TESTMODE = 45
NL80211_CMD_CONNECT = 46
NL80211_CMD_ROAM = 47
NL80211_CMD_DISCONNECT = 48
NL80211_CMD_SET_WIPHY_NETNS = 49
NL80211_CMD_GET_SURVEY = 50
NL80211_CMD_NEW_SURVEY_RESULTS = 51
NL80211_CMD_SET_PMKSA = 52
NL80211_CMD_DEL_PMKSA = 53
NL80211_CMD_FLUSH_PMKSA = 54
NL80211_CMD_REMAIN_ON_CHANNEL = 55
NL80211_CMD_CANCEL_REMAIN_ON_CHANNEL = 56
NL80211_CMD_SET_TX_BITRATE_MASK = 57
NL80211_CMD_REGISTER_FRAME = 58
NL80211_CMD_REGISTER_ACTION = NL80211_CMD_REGISTER_FRAME
NL80211_CMD_FRAME = 59
NL80211_CMD_ACTION = NL80211_CMD_FRAME
NL80211_CMD_FRAME_TX_STATUS = 60
NL80211_CMD_ACTION_TX_STATUS = NL80211_CMD_FRAME_TX_STATUS
NL80211_CMD_SET_POWER_SAVE = 61
NL80211_CMD_GET_POWER_SAVE = 62
NL80211_CMD_SET_CQM = 63
NL80211_CMD_NOTIFY_CQM = 64
NL80211_CMD_SET_CHANNEL = 65
NL80211_CMD_SET_WDS_PEER = 66
NL80211_CMD_FRAME_WAIT_CANCEL = 67
NL80211_CMD_JOIN_MESH = 68
NL80211_CMD_LEAVE_MESH = 69
NL80211_CMD_UNPROT_DEAUTHENTICATE = 70
NL80211_CMD_UNPROT_DISASSOCIATE = 71
NL80211_CMD_NEW_PEER_CANDIDATE = 72
NL80211_CMD_GET_WOWLAN = 73
NL80211_CMD_SET_WOWLAN = 74
NL80211_CMD_START_SCHED_SCAN = 75
NL80211_CMD_STOP_SCHED_SCAN = 76
NL80211_CMD_SCHED_SCAN_RESULTS = 77
NL80211_CMD_SCHED_SCAN_STOPPED = 78
NL80211_CMD_SET_REKEY_OFFLOAD = 79
NL80211_CMD_PMKSA_CANDIDATE = 80
NL80211_CMD_TDLS_OPER = 81
NL80211_CMD_TDLS_MGMT = 82
NL80211_CMD_UNEXPECTED_FRAME = 83
NL80211_CMD_PROBE_CLIENT = 84
NL80211_CMD_REGISTER_BEACONS = 85
NL80211_CMD_UNEXPECTED_4ADDR_FRAME = 86
NL80211_CMD_SET_NOACK_MAP = 87
NL80211_CMD_CH_SWITCH_NOTIFY = 88
NL80211_CMD_START_P2P_DEVICE = 89
NL80211_CMD_STOP_P2P_DEVICE = 90
NL80211_CMD_CONN_FAILED = 91
NL80211_CMD_SET_MCAST_RATE = 92
NL80211_CMD_SET_MAC_ACL = 93
NL80211_CMD_RADAR_DETECT = 94
NL80211_CMD_GET_PROTOCOL_FEATURES = 95
NL80211_CMD_UPDATE_FT_IES = 96
NL80211_CMD_FT_EVENT = 97
NL80211_CMD_CRIT_PROTOCOL_START = 98
NL80211_CMD_CRIT_PROTOCOL_STOP = 99
NL80211_CMD_GET_COALESCE = 100
NL80211_CMD_SET_COALESCE = 101
NL80211_CMD_CHANNEL_SWITCH = 102
NL80211_CMD_VENDOR = 103
NL80211_CMD_SET_QOS_MAP = 104
NL80211_CMD_ADD_TX_TS = 105
NL80211_CMD_DEL_TX_TS = 106
NL80211_CMD_MAX = 113

NL80211_CMD_SET_BSS = NL80211_CMD_SET_BSS
NL80211_CMD_SET_MGMT_EXTRA_IE = NL80211_CMD_SET_MGMT_EXTRA_IE
NL80211_CMD_REG_CHANGE = NL80211_CMD_REG_CHANGE
NL80211_CMD_AUTHENTICATE = NL80211_CMD_AUTHENTICATE
NL80211_CMD_ASSOCIATE = NL80211_CMD_ASSOCIATE
NL80211_CMD_DEAUTHENTICATE = NL80211_CMD_DEAUTHENTICATE
NL80211_CMD_DISASSOCIATE = NL80211_CMD_DISASSOCIATE
NL80211_CMD_REG_BEACON_HINT = NL80211_CMD_REG_BEACON_HINT
NL80211_CMD_GET_MESH_PARAMS = NL80211_CMD_GET_MESH_CONFIG
NL80211_CMD_SET_MESH_PARAMS = NL80211_CMD_SET_MESH_CONFIG
NL80211_MESH_SETUP_VENDOR_PATH_SEL_IE = NL80211_MESH_SETUP_IE

NL80211_ATTR_UNSPEC = 0
NL80211_ATTR_WIPHY = 1
NL80211_ATTR_WIPHY_NAME = 2
NL80211_ATTR_IFINDEX = 3
NL80211_ATTR_IFNAME = 4
NL80211_ATTR_IFTYPE = 5
NL80211_ATTR_MAC = 6
NL80211_ATTR_KEY_DATA = 7
NL80211_ATTR_KEY_IDX = 8
NL80211_ATTR_KEY_CIPHER = 9
NL80211_ATTR_KEY_SEQ = 10
NL80211_ATTR_KEY_DEFAULT = 11
NL80211_ATTR_BEACON_INTERVAL = 12
NL80211_ATTR_DTIM_PERIOD = 13
NL80211_ATTR_BEACON_HEAD = 14
NL80211_ATTR_BEACON_TAIL = 15
NL80211_ATTR_STA_AID = 16
NL80211_ATTR_STA_FLAGS = 17
NL80211_ATTR_STA_LISTEN_INTERVAL = 18
NL80211_ATTR_STA_SUPPORTED_RATES = 19
NL80211_ATTR_STA_VLAN = 20
NL80211_ATTR_STA_INFO = 21
NL80211_ATTR_WIPHY_BANDS = 22
NL80211_ATTR_MNTR_FLAGS = 23
NL80211_ATTR_MESH_ID = 24
NL80211_ATTR_STA_PLINK_ACTION = 25
NL80211_ATTR_MPATH_NEXT_HOP = 26
NL80211_ATTR_MPATH_INFO = 27
NL80211_ATTR_BSS_CTS_PROT = 28
NL80211_ATTR_BSS_SHORT_PREAMBLE = 29
NL80211_ATTR_BSS_SHORT_SLOT_TIME = 30
NL80211_ATTR_HT_CAPABILITY = 31
NL80211_ATTR_SUPPORTED_IFTYPES = 32
NL80211_ATTR_REG_ALPHA2 = 33
NL80211_ATTR_REG_RULES = 34
NL80211_ATTR_MESH_CONFIG = 35
NL80211_ATTR_BSS_BASIC_RATES = 36
NL80211_ATTR_WIPHY_TXQ_PARAMS = 37
NL80211_ATTR_WIPHY_FREQ = 38
NL80211_ATTR_WIPHY_CHANNEL_TYPE = 39
NL80211_ATTR_KEY_DEFAULT_MGMT = 40
NL80211_ATTR_MGMT_SUBTYPE = 41
NL80211_ATTR_IE = 42
NL80211_ATTR_MAX_NUM_SCAN_SSIDS = 43
NL80211_ATTR_SCAN_FREQUENCIES = 44
NL80211_ATTR_SCAN_SSIDS = 45
NL80211_ATTR_GENERATION = 46
NL80211_ATTR_BSS = 47
NL80211_ATTR_REG_INITIATOR = 48
NL80211_ATTR_REG_TYPE = 49
NL80211_ATTR_SUPPORTED_COMMANDS = 50
NL80211_ATTR_FRAME = 51
NL80211_ATTR_SSID = 52
NL80211_ATTR_AUTH_TYPE = 53
NL80211_ATTR_REASON_CODE = 54
NL80211_ATTR_KEY_TYPE = 55
NL80211_ATTR_MAX_SCAN_IE_LEN = 56
NL80211_ATTR_CIPHER_SUITES = 57
NL80211_ATTR_FREQ_BEFORE = 58
NL80211_ATTR_FREQ_AFTER = 59
NL80211_ATTR_FREQ_FIXED = 60
NL80211_ATTR_WIPHY_RETRY_SHORT = 61
NL80211_ATTR_WIPHY_RETRY_LONG = 62
NL80211_ATTR_WIPHY_FRAG_THRESHOLD = 63
NL80211_ATTR_WIPHY_RTS_THRESHOLD = 64
NL80211_ATTR_TIMED_OUT = 65
NL80211_ATTR_USE_MFP = 66
NL80211_ATTR_STA_FLAGS2 = 67
NL80211_ATTR_CONTROL_PORT = 68
NL80211_ATTR_TESTDATA = 69
NL80211_ATTR_PRIVACY = 70
NL80211_ATTR_DISCONNECTED_BY_AP = 71
NL80211_ATTR_STATUS_CODE = 72
NL80211_ATTR_CIPHER_SUITES_PAIRWISE = 73
NL80211_ATTR_CIPHER_SUITE_GROUP = 74
NL80211_ATTR_WPA_VERSIONS = 75
NL80211_ATTR_AKM_SUITES = 76
NL80211_ATTR_REQ_IE = 77
NL80211_ATTR_RESP_IE = 78
NL80211_ATTR_PREV_BSSID = 79
NL80211_ATTR_KEY = 80
NL80211_ATTR_KEYS = 81
NL80211_ATTR_PID = 82
NL80211_ATTR_4ADDR = 83
NL80211_ATTR_SURVEY_INFO = 84
NL80211_ATTR_PMKID = 85
NL80211_ATTR_MAX_NUM_PMKIDS = 86
NL80211_ATTR_DURATION = 87
NL80211_ATTR_COOKIE = 88
NL80211_ATTR_WIPHY_COVERAGE_CLASS = 89
NL80211_ATTR_TX_RATES = 90
NL80211_ATTR_FRAME_MATCH = 91
NL80211_ATTR_ACK = 92
NL80211_ATTR_PS_STATE = 93
NL80211_ATTR_CQM = 94
NL80211_ATTR_LOCAL_STATE_CHANGE = 95
NL80211_ATTR_AP_ISOLATE = 96
NL80211_ATTR_WIPHY_TX_POWER_SETTING = 97
NL80211_ATTR_WIPHY_TX_POWER_LEVEL = 98
NL80211_ATTR_TX_FRAME_TYPES = 99
NL80211_ATTR_RX_FRAME_TYPES = 100
NL80211_ATTR_FRAME_TYPE = 101
NL80211_ATTR_CONTROL_PORT_ETHERTYPE = 102
NL80211_ATTR_CONTROL_PORT_NO_ENCRYPT = 103
NL80211_ATTR_SUPPORT_IBSS_RSN = 104
NL80211_ATTR_WIPHY_ANTENNA_TX = 105
NL80211_ATTR_WIPHY_ANTENNA_RX = 106
NL80211_ATTR_MCAST_RATE = 107
NL80211_ATTR_OFFCHANNEL_TX_OK = 108
NL80211_ATTR_BSS_HT_OPMODE = 109
NL80211_ATTR_KEY_DEFAULT_TYPES = 110
NL80211_ATTR_MAX_REMAIN_ON_CHANNEL_DURATION = 111
NL80211_ATTR_MESH_SETUP = 112
NL80211_ATTR_WIPHY_ANTENNA_AVAIL_TX = 113
NL80211_ATTR_WIPHY_ANTENNA_AVAIL_RX = 114
NL80211_ATTR_SUPPORT_MESH_AUTH = 115
NL80211_ATTR_STA_PLINK_STATE = 116
NL80211_ATTR_WOWLAN_TRIGGERS = 117
NL80211_ATTR_WOWLAN_TRIGGERS_SUPPORTED = 118
NL80211_ATTR_SCHED_SCAN_INTERVAL = 119
NL80211_ATTR_INTERFACE_COMBINATIONS = 120
NL80211_ATTR_SOFTWARE_IFTYPES = 121
NL80211_ATTR_REKEY_DATA = 122
NL80211_ATTR_MAX_NUM_SCHED_SCAN_SSIDS = 123
NL80211_ATTR_MAX_SCHED_SCAN_IE_LEN = 124
NL80211_ATTR_SCAN_SUPP_RATES = 125
NL80211_ATTR_HIDDEN_SSID = 126
NL80211_ATTR_IE_PROBE_RESP = 127
NL80211_ATTR_IE_ASSOC_RESP = 128
NL80211_ATTR_STA_WME = 129
NL80211_ATTR_SUPPORT_AP_UAPSD = 130
NL80211_ATTR_ROAM_SUPPORT = 131
NL80211_ATTR_SCHED_SCAN_MATCH = 132
NL80211_ATTR_MAX_MATCH_SETS = 133
NL80211_ATTR_PMKSA_CANDIDATE = 134
NL80211_ATTR_TX_NO_CCK_RATE = 135
NL80211_ATTR_TDLS_ACTION = 136
NL80211_ATTR_TDLS_DIALOG_TOKEN = 137
NL80211_ATTR_TDLS_OPERATION = 138
NL80211_ATTR_TDLS_SUPPORT = 139
NL80211_ATTR_TDLS_EXTERNAL_SETUP = 140
NL80211_ATTR_DEVICE_AP_SME = 141
NL80211_ATTR_DONT_WAIT_FOR_ACK = 142
NL80211_ATTR_FEATURE_FLAGS = 143
NL80211_ATTR_PROBE_RESP_OFFLOAD = 144
NL80211_ATTR_PROBE_RESP = 145
NL80211_ATTR_DFS_REGION = 146
NL80211_ATTR_DISABLE_HT = 147
NL80211_ATTR_HT_CAPABILITY_MASK = 148
NL80211_ATTR_NOACK_MAP = 149
NL80211_ATTR_INACTIVITY_TIMEOUT = 150
NL80211_ATTR_RX_SIGNAL_DBM = 151
NL80211_ATTR_BG_SCAN_PERIOD = 152
NL80211_ATTR_WDEV = 153
NL80211_ATTR_USER_REG_HINT_TYPE = 154
NL80211_ATTR_CONN_FAILED_REASON = 155
NL80211_ATTR_SAE_DATA = 156
NL80211_ATTR_VHT_CAPABILITY = 157
NL80211_ATTR_SCAN_FLAGS = 158
NL80211_ATTR_CHANNEL_WIDTH = 159
NL80211_ATTR_CENTER_FREQ1 = 160
NL80211_ATTR_CENTER_FREQ2 = 161
NL80211_ATTR_P2P_CTWINDOW = 162
NL80211_ATTR_P2P_OPPPS = 163
NL80211_ATTR_LOCAL_MESH_POWER_MODE = 164
NL80211_ATTR_ACL_POLICY = 165
NL80211_ATTR_MAC_ADDRS = 166
NL80211_ATTR_MAC_ACL_MAX = 167
NL80211_ATTR_RADAR_EVENT = 168
NL80211_ATTR_EXT_CAPA = 169
NL80211_ATTR_EXT_CAPA_MASK = 170
NL80211_ATTR_STA_CAPABILITY = 171
NL80211_ATTR_STA_EXT_CAPABILITY = 172
NL80211_ATTR_PROTOCOL_FEATURES = 173
NL80211_ATTR_SPLIT_WIPHY_DUMP = 174
NL80211_ATTR_DISABLE_VHT = 175
NL80211_ATTR_VHT_CAPABILITY_MASK = 176
NL80211_ATTR_MDID = 177
NL80211_ATTR_IE_RIC = 178
NL80211_ATTR_CRIT_PROT_ID = 179
NL80211_ATTR_MAX_CRIT_PROT_DURATION = 180
NL80211_ATTR_PEER_AID = 181
NL80211_ATTR_COALESCE_RULE = 182
NL80211_ATTR_CH_SWITCH_COUNT = 183
NL80211_ATTR_CH_SWITCH_BLOCK_TX = 184
NL80211_ATTR_CSA_IES = 185
NL80211_ATTR_CSA_C_OFF_BEACON = 186
NL80211_ATTR_CSA_C_OFF_PRESP = 187
NL80211_ATTR_RXMGMT_FLAGS = 188
NL80211_ATTR_STA_SUPPORTED_CHANNELS = 189
NL80211_ATTR_STA_SUPPORTED_OPER_CLASSES = 190
NL80211_ATTR_HANDLE_DFS = 191
NL80211_ATTR_SUPPORT_5_MHZ = 192
NL80211_ATTR_SUPPORT_10_MHZ = 193
NL80211_ATTR_OPMODE_NOTIF = 194
NL80211_ATTR_VENDOR_ID = 195
NL80211_ATTR_VENDOR_SUBCMD = 196
NL80211_ATTR_VENDOR_DATA = 197
NL80211_ATTR_VENDOR_EVENTS = 198
NL80211_ATTR_QOS_MAP = 199
NL80211_ATTR_MAC_HINT = 200
NL80211_ATTR_WIPHY_FREQ_HINT = 201
NL80211_ATTR_MAX_AP_ASSOC_STA = 202
NL80211_ATTR_TDLS_PEER_CAPABILITY = 203
NL80211_ATTR_IFACE_SOCKET_OWNER = 204
NL80211_ATTR_CSA_C_OFFSETS_TX = 205
NL80211_ATTR_MAX_CSA_COUNTERS = 206
NL80211_ATTR_TDLS_INITIATOR = 207
NL80211_ATTR_USE_RRM = 208
NL80211_ATTR_WIPHY_DYN_ACK = 209
NL80211_ATTR_TSID = 210
NL80211_ATTR_USER_PRIO = 211
NL80211_ATTR_ADMITTED_TIME = 212
NL80211_ATTR_SMPS_MODE = 213
NL80211_ATTR_MAX = 216

NL80211_ATTR_SCAN_GENERATION = NL80211_ATTR_GENERATION
NL80211_ATTR_MESH_PARAMS = NL80211_ATTR_MESH_CONFIG
NL80211_CMD_CONNECT = NL80211_CMD_CONNECT
NL80211_ATTR_HT_CAPABILITY = NL80211_ATTR_HT_CAPABILITY
NL80211_ATTR_BSS_BASIC_RATES = NL80211_ATTR_BSS_BASIC_RATES
NL80211_ATTR_WIPHY_TXQ_PARAMS = NL80211_ATTR_WIPHY_TXQ_PARAMS
NL80211_ATTR_WIPHY_FREQ = NL80211_ATTR_WIPHY_FREQ
NL80211_ATTR_WIPHY_CHANNEL_TYPE = NL80211_ATTR_WIPHY_CHANNEL_TYPE
NL80211_ATTR_MGMT_SUBTYPE = NL80211_ATTR_MGMT_SUBTYPE
NL80211_ATTR_IE = NL80211_ATTR_IE
NL80211_ATTR_REG_INITIATOR = NL80211_ATTR_REG_INITIATOR
NL80211_ATTR_REG_TYPE = NL80211_ATTR_REG_TYPE
NL80211_ATTR_FRAME = NL80211_ATTR_FRAME
NL80211_ATTR_SSID = NL80211_ATTR_SSID
NL80211_ATTR_AUTH_TYPE = NL80211_ATTR_AUTH_TYPE
NL80211_ATTR_REASON_CODE = NL80211_ATTR_REASON_CODE
NL80211_ATTR_CIPHER_SUITES_PAIRWISE = NL80211_ATTR_CIPHER_SUITES_PAIRWISE
NL80211_ATTR_CIPHER_SUITE_GROUP = NL80211_ATTR_CIPHER_SUITE_GROUP
NL80211_ATTR_WPA_VERSIONS = NL80211_ATTR_WPA_VERSIONS
NL80211_ATTR_AKM_SUITES = NL80211_ATTR_AKM_SUITES
NL80211_ATTR_KEY = NL80211_ATTR_KEY
NL80211_ATTR_KEYS = NL80211_ATTR_KEYS
NL80211_ATTR_FEATURE_FLAGS = NL80211_ATTR_FEATURE_FLAGS
NL80211_MAX_SUPP_RATES = 32
NL80211_MAX_SUPP_HT_RATES = 77
NL80211_MAX_SUPP_REG_RULES = 32
NL80211_TKIP_DATA_OFFSET_ENCR_KEY = 0
NL80211_TKIP_DATA_OFFSET_TX_MIC_KEY = 16
NL80211_TKIP_DATA_OFFSET_RX_MIC_KEY = 24
NL80211_HT_CAPABILITY_LEN = 26
NL80211_VHT_CAPABILITY_LEN = 12
NL80211_MAX_NR_CIPHER_SUITES = 5
NL80211_MAX_NR_AKM_SUITES = 2
NL80211_MIN_REMAIN_ON_CHANNEL_TIME = 10
NL80211_SCAN_RSSI_THOLD_OFF = -300
NL80211_CQM_TXE_MAX_INTVL = 1800

NL80211_IFTYPE_UNSPECIFIED = 0
NL80211_IFTYPE_ADHOC = 1
NL80211_IFTYPE_STATION = 2
NL80211_IFTYPE_AP = 3
NL80211_IFTYPE_AP_VLAN = 4
NL80211_IFTYPE_WDS = 5
NL80211_IFTYPE_MONITOR = 6
NL80211_IFTYPE_MESH_POINT = 7
NL80211_IFTYPE_P2P_CLIENT = 8
NL80211_IFTYPE_P2P_GO = 9
NL80211_IFTYPE_P2P_DEVICE = 10
NUM_NL80211_IFTYPES = 12
NL80211_IFTYPE_MAX = NUM_NL80211_IFTYPES - 1

NL80211_STA_FLAG_INVALID = 0
NL80211_STA_FLAG_AUTHORIZED = 1
NL80211_STA_FLAG_SHORT_PREAMBLE = 2
NL80211_STA_FLAG_WME = 3
NL80211_STA_FLAG_MFP = 4
NL80211_STA_FLAG_AUTHENTICATED = 5
NL80211_STA_FLAG_TDLS_PEER = 6
NL80211_STA_FLAG_ASSOCIATED = 7
NL80211_STA_FLAG_MAX = 7

NL80211_STA_FLAG_MAX_OLD_API = NL80211_STA_FLAG_TDLS_PEER

NL80211_RATE_INFO_INVALID = 0
NL80211_RATE_INFO_BITRATE = 1
NL80211_RATE_INFO_MCS = 2
NL80211_RATE_INFO_40_MHZ_WIDTH = 3
NL80211_RATE_INFO_SHORT_GI = 4
NL80211_RATE_INFO_BITRATE32 = 5
NL80211_RATE_INFO_VHT_MCS = 6
NL80211_RATE_INFO_VHT_NSS = 7
NL80211_RATE_INFO_80_MHZ_WIDTH = 8
NL80211_RATE_INFO_80P80_MHZ_WIDTH = 9
NL80211_RATE_INFO_160_MHZ_WIDTH = 10
NL80211_RATE_INFO_MAX = 10

NL80211_STA_BSS_PARAM_INVALID = 0
NL80211_STA_BSS_PARAM_CTS_PROT = 1
NL80211_STA_BSS_PARAM_SHORT_PREAMBLE = 2
NL80211_STA_BSS_PARAM_SHORT_SLOT_TIME = 3
NL80211_STA_BSS_PARAM_DTIM_PERIOD = 4
NL80211_STA_BSS_PARAM_BEACON_INTERVAL = 5
NL80211_STA_BSS_PARAM_MAX = 5

NL80211_STA_INFO_INVALID = 0
NL80211_STA_INFO_INACTIVE_TIME = 1
NL80211_STA_INFO_RX_BYTES = 2
NL80211_STA_INFO_TX_BYTES = 3
NL80211_STA_INFO_LLID = 4
NL80211_STA_INFO_PLID = 5
NL80211_STA_INFO_PLINK_STATE = 6
NL80211_STA_INFO_SIGNAL = 7
NL80211_STA_INFO_TX_BITRATE = 8
NL80211_STA_INFO_RX_PACKETS = 9
NL80211_STA_INFO_TX_PACKETS = 10
NL80211_STA_INFO_TX_RETRIES = 11
NL80211_STA_INFO_TX_FAILED = 12
NL80211_STA_INFO_SIGNAL_AVG = 13
NL80211_STA_INFO_RX_BITRATE = 14
NL80211_STA_INFO_BSS_PARAM = 15
NL80211_STA_INFO_CONNECTED_TIME = 16
NL80211_STA_INFO_STA_FLAGS = 17
NL80211_STA_INFO_BEACON_LOSS = 18
NL80211_STA_INFO_T_OFFSET = 19
NL80211_STA_INFO_LOCAL_PM = 20
NL80211_STA_INFO_PEER_PM = 21
NL80211_STA_INFO_NONPEER_PM = 22
NL80211_STA_INFO_RX_BYTES64 = 23
NL80211_STA_INFO_TX_BYTES64 = 24
NL80211_STA_INFO_CHAIN_SIGNAL = 25
NL80211_STA_INFO_CHAIN_SIGNAL_AVG = 26
NL80211_STA_INFO_EXPECTED_THROUGHPUT = 27
NL80211_STA_INFO_MAX = 27

NL80211_MPATH_FLAG_ACTIVE = 1 << 0
NL80211_MPATH_FLAG_RESOLVING = 1 << 1
NL80211_MPATH_FLAG_SN_VALID = 1 << 2
NL80211_MPATH_FLAG_FIXED = 1 << 3
NL80211_MPATH_FLAG_RESOLVED = 1 << 4

NL80211_MPATH_INFO_INVALID = 0
NL80211_MPATH_INFO_FRAME_QLEN = 1
NL80211_MPATH_INFO_SN = 2
NL80211_MPATH_INFO_METRIC = 3
NL80211_MPATH_INFO_EXPTIME = 4
NL80211_MPATH_INFO_FLAGS = 5
NL80211_MPATH_INFO_DISCOVERY_TIMEOUT = 6
NL80211_MPATH_INFO_DISCOVERY_RETRIES = 7
NL80211_MPATH_INFO_MAX = 7

NL80211_BAND_ATTR_INVALID = 0
NL80211_BAND_ATTR_FREQS = 1
NL80211_BAND_ATTR_RATES = 2
NL80211_BAND_ATTR_HT_MCS_SET = 3
NL80211_BAND_ATTR_HT_CAPA = 4
NL80211_BAND_ATTR_HT_AMPDU_FACTOR = 5
NL80211_BAND_ATTR_HT_AMPDU_DENSITY = 6
NL80211_BAND_ATTR_VHT_MCS_SET = 7
NL80211_BAND_ATTR_VHT_CAPA = 8
NL80211_BAND_ATTR_MAX = 8

NL80211_BAND_ATTR_HT_CAPA = NL80211_BAND_ATTR_HT_CAPA

NL80211_FREQUENCY_ATTR_INVALID = 0
NL80211_FREQUENCY_ATTR_FREQ = 1
NL80211_FREQUENCY_ATTR_DISABLED = 2
NL80211_FREQUENCY_ATTR_NO_IR = 3
__NL80211_FREQUENCY_ATTR_NO_IBSS = 4
NL80211_FREQUENCY_ATTR_RADAR = 5
NL80211_FREQUENCY_ATTR_MAX_TX_POWER = 6
NL80211_FREQUENCY_ATTR_DFS_STATE = 7
NL80211_FREQUENCY_ATTR_DFS_TIME = 8
NL80211_FREQUENCY_ATTR_NO_HT40_MINUS = 9
NL80211_FREQUENCY_ATTR_NO_HT40_PLUS = 10
NL80211_FREQUENCY_ATTR_NO_80MHZ = 11
NL80211_FREQUENCY_ATTR_NO_160MHZ = 12
NL80211_FREQUENCY_ATTR_DFS_CAC_TIME = 13
NL80211_FREQUENCY_ATTR_INDOOR_ONLY = 14
NL80211_FREQUENCY_ATTR_GO_CONCURRENT = 15
NL80211_FREQUENCY_ATTR_NO_20MHZ = 16
NL80211_FREQUENCY_ATTR_NO_10MHZ = 17
NL80211_FREQUENCY_ATTR_MAX = 17

NL80211_FREQUENCY_ATTR_MAX_TX_POWER = NL80211_FREQUENCY_ATTR_MAX_TX_POWER
NL80211_FREQUENCY_ATTR_PASSIVE_SCAN = NL80211_FREQUENCY_ATTR_NO_IR
NL80211_FREQUENCY_ATTR_NO_IBSS = NL80211_FREQUENCY_ATTR_NO_IR
NL80211_FREQUENCY_ATTR_NO_IR = NL80211_FREQUENCY_ATTR_NO_IR

NL80211_BITRATE_ATTR_INVALID = 0
NL80211_BITRATE_ATTR_RATE = 1
NL80211_BITRATE_ATTR_2GHZ_SHORTPREAMBLE = 2
NL80211_BITRATE_ATTR_MAX = 2

NL80211_REGDOM_SET_BY_CORE = 0
NL80211_REGDOM_SET_BY_USER = 1
NL80211_REGDOM_SET_BY_DRIVER = 2
NL80211_REGDOM_SET_BY_COUNTRY_IE = 3

NL80211_REGDOM_TYPE_COUNTRY = 0
NL80211_REGDOM_TYPE_WORLD = 1
NL80211_REGDOM_TYPE_CUSTOM_WORLD = 2
NL80211_REGDOM_TYPE_INTERSECTION = 3

NL80211_REG_RULE_ATTR_INVALID = 0
NL80211_ATTR_REG_RULE_FLAGS = 1
NL80211_ATTR_FREQ_RANGE_START = 2
NL80211_ATTR_FREQ_RANGE_END = 3
NL80211_ATTR_FREQ_RANGE_MAX_BW = 4
NL80211_ATTR_POWER_RULE_MAX_ANT_GAIN = 5
NL80211_ATTR_POWER_RULE_MAX_EIRP = 6
NL80211_ATTR_DFS_CAC_TIME = 7
NL80211_REG_RULE_ATTR_MAX = 7

NL80211_SCHED_SCAN_MATCH_ATTR_INVALID = 0
NL80211_SCHED_SCAN_MATCH_ATTR_SSID = 1
NL80211_SCHED_SCAN_MATCH_ATTR_RSSI = 2
NL80211_SCHED_SCAN_MATCH_ATTR_MAX = 2

NL80211_ATTR_SCHED_SCAN_MATCH_SSID = NL80211_SCHED_SCAN_MATCH_ATTR_SSID

NL80211_RRF_NO_OFDM = 1 << 0
NL80211_RRF_NO_CCK = 1 << 1
NL80211_RRF_NO_INDOOR = 1 << 2
NL80211_RRF_NO_OUTDOOR = 1 << 3
NL80211_RRF_DFS = 1 << 4
NL80211_RRF_PTP_ONLY = 1 << 5
NL80211_RRF_PTMP_ONLY = 1 << 6
NL80211_RRF_NO_IR = 1 << 7
__NL80211_RRF_NO_IBSS = 1 << 8
NL80211_RRF_AUTO_BW = 1 << 11

NL80211_RRF_PASSIVE_SCAN = NL80211_RRF_NO_IR
NL80211_RRF_NO_IBSS = NL80211_RRF_NO_IR
NL80211_RRF_NO_IR = NL80211_RRF_NO_IR
NL80211_RRF_NO_IR_ALL = NL80211_RRF_NO_IR | __NL80211_RRF_NO_IBSS

NL80211_DFS_UNSET = 0
NL80211_DFS_FCC = 1
NL80211_DFS_ETSI = 2
NL80211_DFS_JP = 3

NL80211_USER_REG_HINT_USER = 0
NL80211_USER_REG_HINT_CELL_BASE = 1
NL80211_USER_REG_HINT_INDOOR = 2

NL80211_SURVEY_INFO_INVALID = 0
NL80211_SURVEY_INFO_FREQUENCY = 1
NL80211_SURVEY_INFO_NOISE = 2
NL80211_SURVEY_INFO_IN_USE = 3
NL80211_SURVEY_INFO_CHANNEL_TIME = 4
NL80211_SURVEY_INFO_CHANNEL_TIME_BUSY = 5
NL80211_SURVEY_INFO_CHANNEL_TIME_EXT_BUSY = 6
NL80211_SURVEY_INFO_CHANNEL_TIME_RX = 7
NL80211_SURVEY_INFO_CHANNEL_TIME_TX = 8
NL80211_SURVEY_INFO_MAX = 8

NL80211_MNTR_FLAG_INVALID = 0
NL80211_MNTR_FLAG_FCSFAIL = 1
NL80211_MNTR_FLAG_PLCPFAIL = 2
NL80211_MNTR_FLAG_CONTROL = 3
NL80211_MNTR_FLAG_OTHER_BSS = 4
NL80211_MNTR_FLAG_COOK_FRAMES = 5
NL80211_MNTR_FLAG_ACTIVE = 6
NL80211_MNTR_FLAG_MAX = 6

NL80211_MESH_POWER_UNKNOWN = 0
NL80211_MESH_POWER_ACTIVE = 1
NL80211_MESH_POWER_LIGHT_SLEEP = 2
NL80211_MESH_POWER_DEEP_SLEEP = 3
NL80211_MESH_POWER_MAX = 3

NL80211_MESHCONF_INVALID = 0
NL80211_MESHCONF_RETRY_TIMEOUT = 1
NL80211_MESHCONF_CONFIRM_TIMEOUT = 2
NL80211_MESHCONF_HOLDING_TIMEOUT = 3
NL80211_MESHCONF_MAX_PEER_LINKS = 4
NL80211_MESHCONF_MAX_RETRIES = 5
NL80211_MESHCONF_TTL = 6
NL80211_MESHCONF_AUTO_OPEN_PLINKS = 7
NL80211_MESHCONF_HWMP_MAX_PREQ_RETRIES = 8
NL80211_MESHCONF_PATH_REFRESH_TIME = 9
NL80211_MESHCONF_MIN_DISCOVERY_TIMEOUT = 10
NL80211_MESHCONF_HWMP_ACTIVE_PATH_TIMEOUT = 11
NL80211_MESHCONF_HWMP_PREQ_MIN_INTERVAL = 12
NL80211_MESHCONF_HWMP_NET_DIAM_TRVS_TIME = 13
NL80211_MESHCONF_HWMP_ROOTMODE = 14
NL80211_MESHCONF_ELEMENT_TTL = 15
NL80211_MESHCONF_HWMP_RANN_INTERVAL = 16
NL80211_MESHCONF_GATE_ANNOUNCEMENTS = 17
NL80211_MESHCONF_HWMP_PERR_MIN_INTERVAL = 18
NL80211_MESHCONF_FORWARDING = 19
NL80211_MESHCONF_RSSI_THRESHOLD = 20
NL80211_MESHCONF_SYNC_OFFSET_MAX_NEIGHBOR = 21
NL80211_MESHCONF_HT_OPMODE = 22
NL80211_MESHCONF_HWMP_PATH_TO_ROOT_TIMEOUT = 23
NL80211_MESHCONF_HWMP_ROOT_INTERVAL = 24
NL80211_MESHCONF_HWMP_CONFIRMATION_INTERVAL = 25
NL80211_MESHCONF_POWER_MODE = 26
NL80211_MESHCONF_AWAKE_WINDOW = 27
NL80211_MESHCONF_PLINK_TIMEOUT = 28
NL80211_MESHCONF_ATTR_MAX = 28

NL80211_TXQ_ATTR_INVALID = 0
NL80211_TXQ_ATTR_AC = 1
NL80211_TXQ_ATTR_TXOP = 2
NL80211_TXQ_ATTR_CWMIN = 3
NL80211_TXQ_ATTR_CWMAX = 4
NL80211_TXQ_ATTR_AIFS = 5
NL80211_TXQ_ATTR_MAX = 5

NL80211_AC_VO = 0
NL80211_AC_VI = 1
NL80211_AC_BE = 2
NL80211_AC_BK = 3
NL80211_NUM_ACS = 4

NL80211_TXQ_ATTR_QUEUE = NL80211_TXQ_ATTR_AC
NL80211_TXQ_Q_VO = NL80211_AC_VO
NL80211_TXQ_Q_VI = NL80211_AC_VI
NL80211_TXQ_Q_BE = NL80211_AC_BE
NL80211_TXQ_Q_BK = NL80211_AC_BK

NL80211_CHAN_NO_HT = 0
NL80211_CHAN_HT20 = 1
NL80211_CHAN_HT40MINUS = 2
NL80211_CHAN_HT40PLUS = 3

NL80211_CHAN_WIDTH_20_NOHT = 0
NL80211_CHAN_WIDTH_20 = 1
NL80211_CHAN_WIDTH_40 = 2
NL80211_CHAN_WIDTH_80 = 3
NL80211_CHAN_WIDTH_80P80 = 4
NL80211_CHAN_WIDTH_160 = 5
NL80211_CHAN_WIDTH_5 = 6
NL80211_CHAN_WIDTH_10 = 7

NL80211_BSS_CHAN_WIDTH_20 = 0
NL80211_BSS_CHAN_WIDTH_10 = 1
NL80211_BSS_CHAN_WIDTH_5 = 2

NL80211_BSS_INVALID = 0
NL80211_BSS_BSSID = 1
NL80211_BSS_FREQUENCY = 2
NL80211_BSS_TSF = 3
NL80211_BSS_BEACON_INTERVAL = 4
NL80211_BSS_CAPABILITY = 5
NL80211_BSS_INFORMATION_ELEMENTS = 6
NL80211_BSS_SIGNAL_MBM = 7
NL80211_BSS_SIGNAL_UNSPEC = 8
NL80211_BSS_STATUS = 9
NL80211_BSS_SEEN_MS_AGO = 10
NL80211_BSS_BEACON_IES = 11
NL80211_BSS_CHAN_WIDTH = 12
NL80211_BSS_BEACON_TSF = 13
NL80211_BSS_PRESP_DATA = 14
NL80211_BSS_MAX = 14

NL80211_BSS_STATUS_AUTHENTICATED = 0
NL80211_BSS_STATUS_ASSOCIATED = 1
NL80211_BSS_STATUS_IBSS_JOINED = 2

NL80211_AUTHTYPE_OPEN_SYSTEM = 0
NL80211_AUTHTYPE_SHARED_KEY = 1
NL80211_AUTHTYPE_FT = 2
NL80211_AUTHTYPE_NETWORK_EAP = 3
NL80211_AUTHTYPE_SAE = 4
NL80211_AUTHTYPE_MAX = 4
NL80211_AUTHTYPE_AUTOMATIC = 5

NL80211_KEYTYPE_GROUP = 0
NL80211_KEYTYPE_PAIRWISE = 1
NL80211_KEYTYPE_PEERKEY = 2
NUM_NL80211_KEYTYPES = 3

NL80211_MFP_NO = 0
NL80211_MFP_REQUIRED = 1

NL80211_WPA_VERSION_1 = 1 << 0
NL80211_WPA_VERSION_2 = 1 << 1

NL80211_KEY_DEFAULT_TYPE_INVALID = 0
NL80211_KEY_DEFAULT_TYPE_UNICAST = 1
NL80211_KEY_DEFAULT_TYPE_MULTICAST = 2
NUM_NL80211_KEY_DEFAULT_TYPES = 3

NL80211_KEY_INVALID = 0
NL80211_KEY_DATA = 1
NL80211_KEY_IDX = 2
NL80211_KEY_CIPHER = 3
NL80211_KEY_SEQ = 4
NL80211_KEY_DEFAULT = 5
NL80211_KEY_DEFAULT_MGMT = 6
NL80211_KEY_TYPE = 7
NL80211_KEY_DEFAULT_TYPES = 8
NL80211_KEY_MAX = 8

NL80211_TXRATE_INVALID = 0
NL80211_TXRATE_LEGACY = 1
NL80211_TXRATE_HT = 2
NL80211_TXRATE_VHT = 3
NL80211_TXRATE_GI = 4
NL80211_TXRATE_MAX = 4

NL80211_TXRATE_MCS = NL80211_TXRATE_HT
NL80211_VHT_NSS_MAX = 8

NL80211_TXRATE_DEFAULT_GI = 0
NL80211_TXRATE_FORCE_SGI = 1
NL80211_TXRATE_FORCE_LGI = 2

NL80211_BAND_2GHZ = 0
NL80211_BAND_5GHZ = 1
NL80211_BAND_60GHZ = 2

NL80211_PS_DISABLED = 0
NL80211_PS_ENABLED = 1

NL80211_ATTR_CQM_INVALID = 0
NL80211_ATTR_CQM_RSSI_THOLD = 1
NL80211_ATTR_CQM_RSSI_HYST = 2
NL80211_ATTR_CQM_RSSI_THRESHOLD_EVENT = 3
NL80211_ATTR_CQM_PKT_LOSS_EVENT = 4
NL80211_ATTR_CQM_TXE_RATE = 5
NL80211_ATTR_CQM_TXE_PKTS = 6
NL80211_ATTR_CQM_TXE_INTVL = 7
NL80211_ATTR_CQM_MAX = 8

NL80211_CQM_RSSI_THRESHOLD_EVENT_LOW = 0
NL80211_CQM_RSSI_THRESHOLD_EVENT_HIGH = 1
NL80211_CQM_RSSI_BEACON_LOSS_EVENT = 2

NL80211_TX_POWER_AUTOMATIC = 0
NL80211_TX_POWER_LIMITED = 1
NL80211_TX_POWER_FIXED = 2

NL80211_PKTPAT_INVALID = 0
NL80211_PKTPAT_MASK = 1
NL80211_PKTPAT_PATTERN = 2
NL80211_PKTPAT_OFFSET = 3
NUM_NL80211_PKTPAT = 4
MAX_NL80211_PKTPAT = 3

NL80211_WOWLAN_PKTPAT_INVALID = NL80211_PKTPAT_INVALID
NL80211_WOWLAN_PKTPAT_MASK = NL80211_PKTPAT_MASK
NL80211_WOWLAN_PKTPAT_PATTERN = NL80211_PKTPAT_PATTERN
NL80211_WOWLAN_PKTPAT_OFFSET = NL80211_PKTPAT_OFFSET
NUM_NL80211_WOWLAN_PKTPAT = NUM_NL80211_PKTPAT
MAX_NL80211_WOWLAN_PKTPAT = MAX_NL80211_PKTPAT

NL80211_WOWLAN_TRIG_INVALID = 0
NL80211_WOWLAN_TRIG_ANY = 1
NL80211_WOWLAN_TRIG_DISCONNECT = 2
NL80211_WOWLAN_TRIG_MAGIC_PKT = 3
NL80211_WOWLAN_TRIG_PKT_PATTERN = 4
NL80211_WOWLAN_TRIG_GTK_REKEY_SUPPORTED = 5
NL80211_WOWLAN_TRIG_GTK_REKEY_FAILURE = 6
NL80211_WOWLAN_TRIG_EAP_IDENT_REQUEST = 7
NL80211_WOWLAN_TRIG_4WAY_HANDSHAKE = 8
NL80211_WOWLAN_TRIG_RFKILL_RELEASE = 9
NL80211_WOWLAN_TRIG_WAKEUP_PKT_80211 = 10
NL80211_WOWLAN_TRIG_WAKEUP_PKT_80211_LEN = 11
NL80211_WOWLAN_TRIG_WAKEUP_PKT_8023 = 12
NL80211_WOWLAN_TRIG_WAKEUP_PKT_8023_LEN = 13
NL80211_WOWLAN_TRIG_TCP_CONNECTION = 14
NL80211_WOWLAN_TRIG_WAKEUP_TCP_MATCH = 15
NL80211_WOWLAN_TRIG_WAKEUP_TCP_CONNLOST = 16
NL80211_WOWLAN_TRIG_WAKEUP_TCP_NOMORETOKENS = 17
NUM_NL80211_WOWLAN_TRIG = 20
MAX_NL80211_WOWLAN_TRIG = 19

NL80211_WOWLAN_TCP_INVALID = 0
NL80211_WOWLAN_TCP_SRC_IPV4 = 1
NL80211_WOWLAN_TCP_DST_IPV4 = 2
NL80211_WOWLAN_TCP_DST_MAC = 3
NL80211_WOWLAN_TCP_SRC_PORT = 4
NL80211_WOWLAN_TCP_DST_PORT = 5
NL80211_WOWLAN_TCP_DATA_PAYLOAD = 6
NL80211_WOWLAN_TCP_DATA_PAYLOAD_SEQ = 7
NL80211_WOWLAN_TCP_DATA_PAYLOAD_TOKEN = 8
NL80211_WOWLAN_TCP_DATA_INTERVAL = 9
NL80211_WOWLAN_TCP_WAKE_PAYLOAD = 10
NL80211_WOWLAN_TCP_WAKE_MASK = 11
NUM_NL80211_WOWLAN_TCP = 12
MAX_NL80211_WOWLAN_TCP = 11

NL80211_COALESCE_RULE_INVALID = 0
NL80211_ATTR_COALESCE_RULE_DELAY = 1
NL80211_ATTR_COALESCE_RULE_CONDITION = 2
NL80211_ATTR_COALESCE_RULE_PKT_PATTERN = 3
NUM_NL80211_ATTR_COALESCE_RULE = 4
NL80211_ATTR_COALESCE_RULE_MAX = 3

NL80211_COALESCE_CONDITION_MATCH = 0
NL80211_COALESCE_CONDITION_NO_MATCH = 1

NL80211_IFACE_LIMIT_UNSPEC = 0
NL80211_IFACE_LIMIT_MAX = 1
NL80211_IFACE_LIMIT_TYPES = 2
NUM_NL80211_IFACE_LIMIT = 3
MAX_NL80211_IFACE_LIMIT = 2

NL80211_IFACE_COMB_UNSPEC = 0
NL80211_IFACE_COMB_LIMITS = 1
NL80211_IFACE_COMB_MAXNUM = 2
NL80211_IFACE_COMB_STA_AP_BI_MATCH = 3
NL80211_IFACE_COMB_NUM_CHANNELS = 4
NL80211_IFACE_COMB_RADAR_DETECT_WIDTHS = 5
NL80211_IFACE_COMB_RADAR_DETECT_REGIONS = 6
NUM_NL80211_IFACE_COMB = 7
MAX_NL80211_IFACE_COMB = 6

NL80211_PLINK_LISTEN = 0
NL80211_PLINK_OPN_SNT = 1
NL80211_PLINK_OPN_RCVD = 2
NL80211_PLINK_CNF_RCVD = 3
NL80211_PLINK_ESTAB = 4
NL80211_PLINK_HOLDING = 5
NL80211_PLINK_BLOCKED = 6
NUM_NL80211_PLINK_STATES = 7
MAX_NL80211_PLINK_STATES = 6

NL80211_PLINK_ACTION_NO_ACTION = 0
NL80211_PLINK_ACTION_OPEN = 1
NL80211_PLINK_ACTION_BLOCK = 2
NUM_NL80211_PLINK_ACTIONS = 3

NL80211_KCK_LEN = 16
NL80211_KEK_LEN = 16
NL80211_REPLAY_CTR_LEN = 8

NL80211_REKEY_DATA_INVALID = 0
NL80211_REKEY_DATA_KEK = 1
NL80211_REKEY_DATA_KCK = 2
NL80211_REKEY_DATA_REPLAY_CTR = 3
NUM_NL80211_REKEY_DATA = 4
MAX_NL80211_REKEY_DATA = 3

NL80211_HIDDEN_SSID_NOT_IN_USE = 0
NL80211_HIDDEN_SSID_ZERO_LEN = 1
NL80211_HIDDEN_SSID_ZERO_CONTENTS = 2

NL80211_STA_WME_INVALID = 0
NL80211_STA_WME_UAPSD_QUEUES = 1
NL80211_STA_WME_MAX_SP = 2
NL80211_STA_WME_MAX = 2

NL80211_PMKSA_CANDIDATE_INVALID = 0
NL80211_PMKSA_CANDIDATE_INDEX = 1
NL80211_PMKSA_CANDIDATE_BSSID = 2
NL80211_PMKSA_CANDIDATE_PREAUTH = 3
NUM_NL80211_PMKSA_CANDIDATE = 4
MAX_NL80211_PMKSA_CANDIDATE = 3

NL80211_TDLS_DISCOVERY_REQ = 0
NL80211_TDLS_SETUP = 1
NL80211_TDLS_TEARDOWN = 2
NL80211_TDLS_ENABLE_LINK = 3
NL80211_TDLS_DISABLE_LINK = 4

NL80211_FEATURE_SK_TX_STATUS = 1 << 0
NL80211_FEATURE_HT_IBSS = 1 << 1
NL80211_FEATURE_INACTIVITY_TIMER = 1 << 2
NL80211_FEATURE_CELL_BASE_REG_HINTS = 1 << 3
NL80211_FEATURE_P2P_DEVICE_NEEDS_CHANNEL = 1 << 4
NL80211_FEATURE_SAE = 1 << 5
NL80211_FEATURE_LOW_PRIORITY_SCAN = 1 << 6
NL80211_FEATURE_SCAN_FLUSH = 1 << 7
NL80211_FEATURE_AP_SCAN = 1 << 8
NL80211_FEATURE_VIF_TXPOWER = 1 << 9
NL80211_FEATURE_NEED_OBSS_SCAN = 1 << 10
NL80211_FEATURE_P2P_GO_CTWIN = 1 << 11
NL80211_FEATURE_P2P_GO_OPPPS = 1 << 12
NL80211_FEATURE_ADVERTISE_CHAN_LIMITS = 1 << 14
NL80211_FEATURE_FULL_AP_CLIENT_STATE = 1 << 15
NL80211_FEATURE_USERSPACE_MPM = 1 << 16
NL80211_FEATURE_ACTIVE_MONITOR = 1 << 17
NL80211_FEATURE_AP_MODE_CHAN_WIDTH_CHANGE = 1 << 18
NL80211_FEATURE_DS_PARAM_SET_IE_IN_PROBES = 1 << 19
NL80211_FEATURE_WFA_TPC_IE_IN_PROBES = 1 << 20
NL80211_FEATURE_QUIET = 1 << 21
NL80211_FEATURE_TX_POWER_INSERTION = 1 << 22
NL80211_FEATURE_ACKTO_ESTIMATION = 1 << 23
NL80211_FEATURE_STATIC_SMPS = 1 << 24
NL80211_FEATURE_DYNAMIC_SMPS = 1 << 25

NL80211_PROBE_RESP_OFFLOAD_SUPPORT_WPS = 1 << 0
NL80211_PROBE_RESP_OFFLOAD_SUPPORT_WPS2 = 1 << 1
NL80211_PROBE_RESP_OFFLOAD_SUPPORT_P2P = 1 << 2
NL80211_PROBE_RESP_OFFLOAD_SUPPORT_80211U = 1 << 3

NL80211_CONN_FAIL_MAX_CLIENTS = 0
NL80211_CONN_FAIL_BLOCKED_CLIENT = 1

NL80211_SCAN_FLAG_LOW_PRIORITY = 1 << 0
NL80211_SCAN_FLAG_FLUSH = 1 << 1
NL80211_SCAN_FLAG_AP = 1 << 2

NL80211_ACL_POLICY_ACCEPT_UNLESS_LISTED = 0
NL80211_ACL_POLICY_DENY_UNLESS_LISTED = 1

NL80211_SMPS_OFF = 0
NL80211_SMPS_STATIC = 1
NL80211_SMPS_DYNAMIC = 2
NL80211_SMPS_MAX = 2

NL80211_RADAR_DETECTED = 0
NL80211_RADAR_CAC_FINISHED = 1
NL80211_RADAR_CAC_ABORTED = 2
NL80211_RADAR_NOP_FINISHED = 3

NL80211_DFS_USABLE = 0
NL80211_DFS_UNAVAILABLE = 1
NL80211_DFS_AVAILABLE = 2

NL80211_PROTOCOL_FEATURE_SPLIT_WIPHY_DUMP = 1 << 0

NL80211_CRIT_PROTO_UNSPEC = 0
NL80211_CRIT_PROTO_DHCP = 1
NL80211_CRIT_PROTO_EAPOL = 2
NL80211_CRIT_PROTO_APIPA = 3
NUM_NL80211_CRIT_PROTO = 4

NL80211_CRIT_PROTO_MAX_DURATION = 5000

NL80211_RXMGMT_FLAG_ANSWERED = 1 << 0

NL80211_VENDOR_ID_IS_LINUX = 0x80000000

NL80211_TDLS_PEER_HT = 1 << 0
NL80211_TDLS_PEER_VHT = 1 << 1
NL80211_TDLS_PEER_WMM = 1 << 2