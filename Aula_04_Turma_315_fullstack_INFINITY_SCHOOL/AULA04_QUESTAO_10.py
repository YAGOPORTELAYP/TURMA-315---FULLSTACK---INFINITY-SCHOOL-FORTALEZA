print("""
Digite 2 Números inteiros:
""")
n1 = int(input("""digite o primeiro número: """))
n2 = int(input("""
digite o segundo número: """))
n = " "
while True:
    for i in range(n1 + 1,n2):
        n += str(i) + " "
    break
print(f"""
Os números que estão entre os números {n1} e {n2} são:
""")
print(f"""
{n}
""")