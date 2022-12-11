my_dog = (

    ("name", "Freida"),
    ("age", 5),
    ("nicknames", ["Fru-Frue", "Tee tee"]),
    ("hungry", True)

)

dog_dict = dict(my_dog)

del dog_dict["hungry"]

if "hungry" in dog_dict:
    print(dog_dict["hungry"])

# iterating over dictionaries


capitals = {

    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"

}

for state, city in capitals.items(): # .items() produces tuples under the hood
    print(state, city)

