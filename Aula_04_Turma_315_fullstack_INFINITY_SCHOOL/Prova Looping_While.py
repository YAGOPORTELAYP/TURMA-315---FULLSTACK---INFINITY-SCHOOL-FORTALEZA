n = 0
sum = 0
med = 0
while True:
    num = int(input("Digite um número. (Ou digite 0 para encerrar) :"))
    sum += num
    n += 1
    if num == 0:
        med = sum/n
        break

print(f"Foram digitados {n} números.\nA soma deles é de {med}.\nE a média deles é de {med}.")
# test boy