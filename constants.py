from enum import StrEnum
from enum import IntEnum


class TxPower(StrEnum):
    HIGH = "H"
    MEDIUM = "M"
    LOW = "L"


class TxBandwidth(IntEnum):
    BW_12_5 = 12500
    BW_25 = 25000


class DmrColorCode(IntEnum):
    CC0 = 0
    CC1 = 1
    CC2 = 2
    CC3 = 3
    CC4 = 4
    CC5 = 5
    CC6 = 6
    CC7 = 7
    CC8 = 8
    CC9 = 9
    CC10 = 10
    CC11 = 11
    CC12 = 12
    CC13 = 13
    CC14 = 14
    CC15 = 15


class OnOff(IntEnum):
    ON = 1
    OFF = 0


class Mode(IntEnum):
    FM = 0
    AM = 1


class RepeaterMode(StrEnum):
    ANALOG = "analog"
    DMR = "DMR"
    NXDN = "NXDN"
    P25 = "P25"
    TETRA = "tetra"


class RepeaterTone(StrEnum):
    TONE_NONE = ""
    TONE_67_0 = "67.0"
    TONE_69_3 = "69.3"
    TONE_71_9 = "71.9"
    TONE_74_4 = "74.4"
    TONE_77_0 = "77.0"
    TONE_79_7 = "79.7"
    TONE_82_5 = "82.5"
    TONE_85_4 = "85.4"
    TONE_88_5 = "88.5"
    TONE_91_5 = "91.5"
    TONE_94_8 = "94.8"
    TONE_97_4 = "97.4"
    TONE_100_0 = "100.0"
    TONE_103_5 = "103.5"
    TONE_107_2 = "107.2"
    TONE_110_9 = "110.9"
    TONE_114_8 = "114.8"
    TONE_118_8 = "118.8"
    TONE_123_0 = "123.0"
    TONE_127_3 = "127.3"
    TONE_131_8 = "131.8"
    TONE_136_5 = "136.5"
    TONE_141_3 = "141.3"
    TONE_146_2 = "146.2"
    TONE_150_0 = "150.0"
    TONE_151_4 = "151.4"
    TONE_156_7 = "156.7"
    TONE_159_8 = "159.8"
    TONE_162_2 = "162.2"
    TONE_165_5 = "165.5"
    TONE_167_9 = "167.9"
    TONE_171_3 = "171.3"
    TONE_173_8 = "173.8"
    TONE_177_3 = "177.3"
    TONE_179_9 = "179.9"
    TONE_183_5 = "183.5"
    TONE_186_2 = "186.2"
    TONE_189_9 = "189.9"
    TONE_192_8 = "192.8"
    TONE_196_6 = "196.6"
    TONE_199_5 = "199.5"
    TONE_203_5 = "203.5"
    TONE_206_5 = "206.5"
    TONE_210_7 = "210.7"
    TONE_218_1 = "218.1"
    TONE_225_7 = "225.7"
    TONE_229_1 = "229.1"
    TONE_233_6 = "233.6"
    TONE_241_8 = "241.8"
    TONE_250_3 = "250.3"
    TONE_254_1 = "254.1"


class VgcTone(IntEnum):
    TONE_NONE = 0
    TONE_67_0 = 6700
    TONE_69_3 = 6930
    TONE_71_9 = 7190
    TONE_74_4 = 7440
    TONE_77_0 = 7700
    TONE_79_7 = 7970
    TONE_82_5 = 8250
    TONE_85_4 = 8540
    TONE_88_5 = 8850
    TONE_91_5 = 9150
    TONE_94_8 = 9480
    TONE_97_4 = 9740
    TONE_100_0 = 10000
    TONE_103_5 = 10350
    TONE_107_2 = 10720
    TONE_110_9 = 11090
    TONE_114_8 = 11480
    TONE_118_8 = 11880
    TONE_123_0 = 12300
    TONE_127_3 = 12730
    TONE_131_8 = 13180
    TONE_136_5 = 13650
    TONE_141_3 = 14130
    TONE_146_2 = 14620
    TONE_150_0 = 15000
    TONE_151_4 = 15140
    TONE_156_7 = 15670
    TONE_159_8 = 15980
    TONE_162_2 = 16220
    TONE_165_5 = 16550
    TONE_167_9 = 16790
    TONE_171_3 = 17130
    TONE_173_8 = 17380
    TONE_177_3 = 17730
    TONE_179_9 = 17990
    TONE_183_5 = 18350
    TONE_186_2 = 18620
    TONE_189_9 = 18990
    TONE_192_8 = 19280
    TONE_196_6 = 19660
    TONE_199_5 = 19950
    TONE_203_5 = 20350
    TONE_206_5 = 20650
    TONE_210_7 = 21070
    TONE_218_1 = 21810
    TONE_225_7 = 22570
    TONE_229_1 = 22910
    TONE_233_6 = 23360
    TONE_241_8 = 24180
    TONE_250_3 = 25030
    TONE_254_1 = 25410


class RepeaterDcsCode(StrEnum):
    D023 = "D023"
    D025 = "D025"
    D026 = "D026"
    D031 = "D031"
    D032 = "D032"
    D036 = "D036"
    D047 = "D047"
    D051 = "D051"
    D053 = "D053"
    D054 = "D054"
    D065 = "D065"
    D071 = "D071"
    D072 = "D072"
    D073 = "D073"
    D074 = "D074"
    D114 = "D114"
    D115 = "D115"
    D116 = "D116"
    D122 = "D122"
    D125 = "D125"
    D131 = "D131"
    D132 = "D132"
    D134 = "D134"
    D143 = "D143"
    D145 = "D145"
    D152 = "D152"
    D155 = "D155"
    D156 = "D156"
    D162 = "D162"
    D165 = "D165"
    D172 = "D172"
    D174 = "D174"
    D205 = "D205"
    D212 = "D212"
    D223 = "D223"
    D225 = "D225"
    D226 = "D226"
    D243 = "D243"
    D244 = "D244"
    D245 = "D245"
    D246 = "D246"
    D251 = "D251"
    D252 = "D252"
    D255 = "D255"
    D261 = "D261"
    D263 = "D263"
    D265 = "D265"
    D266 = "D266"
    D271 = "D271"
    D274 = "D274"
    D306 = "D306"
    D311 = "D311"
    D315 = "D315"
    D325 = "D325"
    D331 = "D331"
    D332 = "D332"
    D343 = "D343"
    D346 = "D346"
    D351 = "D351"
    D356 = "D356"
    D364 = "D364"
    D365 = "D365"
    D371 = "D371"
    D411 = "D411"
    D412 = "D412"
    D413 = "D413"
    D423 = "D423"
    D431 = "D431"
    D432 = "D432"
    D445 = "D445"
    D446 = "D446"
    D452 = "D452"
    D454 = "D454"
    D455 = "D455"
    D462 = "D462"
    D464 = "D464"
    D465 = "D465"
    D466 = "D466"
    D503 = "D503"
    D506 = "D506"
    D516 = "D516"
    D523 = "D523"
    D526 = "D526"
    D532 = "D532"
    D546 = "D546"
    D565 = "D565"
    D606 = "D606"
    D612 = "D612"
    D624 = "D624"
    D627 = "D627"
    D631 = "D631"
    D632 = "D632"
    D645 = "D645"
    D654 = "D654"
    D662 = "D662"
    D664 = "D664"
    D703 = "D703"
    D712 = "D712"
    D723 = "D723"
    D731 = "D731"
    D732 = "D732"
    D734 = "D734"
    D743 = "D743"
    D754 = "D754"


class RepeaterUse(StrEnum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    PRIVATE = "PRIVATE"


class StateCodes(IntEnum):
    AL = 1
    AK = 2
    AZ = 4
    AR = 5
    CA = 6
    CO = 8
    CT = 9
    DE = 10
    DC = 11
    FL = 12
    GA = 13
    HI = 15
    ID = 16
    IL = 17
    IN = 18
    IA = 19
    KS = 20
    KY = 21
    LA = 22
    ME = 23
    MD = 24
    MA = 25
    MI = 26
    MN = 27
    MS = 28
    MO = 29
    MT = 30
    NE = 31
    NV = 32
    NH = 33
    NJ = 34
    NM = 35
    NY = 36
    NC = 37
    ND = 38
    OH = 39
    OK = 40
    OR = 41
    PA = 42
    RI = 44
    SC = 45
    SD = 46
    TN = 47
    TX = 48
    UT = 49
    VT = 50
    VA = 51
    WA = 53
    WV = 54
    WI = 55
    WY = 56


class RepeaterStatus(StrEnum):
    UNKNOKWN = "Unknown"
    ONAIR = "On-air"
    OFFAIR = "Off-air"
