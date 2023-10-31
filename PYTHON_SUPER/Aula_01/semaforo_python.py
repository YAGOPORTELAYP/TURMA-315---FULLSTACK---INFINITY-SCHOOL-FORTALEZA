# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO ESCOLHER UMA COR DO SEMÁFORO:
# VERDE
# VERMELHO 
# AMARELO
# QUALQUER OUTRA COR SERÁ CONSIDERADO INVÁLIDO
# E MOSTRE NA TELA
# "ACELERE!" CASO SEJA VERDE
# "ATENÇÃO!" CASO SEJA AMARELO
# "PARE!" CASO SEJA VERMELHO
# "COR INVÁLIDA" PARA OUTRAS CORES

RESOLUÇÃO 1:
cor = str(input("Escolha uma cor do semáforo: "))

if cor == "vermelho":
    print("Pare!")
elif cor == "amarelo":
    print("Atenção!")
elif cor == "verde":
    print("Acelere!")
else:
    print("Cor inválida")
