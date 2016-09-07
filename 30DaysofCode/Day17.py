#Write your code here

from math import exp
class Calculator:

    def power(self, x, y):
        self.x = x
        self.y = y
        if x < 0 or y < 0:
            raise ValueError('n and p should be non-negative')
        return x**y

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
        
