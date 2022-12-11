states = {

    "California": {"capital": "Sacramento", "flower": "Poppy"},
    "New York": {"capital": "Albany", "flower": "Rose"},
    "Texas": {"capital": "Austin", "flower": "Bluebonnet"}

}

for state, facts in states.items():  # values are themselves dicts
    print(state, facts['flower'])

print(states["Texas"]["capital"])
