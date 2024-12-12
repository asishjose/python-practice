pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
    "bread":5,
    "butter":5
}

recipes = {
    "Butter chicken": [
        "chicken",
              "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}


pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
    "bread": 5,
    "butter": 5,
}

recipes = {
    "Butter chicken": [
        "chicken", "lemon", "cumin", "paprika", "chilli powder", "yogurt",
        "oil", "onion", "garlic", "ginger", "tomato puree", "almonds",
        "rice", "coriander", "lime"
    ],
    "Egg sandwich": [
        "egg", "bread", "butter"
    ],
    # other recipes...
}

# Simulate making the recipe multiple times
for k, v in recipes.items():
    if k == 'Egg sandwich':  # Running for 'Egg sandwich' recipe
        for i in v:
            if i in pantry:  # Check if ingredient exists in pantry
                print(f"Using {i}, current quantity: {pantry[i]}")  # Print current ingredient and quantity
                pantry[i] -= 1  # Decrease the quantity by 1
                print(f"Updated {i} quantity: {pantry[i]}")  # Print updated quantity

# Print updated pantry to verify the changes
print("\nUpdated Pantry after making Egg Sandwich:")
for item, quantity in pantry.items():
    print(f"{item}: {quantity}")


# for k,v in recipes.items():
#     if k=='Egg sandwich':
#         for i in v:
#             if i in pantry:
#                 pantry[i] = int(pantry[i])
#                 pantry[i] -= 1
#

# for k,v in recipes.items():
#     if k=='Egg sandwich':
#         for i in v:
#             for p,q in pantry.items():
#                 if p==i:
#                     print(i)
#                     pantry[i] = int(pantry[i])
#                     pantry[i] -= 1



#
# for item,quantity in pantry.items():
#     print(f"{item}:{quantity}")
#


# # recipe='omlette'
# print(recipes['Egg sandwich'])
# item = 'lemon1'
# for k,v in recipes.items():
#     print(f"food item:{k} values: {v}")
#     for i in v:
#         if item == i:
#             if i not in v:
#                 print("not in pantry")
#                 break
#             print(i)
#             pantry[i] -= 1
#             print(f"{item} in pantry decreased....")
#
# print(pantry)

