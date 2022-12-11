objects = ['blue', 'apple', 'dog']
categories = ['colour', 'fruit', 'pet']

a_dict = {k: v for k, v in zip(objects, categories)}

# Swap the k,v pair

new_dict = {v: k for k, v in a_dict.items()}
print(new_dict)

# filter
num_dict = {"one": 1, "Two": 2, "three": 3, "four": 4}
num_dict = {k: v for k, v in num_dict.items() if v > 2}
print(num_dict)

# calcs

incomes = {'Jeff': 12_000, "Annie": 230_000, "Glen": 5_000_000}

income_total = sum(v for k, v in incomes.items())
print(income_total)
print(sum(incomes.values()))

# sort by key

sorted_incomes = {k: incomes[k] for k in sorted(incomes)}
print(sorted_incomes)

# sort by values

sorted_values = {k: v for k, v in sorted(incomes.items(), key=lambda item: item[1])}
print(sorted_values)
