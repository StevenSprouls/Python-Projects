_sum = 0
integer = 1

while integer <= 20:
    integer = integer + 1
    if integer % 2 == 0:
        _sum = _sum + integer
print("The sum of the first 10 even integers is " +  str(_sum))
