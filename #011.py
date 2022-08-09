L = float(input('Largura da parede: '))
A = float(input("Altura da parede: "))

mx2 = L * A
print('Sua parede tem a dimensao de {} x {} e sua area e de {}m²'.format(L, A, mx2))
tinta = mx2 / 2
print("Para pintar essa parede, voce precisa de {}l de tinta".format(tinta))