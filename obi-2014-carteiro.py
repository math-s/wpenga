'''
Carteiro
Um carteiro é o responsável por entregar as encomendas na rua de Joãozinho. Por política da empresa, as encomendas devem ser entregues na mesma ordem que foram enviadas, mesmo que essa não seja a forma mais rápida. Cansado de subir e descer aquela rua tantas vezes, nosso amigo quer mostrar à empresa quanto tempo ele leva para entregar as encomendas, na tentativa de derrubar essa política.

A rua de Joãozinho tem N casas. Naturalmente, as casas são numeradas de forma ordenada (não necessariamente por números consecutivos). Como as casas possuem aproximadamente o mesmo tamanho, você pode assumir que o carteiro leva uma unidade de tempo para caminhar de uma casa até a casa imediatamente vizinha.

Há M encomendas para essa rua, que devem ser entregues na mesma ordem em que chegaram. Cada encomenda contém o número da casa onde deve ser entregue.

Escreva um programa que determine quanto tempo o carteiro levará para entregar todas as encomendas, assumindo que quando o tempo começa a contar, ele está na primeira casa (a de menor número), e o tempo termina de contar quando todas as encomendas foram entregues (mesmo que o carteiro não esteja de volta na primeira casa). Você pode desprezar o tempo para colocar a encomenda na caixa de correio (ou seja, se ele só tiver uma encomenda, para a primeira casa, a resposta para o problema é zero).

Entrada
A primeira linha contém dois inteiros, N e M, respectivamente o número de casas e o número de encomendas. A segunda linha contém N inteiros em ordem estritamente crescente, indicando os números das casas. A terceira linha contém M inteiros indicando os números das casas onde as encomendas devem ser entregues, na ordem dada na entrada.
Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, o tempo que o carteiro levará para entregar todas as encomendas na ordem correta, assumindo que ele começa na casa de menor número.
Restrições
1 ≤ N ≤ 45.000 e 1 ≤ M ≤ 45.000
O número de cada casa é um inteiro entre 1 e 1.000.000.000
Informações sobre a pontuação
Para um subconjunto dos casos de teste totalizando 30 pontos, 1 ≤ N ≤ 1000 e 1 ≤ M ≤ 1000.
Exemplos
Entrada
5 5
1 5 10 20 40
10 20 10 40 1
Saída
10

Entrada
3 4
50 80 100
80 80 100 50
Saída
4


'''
import time
start_time = time.time()


def func(var1, var2, var3):
    var_list1 = var1.split()
    num_casas = var_list1[0]
    num_encomendas = var_list1[1]

    casas_list = var2.split()
    encomendas_list = var3.split()

    aux = 0
    x_pos = casas_list[aux]
    x_count = 0

    for i in range(int(num_encomendas)):
        while int(x_pos) != int(encomendas_list[i]):
            if int(x_pos) < int(encomendas_list[i]):
                aux = aux + 1
                x_pos = casas_list[aux]
                x_count = x_count + 1
            elif int(x_pos) > int(encomendas_list[i]):
                aux = aux - 1
                x_pos = casas_list[aux]
                x_count = x_count + 1
    return x_count


enter = input()
str_l = enter.split("\n")

str_l1 = str_l[0]
str_l2 = str_l[1]
str_l3 = str_l[2]

print(func(str_l1, str_l2, str_l3))

print("--- %s seconds ---" % (time.time() - start_time))
