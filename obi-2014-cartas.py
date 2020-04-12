'''
Cartas
Beatriz gosta muito de jogar cartas com as amigas. Para treinar memória e raciocínio lógico, ela inventou um pequeno passatempo com cartas. Ela retira as cinco primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para baixo.

Então ela olha, por um breve instante, cada uma das cartas da sequência (e logo as recoloca na mesa, com a face para baixo). Usando apenas a sua memória, Beatriz deve agora dizer se a sequência de cartas está ordenada crescentemente, decrescentemente, ou não está ordenada.

De tanto jogar, ela está ficando cansada, e não confia em seu próprio julgamento para saber se acertou ou errou. Por isso, ela pediu para você fazer um programa que, dada uma sequência de cinco cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.

Entrada
A entrada consiste de uma única linha que contém as cinco cartas da sequência. Os valores das cartas são representados por inteiros entre 1 e 13. As cinco cartas têm valores distintos.
Saída
Seu programa deve produzir uma única linha, contendo um único caractere maiúsculo: "C" caso a sequência dada esteja ordenada crescentemente, "D" se estiver ordenada decrescentemente, ou "N" caso contrário.
Restrições
o valor de cada carta é um inteiro entre 1 e 13.
Exemplos
Entrada
1 2 3 5 6
Saída
C

Entrada
5 7 10 9 11
Saída
N

Entrada
12 10 4 3 2
Saída
D

'''


def func(cards):
    cards_list = cards.split()
    d = False
    c = False

    for i in range(len(cards_list)):
        if int(cards_list[i]) > 13:
            return "Sequência de cartas inválida!"
        if i != 0:
            if int(cards_list[i]) < int(cards_list[i - 1]):
                d = True
            elif int(cards_list[i]) > int(cards_list[i - 1]):
                c = True

    if d and c:
        return "N"

    elif d and not c:
        return "D"

    elif c and not d:
        return "C"


line = input()
print(func(line))

'''

TAREFA: Cartas
LINGUAGEM: Python3

Compilação correta

Fase de testes -- Tempo Limite para cada execução: 1000 ms
Teste  1: .....     (10 pontos)
Teste  2: ....     (10 pontos)
Teste  3: ....     (10 pontos)
Teste  4: ....     (10 pontos)
Teste  5: ....     (10 pontos)
Teste  6: ....     (10 pontos)
Teste  7: ....     (10 pontos)
Teste  8: ....     (10 pontos)
Teste  9: ....     (10 pontos)
Teste 10: ....     (10 pontos)

Total: 100 pontos (de 100 possíveis)

Legenda: 
  .: resultado correto           X: resultado incorreto
  E: erro em tempo de execução   M: Referência a memória inválida  
  S: programa não gerou saída    T: tempo limite excedido
  V: violação de recursos


'''
