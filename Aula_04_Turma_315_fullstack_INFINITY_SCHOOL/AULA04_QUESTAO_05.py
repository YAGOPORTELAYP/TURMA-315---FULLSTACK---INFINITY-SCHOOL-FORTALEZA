num_anos = 0
while True:
    pais_A = int(input("Digite a População do país A:"))
    if pais_A > 0:
        print("Número populacional válido.")
        break
    else:
        print("Digite um número populacional válido.")
        continue    
while True:
    pais_B = int(input("Digite a População do país B:"))
    if pais_B > 0:
        print("Número populacional válido.")
        break
    else:
        print("Digite um número populacional válido.")
        continue 
taxa_A = float(input("Digite a taxa de crescimento do país A(Pode ser em porcentagem!):"))
taxa_B = float(input("Digite a taxa de crescimento do país B(Pode ser em porcentagem!):"))
while True:
    if pais_A < pais_B:
        pais_A = pais_A*(1 + (taxa_A/100))
        pais_B = pais_B*(1 + (taxa_B/100))
        num_anos += 1
        continue
    else:
        print(f"O número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento é: {num_anos}")
    break
