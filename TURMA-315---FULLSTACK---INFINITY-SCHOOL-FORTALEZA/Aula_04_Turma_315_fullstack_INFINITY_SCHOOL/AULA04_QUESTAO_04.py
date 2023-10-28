num_anos = 0
pais_A = 80000
pais_B = 200000

while True:
    if pais_A < pais_B:
        pais_A = pais_A*1.03
        pais_B = pais_B*1.015
        num_anos += 1
        continue
    else:
        print(f"""o número de anos necessários
              para que a população do país A ultrapasse ou iguale
               a população
                do país B, mantidas as taxas de crescimento é: {num_anos}""")
        break
