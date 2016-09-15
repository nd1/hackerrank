def prime_num(num_list):

    if n < 2:
        return False

    if n == 2:
        return True

    if not n & 1:
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True



T=int(input())
check_list = []

for i in range(T):
    check_list.append(int(input()))
for n in check_list:
    status = prime_num(n)
    if status == True:
        print("Prime")
    else:
        print("Not prime")
