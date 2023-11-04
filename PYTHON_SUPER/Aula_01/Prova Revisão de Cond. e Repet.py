email = "email"
senha = "senha"
print(f"\nEstes são o email e senha cadastrados:\n{email}\n{senha}")

while True:
    user_email = str(input("\nDigite o seu email:"))
    user_senha = str(input("\nDigite a sua senha:"))
    if user_email == email and user_senha == senha:
        print("\nO email e senha cadastrados correspondem aos que foram cadastrados anteriormente.")
        break
    else:
        print("\nO email e senha cadastrados não correspondem aos que foram cadastrados anteriormente.")