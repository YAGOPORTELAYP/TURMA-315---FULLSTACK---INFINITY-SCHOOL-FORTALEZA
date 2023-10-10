cor = str(input("Digite uma cor[AMARELO | VERDE | VERMELHO]:")).upper().strip()
red1 = "VERMELHO"
red2 = "VERMELHA"
yellow1 = "AMARELO"
yellow2 = "AMARELA"
green= "VERDE"

if cor == red1 or cor == red2:
    print("PARE!!!")
elif cor == yellow1 or cor == yellow2:
    print("MANTENHA ATENÇÃO!!")
elif cor == green:
    print("SIGA EM FRENTE!")
else:
    print("COR INVÁLIDA")