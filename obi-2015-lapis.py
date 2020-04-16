n = int(input())
dic = []


def split(word):
    return [char for char in word]


for i in range(0, n):
    in_var = input()
    aux = split(in_var)
    dic.append(aux)


for i in range(0, n):
    for j in range(0, n):
        if dic[i][j] == '0':
            for x in range(0, n):
                for y in range(0, n):
                    if dic[x][y] != '0':
                        value = abs(i - x) + abs(j - y)
                        if value > 9:
                            value = 9
                        if dic[x][y] == '*':
                            dic[x][y] = str(value)
                        elif int(dic[x][y]) > value:
                            dic[x][y] = str(value)


res = " "
for i in range(0, n):
    print(res.join(dic[i]))


