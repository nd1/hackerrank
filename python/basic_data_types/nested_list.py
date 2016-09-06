n = int(input())
students = sorted([[input(), float(input())] for _ in range(n)])

second_lowest = sorted(list(set(grade for [_, grade] in students)))[1]

print("\n".join(name for [name, grade] in students if grade == second_lowest))
