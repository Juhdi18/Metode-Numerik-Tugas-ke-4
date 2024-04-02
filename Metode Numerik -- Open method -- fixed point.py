import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

iterasi = 10
a = 1
b = -2
c = -6

hasil1 = np.zeros(iterasi, dtype=float)
hasil2 = np.zeros(iterasi, dtype=float)
x1 = np.zeros(iterasi, dtype=float)  # Variabel x untuk gx1
x2 = np.zeros(iterasi, dtype=float)  # Variabel x untuk gx2
gx1 = np.zeros(iterasi, dtype=float)
gx2 = np.zeros(iterasi, dtype=float)
epsT_1 = np.zeros(iterasi+1, dtype=float)
epsA_1 = np.zeros(iterasi+1, dtype=float)
epsT_2 = np.zeros(iterasi+1, dtype=float)
epsA_2 = np.zeros(iterasi+1, dtype=float)

x_1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
x_2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
eksak = x_2

# Menghitung akar-akar dari persamaan kuadratik
x1[0] = 1  # Nilai awal yang dipilih secara arbitrer untuk gx1
x2[0] = 1  # Nilai awal yang dipilih secara arbitrer untuk gx2

for i in range(1, iterasi):  # Memulai iterasi dari 1
    gx1[i] = (x1[i-1]**2 - 6) / 2
    gx2[i] = 2 + (6 / x2[i-1])
    x1[i] = gx1[i]  # Memperbaharui nilai x1 menggunakan gx1
    x2[i] = gx2[i]  # Memperbaharui nilai x2 menggunakan gx2
    epsT_1[i] = abs((eksak - gx1[i])) * 100
    epsA_1[i] = abs((gx1[i] - gx1[i-1]) / gx1[i]) * 100 if i != 0 else 0
    epsT_2[i] = abs((eksak - gx2[i])) * 100
    epsA_2[i] = abs((gx2[i] - gx2[i-1]) / gx2[i]) * 100 if i != 0 else 0

# Buat daftar data untuk tabel
data = []
for i in range(1, iterasi):
    row = [i, gx1[i], gx2[i], x1[i], x2[i], epsT_1[i], epsA_1[i], epsT_2[i], epsA_2[i]]
    data.append(row)

# Buat header tabel
header = ["iterasi", "hasil 1", "hasil 2", "x1", "x2", "epsT 1", "epsA 1", "epsT 2", "epsA 2"]

# Tampilkan tabel menggunakan tabulate
print(tabulate(data, headers=header))

# Plot
plt.plot(range(iterasi), gx1, label='gx1: (x^2 - 6) / 2')
plt.plot(range(iterasi), gx2, label='gx2: 2 + 6 / x')
plt.xlabel('Iterasi')
plt.ylabel('Nilai')
plt.title('Perbandingan Hasil dari Dua Iterasi')
plt.legend()
plt.grid(True)
plt.show()
