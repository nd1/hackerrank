N = int(input())
phone_book = {}

for _ in range(N):
    k, v = input().split(' ')
    phone_book.update({k:v})

while True:
    try:
        person = input()
        if person in phone_book:
            print('%s=%s' % (person, phone_book[person]))
        else:
            print('Not found')
    except:
        break
