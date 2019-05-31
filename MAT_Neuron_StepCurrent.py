from neuron import h, gui

dummy_sec = h.Section()
model = h.MATmodel(dummy_sec(0.5))

t_vec = h.Vector()
i_vec = h.Vector()
v_vec = h.Vector()
t_vec.record(h._ref_t)
i_vec.record(model._ref_I)
v_vec.record(model._ref_y)

h.tstop = 700
h.v_init = model.vm

# For Regular Spiking (RS)
model.omega = -45.0
model.a_1 = 30.0
model.a_2 = 2.0
h.run()
rs_v_vec = v_vec.to_python()

# For Intrinsic Bursting (RS)
model.omega = -46.0
model.a_1 = 7.5
model.a_2 = 1.5
h.run()
ib_v_vec = v_vec.to_python()

# For Fast Spiking (FS)
model.omega = -55.0
model.a_1 = 10.0
model.a_2 = 0.2
h.run()
fs_v_vec = v_vec.to_python()

# For CHattering (CH)
model.omega = -39.0
model.a_1 = -0.5
model.a_2 = 0.4
h.run()
ch_v_vec = v_vec.to_python()

from matplotlib import pyplot
fig = pyplot.figure(figsize=(8,12))
pyplot.suptitle("Fig. 5 from Kobayashi et al., 2009", fontsize=16, fontweight='bold')

pyplot.subplot(5,1,1)
pyplot.plot(t_vec, i_vec)
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Current Input')
pyplot.xlabel('time (ms)')
pyplot.ylabel('current (nA)')

pyplot.subplot(5,1,2)
pyplot.plot(t_vec, rs_v_vec)
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Regular Spiking (RS)')
pyplot.xlabel('time (ms)')
pyplot.ylabel('potential (mV)')

pyplot.subplot(5,1,3)
pyplot.plot(t_vec, ib_v_vec)
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Intrinsic Bursting (RS)')
pyplot.xlabel('time (ms)')
pyplot.ylabel('potential (mV)')

pyplot.subplot(5,1,4)
pyplot.plot(t_vec, fs_v_vec)
pyplot.margins(x=0.0, y=0.1)
pyplot.title('Fast Spiking (FS)')
pyplot.xlabel('time (ms)')
pyplot.ylabel('potential (mV)')

pyplot.subplot(5,1,5)
pyplot.plot(t_vec, ch_v_vec)
pyplot.margins(x=0.0, y=0.1)
pyplot.title('CHattering (CH)')
pyplot.xlabel('time (ms)')
pyplot.ylabel('potential (mV)')

fig.tight_layout()
fig.subplots_adjust(top=0.92)
pyplot.show()
