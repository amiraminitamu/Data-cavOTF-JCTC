import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})

O_data = np.loadtxt("O_time_series.dat")
t_half = O_data[:, 0]
O = O_data[:, 1:-1]     
O_avg = O_data[:, -1]   

H_data = np.loadtxt("H_time_series.dat")
t = H_data[:, 0]
H = H_data[:, 1:-1]     
H_avg = H_data[:, -1]

for j in range(O.shape[1]):
    plt.plot(t_half, O[:, j], c="#ff6b6b", alpha=0.2)

plt.plot(t_half, O_avg, c="#c23616", linewidth=2, label="O avg")

plt.xlim(0, 500)
plt.ylim(-2, 2)
plt.xlabel("Time (fs)")
plt.ylabel("$\\frac{d\mu}{dR_O}$ (a.u.)")

for j in range(H.shape[1]):
    plt.plot(t, H[:, j], c="#54a0ff", alpha=0.2)

plt.plot(t, H_avg, c="#273c75", linewidth=2, label="H avg")

plt.xlim(0, 500)
plt.ylim(-2, 2)
plt.xlabel("Time (fs)")
plt.ylabel("$\\nabla\mu$ (a.u.)")

plt.savefig("Fig2b.pdf", bbox_inches="tight")
