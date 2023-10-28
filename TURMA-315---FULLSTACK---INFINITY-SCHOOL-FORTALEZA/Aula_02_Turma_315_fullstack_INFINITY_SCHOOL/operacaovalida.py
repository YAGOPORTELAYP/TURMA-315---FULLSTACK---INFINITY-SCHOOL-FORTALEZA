alternativa = str(input("Você deseja sair? S/N:")).upper().strip()

if alternativa == "S" or alternativa == "N" :
    print("Operação Válida!")
    if alternativa == "S" :
        print("Adeus!")
    else:
        print("Continue usando o programa!")
else:
    print("Operação Inválida!")