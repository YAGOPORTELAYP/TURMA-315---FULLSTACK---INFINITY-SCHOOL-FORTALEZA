cor = str(input("Digite uma cor[AMARELO | VERDE | VERMELHO]:")).upper().strip()

match cor:
    case "VERMELHO":
        print("PARE!!!")
    case "VERMELHA":
        print("PARE!!!")
    case "AMARELO":
        print("MANTENHA ATENÇÃO!!")
    case "AMARELA":
        print("MANTENHA ATENÇÃO!!")
    case "VERDE":
        print("SIGA EM FRENTE!")
    case _:
        print("COR INVÁLIDA")