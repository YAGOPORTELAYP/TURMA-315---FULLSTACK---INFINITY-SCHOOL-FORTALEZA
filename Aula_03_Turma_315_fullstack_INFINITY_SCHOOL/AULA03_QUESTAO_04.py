num_i = int(input("Insira o valor inicial de uma sequência de números para realizar a soma dos números dentro desse intervalo:"))
num_f = int(input("Insira o valor final de uma sequência de números para realizar a soma dos números dentro desse intervalo:"))
num_f += 1
sum = 0

for num in range (num_i,num_f):
    sum = sum + num

print(f"A soma dos números de {num_i} a {num_f} é: {sum}")