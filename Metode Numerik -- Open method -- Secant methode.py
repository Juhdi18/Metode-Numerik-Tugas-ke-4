import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# Definisikan parameter persamaan kuadrat
iterasi = 10  # Jumlah iterasi
a = 1
b = -2
c = -6

# Inisialisasi array untuk menyimpan hasil
hasil1 = np.zeros(iterasi, dtype=float)
hasil2 = np.zeros(iterasi, dtype=float)
x = np.zeros(iterasi, dtype=float)  # Variabel x untuk gx1
gx1 = np.zeros(iterasi, dtype=float)
epsT_1 = np.zeros(iterasi+1, dtype=float)
epsA_1 = np.zeros(iterasi+1, dtype=float)

# Hitung akar-akar persamaan kuadrat
x_1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
x_2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
eksak = x_1  # Akar eksak

# Nilai awal untuk gx1
x[0] = 1  # Nilai awal yang dipilih secara arbitrer
x[1] = 1.5

# Lakukan iterasi
for i in range(1, iterasi-1):
    # Hitung nilai gx1
    gx1[i] = x[i] - ((x[i]**2 - 2*x[i] - 6) * (x[i] - x[i-1])) / ((x[i]**2 - 2*x[i] - 6) - (x[i-1]**2 - 2*x[i-1] - 6))

    # Perbarui nilai x untuk iterasi selanjutnya
    x[i+1] = gx1[i]

    # Hitung error toleransi relatif (epsT)
    epsT_1[i] = abs((eksak - gx1[i])/eksak) * 100

    # Hitung error toleransi absolut (epsA)
    epsA_1[i] = abs((gx1[i] - gx1[i-1]) / gx1[i]) * 100 if i != 0 else 0

# Siapkan data untuk tabel
data = []
for i in range(1, iterasi):
    row = [i, gx1[i], epsT_1[i], epsA_1[i]]
    data.append(row)

# Buat header tabel
header = ["Iterasi", "Hasil 1", "epsT 1", "epsA 1"]

# Tampilkan tabel menggunakan tabulate
print(tabulate(data, headers=header))
print (eksak)

# Plot hasil
plt.plot(range(iterasi-1), gx1[1:], label='gx1: (x^2 - 6) / 2')
plt.xlabel('Iterasi')
plt.ylabel('Nilai')
plt.title('Perbandingan Hasil dari Dua Iterasi')
plt.legend()
plt.grid(True)
plt.show()
