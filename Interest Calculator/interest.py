initial_balance = 1000
interest_rate = .05

balance_after_first_year = initial_balance + (initial_balance * interest_rate)
balance_after_second_year = balance_after_first_year + (balance_after_first_year * interest_rate)
balance_after_third_year = balance_after_second_year + (balance_after_second_year * interest_rate)

print("With the initial balance being 1000, the balance after the first year is " + str(balance_after_first_year))
print("The balance after the second year is " + str(balance_after_second_year))
print("The balance after the third year is " + str(balance_after_third_year))
