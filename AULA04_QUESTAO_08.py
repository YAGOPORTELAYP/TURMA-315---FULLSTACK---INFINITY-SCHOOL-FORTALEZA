print("""
Digite 5 números:
      """)
sum = 0
med = 0
while True:
    for n in range(5):
        float(input(f"digite o {n+1}º número:"))
        sum += n + 1
    med = sum/5
    break
print(f"""
A soma dos 5 números é: {sum}
""")
print(f"""A média dos 5 números é: {med}
""")
