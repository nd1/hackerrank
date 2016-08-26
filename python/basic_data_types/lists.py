L = []
n= int(input())
for _ in range(n):
    command, *args = input().strip().split(' ')
    if command == 'print':
        print(L)
    else:
        getattr(L, command)(*(int(x) for x in args))
