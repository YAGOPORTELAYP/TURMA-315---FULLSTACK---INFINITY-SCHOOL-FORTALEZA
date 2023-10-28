frase = str(input("Digite uma frase:")).lower().strip()
numeros = "0123456789"

for caractere in frase:
    if caractere in numeros:
        print(f"Número encontrado: {caractere}")