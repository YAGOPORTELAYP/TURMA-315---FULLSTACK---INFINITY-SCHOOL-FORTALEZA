print("Este é  um gerador de Tabuada de Multiplicação.\n")
tabuada = int(input("Digite a tabuada do número que você deseja:"))
print(f"Esta é a Tabuada do {tabuada} multiplicando de 1 a 10 :\n")
for n in range(1,11):
    mult = tabuada * n
    print(f"{tabuada} X {n} = {mult}")
