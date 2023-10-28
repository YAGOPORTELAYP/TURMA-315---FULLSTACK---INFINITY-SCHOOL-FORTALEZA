while True:
    name = str(input("Digite o seu nome:"))
    age = int(input("Digite a sua idade:"))
    sal = float(input("Digite o seu salário:"))
    sex = str(input("Digite o seu sexo(m - Masculino | f - Feminino):")).lower()
    civil = str(input("Digite o seu Estado Civil (s - Solteiro | c - Casado | v - Viúvo | d - Divorciado ):")).lower()

    while True:
        if len(name) < 3:
            print("""O seu nome deve possuir mais que 3 caracteres
                  """)
            continue
        else:
            print("Nome Válido.")
        break

    while True:
        if age in range(151):
            print("""Idade Válida.
            """)
            break
        else:
            print("Idade Inválida. Deve se uma idade entre 0 e 150 Anos.")
            continue

    while True:
        if sal > 0:
            print("""Salário Válido.
            """)
            break
        else:
            print("Salário Inválido.")
            continue

    while True:
        if sex in "mf" and len(sex) == 1:
            if sex == "m":
                sex = "Masculino"
            if sex == "f":
                sex = "Feminino"

            print("""Sexo Válido.
            """)
            break
        else:
            print("Sexo inválido.")
            continue

    while True:
        if civil in "scvd" and len(civil) == 1 :
            if civil == "s" :
                civil = "Solteiro"
            if civil == "c" :
                civil = "Casado"
            if civil == "v":
                civil = "Viúvo"
            if civil == "d":
                civil = "Divorciado"

            print("""Estado Civil Válido.
            """)
            break
        else:
            print("Estado Civil inválido.")
            continue
    break

print(f"""
Seu nome é {name}.

Seu sexo é {sex}.

Você tem {age} anos.

Você ganha um salário em torno de {sal} 

e está {civil} atualmente.""")