print("\nDigite 10 Números:")
par_impar = ""

for i in range(1,11):
    num = int(input(f"\nDigite o #0{i} número:"))
    if num % 2 == 0:
        par_impar = "Par"
        print(f"\nO Número {num} é {par_impar}.")
    elif num % 2 == 1:
        par_impar = "ímpar"
        print(f"\nO Número {num} é {par_impar}.")