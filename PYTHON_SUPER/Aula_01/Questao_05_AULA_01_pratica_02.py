frase = str(input("\nDigite uma frase:")).lower().strip()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
v_contador = 0
c_contador = 0
for scan in frase:
    if scan in vogais:
        v_contador += 1
    if scan in consoantes:
        c_contador += 1   
print(f"\nHá {v_contador} Vogais e {c_contador} consoantes nessa frase.\n")
