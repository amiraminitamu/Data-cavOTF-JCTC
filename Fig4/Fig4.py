import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams.update({'font.size': 20})

DATA = "./"

def load_spec(name):
    d = np.loadtxt(DATA + name, skiprows=1)
    return d[:,0], d[:,1]


hist19 = np.loadtxt(DATA + "hist_19.dat")
hist43 = np.loadtxt(DATA + "hist_43.dat")

L = 423341.7992
k19 = 2 * np.pi * np.arange(hist19.shape[0]) / L
k43 = 2 * np.pi * np.arange(hist43.shape[0]) / L
omega = np.arange(0.03, 0.850, 0.0001)


def plot_stacked(ax_list, names, colors):
    for ax, (fname, color) in zip(ax_list, zip(names, colors)):
        x, y = load_spec(fname)
        ax.plot(x, y, lw=3.5, color=color)
        ax.fill_between(x, y, color=color, alpha=0.3)
        ax.set_xlim(0.15, 0.50)
        ax.set_ylim(0, 1.05)
        ax.label_outer()


def plot_hist(ax, hist, k, ylim, xlim):

    im = ax.imshow(
        hist.T[::-1, :],                      
        aspect="auto",
        extent=[k[0] * 1e4, k[-1] * 1e4, omega[0], omega[-1]],
        cmap=matplotlib.colors.LinearSegmentedColormap.from_list(
            'custom', ['#020024', '#547bff', '#00d4ff', '#a9f0ff', '#a9ffe2'],
        )
    )
    if ax == ax19:
        #set yticks to 0.1 0.2 0.3 0.4

        ax.set_yticks([0.1, 0.2, 0.3, 0.4])
    ax.set_ylim(*ylim)
    ax.set_xlim(*xlim)
    im.set_clim(0, 1e5)

    return im


fig = plt.figure(figsize=(24, 12))
outer = fig.add_gridspec(2, 2, wspace=0.12, hspace=0.28)


gs19 = outer[0,0].subgridspec(4,1, hspace=0.35)
axes19 = [fig.add_subplot(gs19[i,0]) for i in range(4)]
plot_stacked(
    axes19,
    ["no_cavity.dat", "19_1.dat", "19_2.dat", "19_3.dat"],
    ["k", "#ee5253", "#ee5253", "#ee5253"]
)


gs43 = outer[0,1].subgridspec(4,1, hspace=0.35)
axes43 = [fig.add_subplot(gs43[i,0]) for i in range(4)]
plot_stacked(
    axes43,
    ["no_cavity.dat", "43_1.dat", "43_2.dat", "43_3.dat"],
    ["k", "#ee5253", "#ee5253", "#ee5253"]
)


ax19 = fig.add_subplot(outer[1,0])
plot_hist(ax19, hist19, k19, ylim=(0.1, 0.4), xlim=(0, 2.0))
ax19.set_xlabel(r"$k\,(10^{-4}\ \mathrm{\AA^{-1}})$")
ax19.set_ylabel("Energy (eV)")


ax43 = fig.add_subplot(outer[1,1])
plot_hist(ax43, hist43, k43, ylim=(0.3, 0.7), xlim=(0, 3.0))
ax43.set_xlabel(r"$k\,(10^{4}\ \mathrm{\AA^{-1}})$")

plt.savefig("Fig4.pdf", bbox_inches="tight")
