import matplotlib.pyplot as plt
import numpy as np


def Am(A, f, t):
    return A * np.sin((2 * np.pi * f) * t)

def M(M, fi, t, eps = 0):
    return M * np.sin((fi * t) + eps)

def Am_Mod(M, A, f, t, eps = 0):
    return (M + A) * np.sin((2 * np.pi * f) * t)


A = 1
M_val = 4
f = 10
t = 10
eps = 0
partitions = 10000


points = np.array(np.linspace(0, t, partitions))
data = Am(A,f,points)
data2 = Am_Mod(M(M_val, f, points), A, f, points)
data3 = data+data2

plt.plot(points, data, label = "Aplitude")
plt.plot(points, data2, label = "Modulation")
plt.plot(points, data3, label = "Finalization")
plt.title("Signal Modulation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend(loc='upper right')
plt.show()