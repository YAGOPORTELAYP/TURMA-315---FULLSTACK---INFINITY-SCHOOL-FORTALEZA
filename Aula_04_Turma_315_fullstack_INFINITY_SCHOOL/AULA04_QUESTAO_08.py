print("""
Digite 5 números:
      """)
sum = 0
med = 0
while True:
    for n in range(5):
        
        num = float(input(f"digite o {n+1}º número:"))
        sum += num
    break
med = sum/5
print(f"""
A soma dos 5 números é: {sum}
""")
print(f"""A média dos 5 números é: {med}
""")
