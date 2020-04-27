
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
