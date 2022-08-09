medida = float(input('Digite uma distancia em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f"A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm")
print(f"A medida de {medida}m corresponde a {dam:.2f}dam e {hm:.2f}hm e {km:.2f}km")
