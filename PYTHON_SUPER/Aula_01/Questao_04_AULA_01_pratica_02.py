print("\nDigite 10 Números:")
n = []

for i in range(10):
    num = int(input(f"\nDigite o #0{i + 1} número:"))
    n.append(num)
for i in range(10):
    if n[i] % 2 == 0:
        print(f"\nO Número {n[i]} é Par .")
    elif n[i] % 2 == 1:
        print(f"\nO Número {n[i]} é ímpar.")