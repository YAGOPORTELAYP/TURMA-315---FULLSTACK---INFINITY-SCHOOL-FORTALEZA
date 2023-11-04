senha = str(input("\nDigite sua senha:")).strip()
if len(senha) >= 7 or len(senha) >= 12:
    print("\nA sua senha atende aos critérios.\n")
else:
    print("\nA sua senha não atende aos critérios.\n")