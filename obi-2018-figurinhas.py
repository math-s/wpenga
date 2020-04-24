in_a = input().split(" ")
N = int(in_a[0])
C = int(in_a[1])
M = int(in_a[2])


in_b = input().split(" ")
in_c = input().split(" ")

counter = 0
for i in in_b:
    if i in in_c:
        pass
    else:
        counter += 1

print(counter)



