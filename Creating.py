# Key-Value pairs (relational)
# Keys can be Strings, Int, Float, Bool, Tuples (Have hash functions)
# Dictionaries are iterable, has an __iter__ method
# Since Python 3.6, dictionary items have the same order as how they are entered
# guts of python built using dictionaries


print(dir({}))


capitals = {

    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"

}

# dict from tuples
my_dog = (

    ("name", "Freida"),
    ("age", 5),
    ("nicknames", ["Fru-Frue", "Tee tee"]),
    ("hungry", True)

)

dog_dict = dict(my_dog)

dog_dict["breed"] = "poodle"  # adding an item to the dictionary(dictname[key]=value)

dog_dict["age"] = 6

del dog_dict["hungry"]  # deleting an item


