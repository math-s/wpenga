
number = int(input())
prime_number_list = []
count = []
res = 1
for val in range(1, number//3):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            prime_number_list.append(val)

for i in range(0, len(prime_number_list)):
    count.append(0)
    while number % prime_number_list[i] == 0:
        count[i] += 1
        number = number/prime_number_list[i]
    count[i] += 1

res = 1
for aux in count:
    res = res * aux

print(res)

