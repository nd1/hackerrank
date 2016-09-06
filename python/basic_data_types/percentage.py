n = int(input())
grades = {}
for _ in range(n):
    info = input().split(" ")
    scores = list(map(float, info[1:]))
    grades.update({info[0]: sum(scores)/len(scores)})

print('{0:.2f}'.format(grades[input()]))
