import EPRsim.EPRsim as sim
import matplotlib.pyplot as plt
P = sim.Parameters()
P.Range = [334,337]
P.mwFreq = 9.4067
P.g = 2.003
P.Nucs = 'H,H'
P.n = [1,4]
P.A = [15,3] 
P.lw = [0.05]
P.motion = 'fast'
B0, spc, flag = sim.simulate(P)

plt.figure(figsize=(10, 6))

plt.plot(B0, spc, color='red', label='Simulation')

plt.xlabel(r'$B$ / mT') 
plt.ylabel(r'Absorption / a.u.')

# plt.grid(True, alpha=0.3)
# plt.axhline(0, color='black', linewidth=0.8)
# plt.legend()
plt.savefig('Gal_Sim.pdf')

plt.show()