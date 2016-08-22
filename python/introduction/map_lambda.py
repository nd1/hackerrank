# switched to python 3 today

fib = lambda x: x if x <2 else (fib(x-1) + fib(x-2))
cube = lambda x: x**3
fib_list = [fib(x) for x in range(0,int(input()))]
print (list((map(cube, fib_list))))
