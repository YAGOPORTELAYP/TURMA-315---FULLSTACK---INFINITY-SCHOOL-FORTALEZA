primo = int(input("Insira uma número para saber se ele é primo:"))
n = primo + 1
num_div_primo = 0

for numero in range (1,n):
    if primo%numero == 0:
        num_div_primo +=1          

if num_div_primo == 2:
    print(f"o número {primo} é Primo!")

else:
    print(f"o número {primo} não é Primo!")