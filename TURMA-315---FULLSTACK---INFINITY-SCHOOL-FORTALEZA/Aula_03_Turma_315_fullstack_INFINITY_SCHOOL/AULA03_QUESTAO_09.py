word = str(input("Insira uma Palavra:")).lower().strip()
vogais = "aeiou"
qnt_vogais = 0

for palavra in word:
    if palavra not in vogais:
        qnt_vogais +=1

print(f"Há {qnt_vogais} Consoantes na Palavra {word}.")