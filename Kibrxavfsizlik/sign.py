import numpy as np
import math
import matplotlib.pyplot as plt

# Berilgan qiymatlar
N0 = 2010.0

# α(t) va β(t)
def alpha(t):
    return 3.0 / (2.0 + t)

def beta(t):
    return 2.0  # doimiy

# Analitik yechim:
# N(t) = N0 * ((2+t)^3 / 8) * e^(-2t)
def N_of_t(t):
    return N0 * ((2.0 + t)**3 / 8.0) * math.exp(-2.0 * t)

# N(4) ni hisoblash
t0 = 4
N4 = N_of_t(t0)
print(f"N(4) = {N4:.5f}")

# Grafik chizish
t_vals = np.linspace(0, 10, 400)
N_vals = [N_of_t(t) for t in t_vals]

plt.figure(figsize=(8,5))
plt.plot(t_vals, N_vals, linewidth=2)
plt.scatter([t0], [N4], s=60)
plt.axvline(t0, linestyle="--")
plt.title("Aholi soni N(t) = 2010 * ((2+t)^3 / 8) * e^{-2t}")
plt.xlabel("t (yil)")
plt.ylabel("Aholi soni N(t)")
plt.grid(True)
plt.show()
