s = input()
n, l = input().split(" ")
n = int(n)
print (s[:n] + l + s[(n+1):])
