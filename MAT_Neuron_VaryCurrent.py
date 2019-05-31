import numpy
from neuron import h, gui

dummy_sec = h.Section()
model = h.MATmodel(dummy_sec(0.5))

# Generating noisy current (can be replaced with loading current from file)
i_dt = 0.1 #ms
i_start = 0 #ms
i_stop = 1000 #ms
i_amp = 0.5 #nA
i_t = numpy.arange(i_start, i_stop+i_dt, i_dt)
i_vals = numpy.random.normal(i_amp, i_amp/5.0, len(i_t))

# Feeding noisy current values into model
i_vals_hoc = h.Vector()
i_t_hoc = h.Vector()
i_vals_hoc = i_vals_hoc.from_python(i_vals)
i_t_hoc = i_t_hoc.from_python(i_t)
i_vals_hoc.play(model._ref_I_amp, i_t_hoc, 1)

t_vec = h.Vector()
i_vec = h.Vector()
v_vec = h.Vector()
t_vec.record(h._ref_t)
i_vec.record(model._ref_I)
v_vec.record(model._ref_y)

h.tstop = 700
h.v_init = model.vm
h.run()
i_vec1 = i_vec.to_python()
v_vec1 = v_vec.to_python()
# Changing the start and stop
model.t_start = 250 #ms
model.t_stop = 500 #ms
h.run()
i_vec2 = i_vec.to_python()
v_vec2 = v_vec.to_python()

from matplotlib import pyplot
fig = pyplot.figure(figsize=(8,8))
pyplot.suptitle("Demo with noisy current input", fontsize=16, fontweight='bold')

pyplot.subplot(3,1,1)
pyplot.plot(t_vec, i_vec1, 'r')
pyplot.plot(t_vec, i_vec2, 'b')
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Current Input')
pyplot.xlabel('time (ms)')
pyplot.ylabel('current (nA)')

pyplot.subplot(3,1,2)
pyplot.plot(t_vec, v_vec1, 'r')
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Default Start/Stop')
pyplot.xlabel('time (ms)')
pyplot.ylabel('potential (mV)')

pyplot.subplot(3,1,3)
pyplot.plot(t_vec, v_vec2, 'b')
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Changed Start/Stop')
pyplot.xlabel('time (ms)')
pyplot.ylabel('potential (mV)')

fig.tight_layout()
fig.subplots_adjust(top=0.92)
pyplot.show()
