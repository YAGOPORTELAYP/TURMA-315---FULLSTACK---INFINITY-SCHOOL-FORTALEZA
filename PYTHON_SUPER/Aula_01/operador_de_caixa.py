soma = 0
while True:
    nome = str(input("\nDigite o nome do produto:"))
    if nome == "-1":
        break
    valor = float(input("\nDigite o preço do produto:"))
    soma += valor
print(f"\nO valor total da compra foi de R$ {soma}")