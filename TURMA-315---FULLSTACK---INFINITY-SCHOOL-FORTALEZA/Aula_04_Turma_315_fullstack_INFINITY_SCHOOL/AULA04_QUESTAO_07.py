big = 0
while True:
    n1 = float(input("Digite o primeiro número:"))
    n2 = float(input("Digite o segundo número:"))
    n3 = float(input("Digite o terceiro número:"))
    n4 = float(input("Digite o quarto número:"))
    n5 = float(input("Digite o quinto número:"))
    if n1 != n2 and n1 != n3 and n1 != n4 and n1 != n5:
        break
    else:
        print("""
Digite 5 números diferentes!
              """)
        continue
while True:
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 :
        big = n1
    if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5 :
        big = n2
    if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5 :
        big = n3
    if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5 :
        big = n4
    if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4 :
        big = n5
    break
print(f"O maior número é: {big}")