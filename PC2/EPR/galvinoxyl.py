import EPRsim.EPRsim as sim

P = sim.Parameters()
P.Range = [335,350]
P.mwFreq = 9.6
P.g = 2.002
P.Nucs = 'N'
P.A = 45.5
P.lw = [0.2]
P.motion = 'fast'
B0, spc, flag = sim.simulate(P)