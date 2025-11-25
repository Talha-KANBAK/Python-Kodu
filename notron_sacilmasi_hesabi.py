import math

# Baslangic enerjisi 1 MeV
E_ilk = 1.0

print("Notron Sacilma Hesabi")

# Kullanici verileri
A = float(input("Hedef cekirdegin kutle numarasi (A): "))
teta_derece = float(input("Sacilma acisi (derece): "))

# Dereceyi radyana cevirme
teta_rad = math.radians(teta_derece)

# Hesaplama
# Esnek Sacilma Formulu: E'/E = [(cos(teta) + sqrt(A^2 - sin^2(teta))) / (A+1)]^2

karekok_ici = (A**2) - (math.sin(teta_rad)**2)

# Karekok ici kontrolu
if karekok_ici < 0:
    print("Hata: Bu aci ve kutle icin sacilma mumkun degil.")
    exit()

terim = math.cos(teta_rad) + math.sqrt(karekok_ici)
oran = (terim / (A + 1)) ** 2

E_son = E_ilk * oran

# Sonuclari ekrana yazdir
print("\nSonuclar")
print("Gelen Enerji:", E_ilk, "MeV")
print("Kutle No (A):", A)
print("Aci (Derece):", teta_derece)
print("Son Enerji:", E_son, "MeV")
