letra = str(input("Digite uma Letra:")).lower().strip()

if len(letra) == 1:
    if letra in "aeiou":
        print(f"{letra} é Vogal!")
    elif letra in "bcdfghjklmnpqrstvwxyz": 
        print(f"{letra} é Consoante!")
    else:
        print(f"{letra} é um tipo de letra inválida!")
else:
    print("Digite somente uma letra!!!")