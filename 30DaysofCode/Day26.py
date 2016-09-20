ret_day, ret_month, ret_year = [int(x) for x in input().split(' ')]
act_day, act_month, act_year = [int(x) for x in input().split(' ')]

if ret_year < act_year:
    print(0)
else:
    if ret_year > act_year:
        print(10000)
    else: #same year
        if ret_month > act_month:
            print(500 * (ret_month - act_month))
        elif ret_month < act_month:
            print(0)
        else:
            if ret_day > act_day:
                print(15 * (ret_day - act_day))
            else:
                print(0)
