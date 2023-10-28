char = str(input("Digite uma letra ou uma frase:")).lower().strip()
char = char.replace(" ","")
i = 0

for string in char:
    i +=1
    print(f"Caracter {i}: {string}")