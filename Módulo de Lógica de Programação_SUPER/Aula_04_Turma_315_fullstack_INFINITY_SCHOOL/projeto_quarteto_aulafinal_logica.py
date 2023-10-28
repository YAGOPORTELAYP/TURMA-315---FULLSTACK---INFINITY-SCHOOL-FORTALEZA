print("""Candy IN Store
""")

#Só encerra o caixa com o registro de vendas maior que 5
#Sortear 3 diferentes clientes

# criei um invertexto
#https://www.invertexto.com/lojayagoinfinity
while True:
    print("""Registro de Vendas:
    
Digite os dados do Cliente:
    """)
    contador = 1
    print(f"Cliente N#{contador}")
    
    client_name = str(input("Digite o nome do cliente:"))
    client_tel = str(input("Digite o telefone do cliente:"))
    client_address = str(input("Digite o endereço do cliente:"))

    while True:
        if len(client_name) < 3:
            print("""Nome Inválido!
            O nome deve possuir mais que 3 caracteres.""")
            continue
        else:
            print("""
            Nome Válido.
            """)
        break

    while True:
        if len(client_tel) != 11:
            print("""Digite um número válido.
            """)
            continue
        else:
            print("Número Válido")
            break

    while True:
        if len(client_address) > 3:
            print("""Endereço Válido.
            """)
            break
        else:
            print("Digite um endereço Inválido.")
            continue

    contador += 1

    if contador > 5:
        print("Você deseja encerrar o caixa?")
        caixa_out = str(input("Sim ou Não?  (s/n)")).lower()
        if caixa_out == "s":
            print("Caixa Encerrado.")
        if caixa_out == "n":
            print("O caixa de ... permanecerá aberto.")


# print(f"""Fluxograma:
#           Número de Vendas:{contador}
# """)

# if 

# while True:
#     for cliente
    
    
#     break