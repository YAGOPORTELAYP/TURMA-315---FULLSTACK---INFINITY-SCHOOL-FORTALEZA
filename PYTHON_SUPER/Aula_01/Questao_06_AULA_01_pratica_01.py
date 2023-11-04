n1 = int(input("\nDigite um Número:"))
n2 = int(input("\nDigite outro Número:"))
sinal = ""
par_impar = ""
calc = 0

op = str(input("""\n Diga qual das 4 operações aritiméticas básicas você quer fazer?
(A - Adição | S - Subtração | M - Multiplicação | D - Divisão)?\n""")).upper()

if op == "A":
    calc = n1 + n2
    
    if calc % 2 == 0:
        par_impar = "Par"
        print(f"O número é {par_impar}.")   
    if calc % 2 == 1:
        par_impar = "Ímpar"
        print(f"O número é {par_impar}.")   
    if calc > 0:
        sinal = "é de sinal Positivo"
        print(f"O número é {sinal}.")   
    if calc < 0:
        sinal = "é de sinal Negativo"
        print(f"O número é {sinal}.")
    if calc == 0:
        sinal = "Nulo"
        print(f"O número é {sinal}.")

if op == "S":
    calc = n1 - n2
    
    if calc % 2 == 0:
        par_impar = "Par"
        print(f"O número é {par_impar}.")   
    if calc % 2 == 1:
        par_impar = "Ímpar"
        print(f"O número é {par_impar}.")   
    if calc > 0:
        sinal = "é de sinal Positivo"
        print(f"O número é {sinal}.")   
    if calc < 0:
        sinal = "é de sinal Negativo"
        print(f"O número é {sinal}.")
    if calc == 0:
        sinal = "Nulo"
        print(f"O número é {sinal}.")
        
if op == "M":
    if (n1 != 0 and n2 != 0) or (n1 == 0 and n2 != 0) or (n1 != 0 and n2 == 0):
        calc = n1 * n2
        
        if calc % 2 == 0:
            par_impar = "Par"
            print(f"O número é {par_impar}.")   
        if calc % 2 == 1:
            par_impar = "Ímpar"
            print(f"O número é {par_impar}.")   
        if calc > 0:
            sinal = "é de sinal Positivo"
            print(f"O número é {sinal}.")   
        if calc < 0:
            sinal = "é de sinal Negativo"
            print(f"O número é {sinal}.")
        if calc == 0:
            sinal = "Nulo"
            print(f"O número é {sinal}.")
    else:
        print("O número é indeterminado.")
        
if op == "D":
    if n2 != 0:
        calc = n1 / n2
        
        if calc % 2 == 0:
            par_impar = "Par"
            print(f"O número é {par_impar}.")   
        if calc % 2 == 1:
            par_impar = "Ímpar"
            print(f"O número é {par_impar}.")   
        if calc > 0:
            sinal = "é de sinal Positivo"
            print(f"O número é {sinal}.")   
        if calc < 0:
            sinal = "é de sinal Negativo"
            print(f"O número é {sinal}.")
        if calc == 0:
            sinal = "Nulo"
            print(f"O número é {sinal}.")
    else:
        print("O número é indeterminado.")