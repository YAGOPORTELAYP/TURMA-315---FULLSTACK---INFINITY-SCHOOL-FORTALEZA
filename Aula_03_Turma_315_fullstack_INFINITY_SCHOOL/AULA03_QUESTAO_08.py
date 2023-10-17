word = str(input("Insira uma Palavra:")).lower().strip()
vogais = "aeiou"
qnt_vogais = 0

for palavra in word:
    if palavra in vogais:
        qnt_vogais +=1

print(f"Há {qnt_vogais} Vogais na Palavra {word}.")