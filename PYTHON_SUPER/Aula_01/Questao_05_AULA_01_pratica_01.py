sum = 0

for i in range(1,5):
    num = int(input(f"Digite o #0{i} Número:"))
    sum = sum + num

med = sum/4
if med >= 7 and med < 10:
    print("Aprovado.")
if med < 7:
    print("Reprovado.")
if med == 10:
    print("Aprovado com Distinção.")