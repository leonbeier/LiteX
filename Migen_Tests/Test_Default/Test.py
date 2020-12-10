from migen import *
from migen.build.platforms import m1
plat = m1.Platform()
led = plat.request("user_led")
m = Module()
counter = Signal(26)
m.comb += led.eq(counter[25])
m.sync += counter.eq(counter + 1)
plat.build(m)