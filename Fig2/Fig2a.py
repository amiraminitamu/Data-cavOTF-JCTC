import numpy as np
import matplotlib.pyplot as plt

H = np.loadtxt('H_hist.dat')
O = np.loadtxt('O_hist.dat')

plt.hist(H, bins=100, color='#54a0ff', alpha=0.8, density=True)
plt.xlim(-1.5, 1)

plt.hist(O, bins=100, color='#ee5253', alpha=0.8, density=True)
plt.xlim(-1.5, 1)

plt.ylabel('Density')
plt.xlabel('$\\nabla\mu$ (a.u.)')
plt.ylim(0,6.0)
plt.savefig('Fig2a.pdf', bbox_inches="tight")