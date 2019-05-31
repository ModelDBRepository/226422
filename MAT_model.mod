NEURON {
    POINT_PROCESS MATmodel
    RANGE E_L, R, taum, tau1, tau2, omega, a_1, a_2, u1, u2, t_f, t_start, t_stop, I_amp, y, vth, I
}

UNITS {
    (mV) = (millivolt)
    (nA) = (nanoamp)
    (mO) = (megohm)
}

INITIAL {
    vm = E_L
    y = E_L
    vth = omega
    I = 0
    u1 = 0
    u2 = 0
    t_f = 0
}

PARAMETER {
    : Default values set for RS neurons
    E_L = -65  (mV)
    R = 50  (mO)
    taum = 5 (ms)
    tau1 = 10 (ms)
    tau2 = 200 (ms)

    omega = -45 (mV)
    a_1 = 30 (mV)
    a_2 = 2.0 (mV)

    t_f = 0 (ms)
    t_start = 100.0 (ms)
    t_stop = 600.0 (ms)
    I_amp = 0.6 (nA)
}

ASSIGNED {
    y (mV)
    vth (mV)
    I (nA)
}

STATE {
    vm (mV)
    u1 (mV)
    u2 (mV)
}

BREAKPOINT {
    vth = omega + u1 + u2
    y = vm

    if ((vm >= vth) && (t-t_f > 2.0)) {
        u1 = u1 + a_1
        u2 = u2 + a_2
        t_f = t
        y = 0
    }

    if ((t >= t_start) && (t <=t_stop)) {
        I = I_amp
    } else {
        I = 0
    }

    SOLVE states METHOD derivimplicit
}

DERIVATIVE states {
    vm' = (R*I-(vm-E_L))/(taum)
    u1' = -u1/tau1
    u2' = -u2/tau2
}
