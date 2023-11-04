frase = str(input("\nDigite uma frase:")).lower().strip()
vogais = "aeiou"
contador = 0

for scan in frase:
    if scan in vogais:
        contador += 1
print(f"Há {contador} Vogais nessa frase.")