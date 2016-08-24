mealCost = float(input())
tip = float(input())
tax = float(input())

print ('The total meal cost is %d dollars.' % round((mealCost + mealCost*tip/100.0 + mealCost*tax/100.0)))
