from enum import StrEnum
from enum import IntEnum


class TxPower(StrEnum):
    HIGH = "H"
    MEDIUM = "M"
    LOW = "L"


class TxBandwidth(IntEnum):
    BW_12_5 = 12500
    BW_25 = 25000


class OnOff(IntEnum):
    ON = 1
    OFF = 0


class Mode(IntEnum):
    FM = 0
    AM = 1


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
