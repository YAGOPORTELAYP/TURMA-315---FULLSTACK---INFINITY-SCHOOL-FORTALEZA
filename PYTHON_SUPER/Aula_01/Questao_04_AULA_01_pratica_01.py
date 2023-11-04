vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"

while True:
    letra = str(input("\nDigite uma letra do alfabeto:")).lower().strip()
    if len(letra) != 1:
        print("\nDigite somente uma Letra!!!\n")
        continue
    if letra in vogais:
        print("\nÉ uma Vogal!\n")
        break
    if letra in consoantes:
        print("\nÉ uma Consoante!\n")
        break
    break