#Aluno: Yago Portela Silva de Vasconcelos
# Exemplo de variáveis em Python
# Tipos de variáveis: int, float, string, boolean
print("Preencha os dados para o seu novo perfil! -->")
name = str(input("Insira seu Nome Completo:")).strip()
age = int(input("Insira sua idade:"))
hight = float(input("Insira sua altura:"))
car = str(input("Você tem carro(sim / não)?  ")).lower().strip()
username = input("Digite o seu novo nome de usuário:")
carro = ""
if car == "sim":
    car == True
    carro = ""
if car == "não":
    car == False
    carro = "não"
print(f"""Olá {name}! Seu perfil foi registrado.
Resumo:
Seu nome é {name},
você possui {age} anos.
 Tem {hight} metros de altura.
 Você{carro} tem um carro.
E seu nome de usuário é:{username}""")