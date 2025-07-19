# liczenie zysku z konta oszczędnościowego

start_amount = 10000
number_of_years = 3
interest_rate = 0.08
first_year = (start_amount * interest_rate) + start_amount
second_year = (first_year * interest_rate) + first_year
third_year = (second_year * interest_rate) + second_year

result = round(third_year - start_amount, 2)

print("You will earn: ", result)