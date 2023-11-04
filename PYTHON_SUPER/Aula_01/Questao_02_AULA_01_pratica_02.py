num = int(input("\nDigite um número inteiro:"))
tabuada = 0

print(f"\nA Tabuada do número {num} de 1 à 10 é:")

for i in range(1,11):
    tabuada = num * i
    print(f"{num} X {i} = {tabuada}")