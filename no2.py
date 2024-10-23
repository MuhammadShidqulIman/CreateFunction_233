import math

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r ** 2

jari_jari = 4
luas = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
