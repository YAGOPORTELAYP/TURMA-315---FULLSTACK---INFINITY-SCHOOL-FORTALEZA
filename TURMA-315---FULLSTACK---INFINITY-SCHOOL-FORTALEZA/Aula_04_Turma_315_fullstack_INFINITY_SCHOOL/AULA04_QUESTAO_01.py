while  True:
    q = float(input("Insira uma nota entre 0 e 10:"))
    if q > 0 and q < 10: 
        print(f"{q} é uma nota válida!")
        break
    else:
        print(f"{q} é uma nota inválida!")