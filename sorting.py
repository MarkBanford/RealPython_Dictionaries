countryPopulation = {

    'USA': 328_000_000,
    'France': 67_000_000,
    'China': 1_393_000_000

}

print(countryPopulation)

sortedByKey = {k: v for k, v in sorted(countryPopulation.items())}
print(sortedByKey)

sortedByVal = {k: v for k, v in
               sorted(countryPopulation.items(), key=lambda v: v[1])}  # references 2nd element which is value

print(sortedByVal)

# reverse sorting

reverse_key = {k: v for k, v in sorted(countryPopulation.items(), reverse=True)}
reverse_value = {k: v for k, v in
                 sorted(countryPopulation.items(), key=lambda v: v[1], reverse=True)}

print(reverse_key)
print(reverse_value)
