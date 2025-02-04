import matplotlib.pyplot as plt
import numpy as np

def Draw_ampl(data1, data2, data3, points):
    plt.plot(points, data1, label = "Amplitude")
    plt.plot(points, data2, label = "Modulation")
    plt.plot(points, data3, label = "Finalization")
    plt.title("Signal Modulation")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(loc='upper right')
    plt.show()

def Nosna(A, f, t):
    return np.array(A * np.sin((2 * np.pi * f) * t))

def M(M, fi, t, eps = 0):
    return (M * np.sin((fi * t) + eps))

def Am_Mod(M, A, f, t, eps = 0):
    return np.array((M + A) * np.sin((2 * np.pi * f) * t))


def frek_nos(f, t):
    w = (2 * np.pi * f)
    return np.array(np.sin(w * t))


def frek_mod(A, f, fm, t):
    w = (2 * np.pi * f)
    wd = (2 * np.pi * fm)
    return np.array(A*np.sin(w * t  + A * np.cos(wd * t)))

A = 2
M_val = 4
f = 10
fm = 1
t = 2
eps = 0
partitions = 10000


points = np.array(np.linspace(0, t, partitions))
data1 = Nosna(A,f,points)
data2 = Am_Mod(M(M_val, f, points), A, f, points)
data3 = data1+data2

frek_nos = frek_nos(f,points)
frek_mod = frek_mod(A, f, fm, points)
plt.plot(points, frek_nos, label = "nosna")
plt.plot(points, frek_mod, label = "final")
plt.legend()
plt.show()

#Draw_ampl(data1, data2, data3, points)