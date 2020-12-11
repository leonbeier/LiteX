
#import
from migen import *
from migen.fhdl.verilog import convert

m = Module()

#create inputs and outputs
m.inputs  = [Signal(1, "btn")]  #add button input
m.outputs = [Signal(1, "led")]  #add led output

#code
counter = Signal(24)                                    #create counter signal
m.sync += counter.eq(counter + 1)                       #count up every clock cycle
m.sync += If(m.inputs[0], m.outputs[0].eq(counter[22])) #if button pressed, set led to the 24th bit of the counter

#add inputs and outputs to i/os
m.io = set()
m.io = m.io.union(m.inputs)
m.io = m.io.union(m.outputs)

#create verilog
convert(m, m.io, name="Test").write("Test.v")