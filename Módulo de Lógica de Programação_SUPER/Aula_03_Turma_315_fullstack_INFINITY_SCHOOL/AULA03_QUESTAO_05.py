num_list = int(input("Quantos números há na sua lista? Digite a quantidade:"))
sum = 0

for lista in range (num_list):
    list_num = int(input("Insira os números da lista:"))
    sum = sum + list_num

med = sum/num_list
print(f"A média dos números da lista é: {med}")