sexo = str(input("Digite o seu sexo ( M - Masculino | F - Feminino ) :\n")).lower()

if sexo in "f":
    print("Sexo Feminino.")
if sexo in "m":
    print("Sexo Masculino.")
else:
    print("Sexo inválido.")