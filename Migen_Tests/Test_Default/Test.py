
#import
from migen import *
from migen.build.platforms import m1

#platform
plat = m1.Platform()

#ports
led = plat.request("user_led")

#module
m = Module()
counter = Signal(26)                #create counter
m.sync += counter.eq(counter + 1)   #increase counter every cycle
m.comb += led.eq(counter[25])       #set led to 26th bit of counter

#build
plat.build(m)