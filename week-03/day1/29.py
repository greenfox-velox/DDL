ab = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same

if credits >= 50 and is_bonus == False:
    ab = ab - 2
elif credits < 50 and is_bonus == False:
    ab = ab - 1
elif is_bonus == True:
    ab = ab
else:
    print("Haha")
print(ab)

if not is_bonus:
    if credits > 50:
        ab -= 2
    else:
        ab -= 1
print(ab)

if not is_bonus:
    pass
if credits > 50:
    ab -= 2
else:
    ab -= 1 
print(ab)
