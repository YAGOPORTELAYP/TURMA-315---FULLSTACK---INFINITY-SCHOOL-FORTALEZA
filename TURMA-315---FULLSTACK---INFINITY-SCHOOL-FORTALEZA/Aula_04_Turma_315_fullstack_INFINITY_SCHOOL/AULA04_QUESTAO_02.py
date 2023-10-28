while True:
    user = str(input("Insira seu usuário:")).lower().strip()
    password = str(input("Insira sua senha:"))
    
    if password == user:
        print("Erro! Usuário e senha não podem ser iguais! ")
    else:
        print("Correto!")
        break