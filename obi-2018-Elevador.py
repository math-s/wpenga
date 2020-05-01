
N = int(input())
P = input().split()
p_list = []

for p in P:
    p_list.append(int(p))

p_list.sort()

for i in range(0, N):
    try:
        if i == 0 and p_list[i] > 8:
            print("N")
            break
        elif p_list[i+1] - p_list[i] > 8:
            print("N")
            break
    except IndexError:
        print("S")
