import csv

from pydantic import BaseModel
from pydantic import RootModel
from pydantic import BeforeValidator
from pydantic import field_validator
from pydantic import Field
from typing import Annotated
from typing import TextIO
from typing import Self

from constants import RepeaterTone
from constants import TxPower
from constants import TxBandwidth
from constants import Mode
from constants import OnOff


def parse_bool_str(v: str):
    return v.lower() in ["yes", "true", "1"]


BoolStr = Annotated[bool, BeforeValidator(parse_bool_str)]


class Repeater(BaseModel):
    rx_freq: float = Field(..., alias="Frequency")
    tx_freq: float = Field(..., alias="Input Freq")
    pl_code: RepeaterTone = Field(..., alias="PL")
    callsign: str = Field(..., alias="Callsign")
    fm_analog: BoolStr = Field(..., alias="FM Analog")
    fm_bandwidth: str = Field(..., alias="FM Bandwidth")


class VGCChannel(BaseModel):
    title: str
    tx_freq: int
    rx_freq: int
    tx_sub_audio: int = 0
    rx_sub_audio: int = 0
    tx_power: TxPower = TxPower.MEDIUM
    bandwidth: TxBandwidth = TxBandwidth.BW_25
    scan: OnOff = OnOff.ON
    talk_around: OnOff = OnOff.OFF
    pre_de_emph_bypass: OnOff = OnOff.OFF
    sign: OnOff = OnOff.ON
    tx_dis: OnOff = OnOff.OFF
    mute: OnOff = OnOff.OFF
    rx_modulation: Mode = Mode.FM
    tx_modulation: Mode = Mode.FM

    @classmethod
    def from_repeater(cls, rp: Repeater) -> Self:
        return cls(
            title=rp.callsign,
            tx_freq=int(rp.tx_freq * 1000000),
            rx_freq=int(rp.rx_freq * 1000000),
            tx_sub_audio=int(float(rp.pl_code) * 100),
        )


class VGCChannelList(RootModel[list[VGCChannel]]):
    root: list[VGCChannel]

    def model_dump_csv(self, fd: TextIO):
        writer = csv.DictWriter(fd, VGCChannel.model_fields)
        writer.writeheader()
        for channel in self.root:
            writer.writerow(channel.model_dump())


class RepeaterBookResults(BaseModel):
    count: int
    results: list[Repeater]

    @classmethod
    def from_file(cls, path: str) -> Self:
        with open(path) as fd:
            return cls.model_validate_json(fd.read())
