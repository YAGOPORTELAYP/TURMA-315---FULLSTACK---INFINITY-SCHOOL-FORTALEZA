n1 = float(input("Digite a Nota Parcial 1:"))
n2 = float(input("Digite a Nota Parcial 2:"))

med = (n1+n2)/2

if med == 10:
    print("Aprovado com Distinção!")
else:
    if med >= 7:
        print("Aprovado!")
    elif med < 7:
        print("Reprovado!")