vel = int(input("Digite a velocidade ( em km/h) do carro avistado:"))
taxa = 20
excedente = (vel - 80)
if vel > 80:
    multa = excedente*taxa
    print(f"""O usuário foi multado!
O valor da multa é:{multa}.
Pois é cobrado uma taxa de {taxa} reais por km excedido.
E foi excedido {excedente} quilômetros.""")
elif vel <= 80:
    print(f"O usuário está à {vel} km/h, que é dentro do limite(Que é de 80 km/h) de velocidade!")