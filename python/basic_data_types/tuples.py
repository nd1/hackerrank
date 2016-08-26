n = int(input())
if n !=0:
    print(hash(tuple(map(int, input().split()))))
else:
    print(hash(()))
