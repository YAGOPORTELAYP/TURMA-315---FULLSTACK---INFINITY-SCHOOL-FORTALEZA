sexo = str(input("Digite o sexo: F/M:"))

if sexo in "fF":
    print(f"{sexo} - Sexo Feminino")
elif sexo in "mM": 
    print(f"{sexo} - Sexo Masculino")
else:
    print("Sexo Inválido!")