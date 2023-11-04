n1 = int(input("Insira um número:"))
n2 = int(input("Insira outro número:"))

if n1 > n2:
    print(f"{n1} é o maior deles!")
elif n2 > n1:
    print(f"{n2} é o maior deles!")
else:
    print(f"{n1} e {n2} são iguais!")