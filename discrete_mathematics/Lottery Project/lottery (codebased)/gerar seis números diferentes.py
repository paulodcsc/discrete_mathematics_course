
import random

lista = []  # cria o espaço pro armazenamento

for x in range(0, 6):  # a quantidade de números gerados
    # o número gerado é o igual ou o intervalo entre os dois
    n = random.randint(1, 60)

    # checa se ele já foi gerado alguma vez e cria a condição pra linha abaixo [lembrete: não é pra usar quando for fazer os gráficos]
    while n in lista:
        n = random.randint(1, 60)  # gera outro se a condição for verdadeira

    lista.append(n)  # coloca na lista depois de checar

# organiza a lista
lista.sort()

# mostra e salva
print(lista)
