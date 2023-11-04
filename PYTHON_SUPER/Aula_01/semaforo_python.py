cor = str(input("Escolha uma cor do semáforo: ")).lower()
if cor == "vermelho":
    print("Pare!")
elif cor == "amarelo":
    print("Atenção!")
elif cor == "verde":
    print("Acelere!")
else:
    print("Cor inválida")
