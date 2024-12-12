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
#adding items to pantry
pantry['poth']='100'
#adding recipes
recipes['omlette']=['bread','egg']
# del pantry['poth']
# del recipes['omlette']

#dynamically removing recipes or pantry items
def remove_recipes(recipes,item):
    if item in recipes:
        del recipes[item]
    else:
        print('item not found')

remove_recipes(recipes,'omlette')

#removing ingredient in recipe
# recipes["Butter chicken"].remove("chilli powder")
def remove_ingredient(ingredient,recipe_name,recipes):
    recipes[recipe_name].remove(ingredient)

remove_ingredient('chicken','Butter chicken',recipes)

#updating quantity
# pantry['poth']=int(pantry['poth'])
# pantry['poth']-=1
def reduce_quantity(item,pantry):
    pantry[item]=int(pantry[item])
    pantry[item]-=1

reduce_quantity('poth',pantry)



# print(pantry)
for item,quantity in pantry.items():
    print(f"{item}:{quantity}")
# print(recipes)
for recipe,ingredients in recipes.items():
    print(f"{recipe}:{ingredients}")