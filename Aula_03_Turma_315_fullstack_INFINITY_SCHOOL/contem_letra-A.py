word = str(input("Insira uma palavra:")).lower()
tem_a_letra_a = False
qnt_letras_A = 0

for palavra in word:
    if palavra == 'a':
        print("Tem a Letra A")
        tem_a_letra_a = True
        qnt_letras_A += 1

if tem_a_letra_a == True:
    print(f"Sua palavra contém {qnt_letras_A} letraS A!")
else:
    print("Sua palavra não contém a letra A!")