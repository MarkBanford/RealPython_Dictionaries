a_dict = {"one": 1, "Two": 2, "three": 3, "four": 4}

new_dict = {}
# Swap the k,v pair


for k, v in a_dict.items():
    new_dict[v] = k

# filter

filtered = {}

for k, v in a_dict.items():
    if v > 2:
        filtered[k] = v

# Calcs

incomes = {'Jeff': 12_000, "Annie": 230_000, "Glen": 5_000_000}

total_income = 0

for k, v in incomes.items():
    total_income += v

print(total_income)
