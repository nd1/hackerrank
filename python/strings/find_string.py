string = input()
sub = input()

print(sum(string[i:].startswith(sub) for i in range(len(string))))
