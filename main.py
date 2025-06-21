import models
import sys

repeaters = models.RepeaterBookResults.from_file("rochester.json")
channels = models.VGCChannelList(
    sorted(
        [
            models.VGCChannel.from_repeater(rp)
            for rp in repeaters.results
            if rp.fm_analog and (140 <= rp.tx_freq <= 200 or 400 <= rp.tx_freq <= 500)
        ],
        key=lambda rp: rp.tx_freq,
    )
)

channels.model_dump_csv(sys.stdout)
