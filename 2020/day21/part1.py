import re


def main():
    f = open("input_test.txt", "r")
    x = f.read().splitlines()
    ingredients = ingredient_builder(x)
    allergens = allergen_builder(x)

    allergen_list = {}
    for i in range(len(ingredients)):
        for i2 in range(len(ingredients)):
            ing = set(ingredients[i]).intersection(set(ingredients[i2]))
            all = set(allergens[i]).intersection(set(allergens[i2]))
            for ingred in allergen_list:
                ing = ing - set([ingred])
                all = all - set([allergen_list[ingred]])
            if len(ing) == 1 and len(all) == 1:
                allergen_list[list(ing)[0]] = list(all)[0]
                print(ing, all)
    for i in range(len(ingredients)):
        

def ingredient_builder(x):
    ingredients = []
    for i in x:
        ingredients.append(i.split(' (')[0].split())
    return ingredients


def allergen_builder(x):
    allergens = []
    for i in x:
        allergens.append(i.split('contains ')[1].split(')')[0].split(', '))
    return allergens


if __name__ == '__main__':
    main()
