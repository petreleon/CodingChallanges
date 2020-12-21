from parse import parse
from operator import methodcaller
import operator
import re
import numpy
import sys
from typing import Union
import math
from collections import defaultdict

file_opened = open("input", 'r')
lines = file_opened.read().splitlines()
positionAllergen = dict()
positionAllergenIndex = 0

positionIngredient = dict()
positionIngredientIndex = 0

dictOfValues = dict()
# lines = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()
# lines.append('')
assignedAllergens = set()
allAllergens = set()
allIngredients = set()
list_ = []
class Ingredients_Description:
    def __init__(self, setIngredients:set, setAllergens:set):
        self.ingredients = setIngredients
        self.allergens = setAllergens
for index, line in enumerate( lines ):
    (ingredients, allergens) = parse("{} (contains {})", line)
    ingredientsSet = list(ingredients.split(' '))
    allergensSet = list(allergens.split(', '))
    allAllergens.update(allergensSet)
    allIngredients.update(ingredientsSet)
    list_.append(Ingredients_Description(ingredientsSet, allergensSet))

for index, ingredients_Description in enumerate(list_):
    for ingredient in ingredients_Description.ingredients:
        for allergen in ingredients_Description.allergens:
            pair = (ingredient, allergen)
            dictOfValues[pair] = dictOfValues.get(pair, 0) + 1
list_ = []
ingredientsWithAllergens = set()
while len(dictOfValues):
    (ingredient, allergen) = max(dictOfValues.keys(), key=(lambda Key: dictOfValues[Key]))
    list_.append((ingredient, allergen))
    ingredientsWithAllergens.add(ingredient)
    for iterated in list(dictOfValues.keys()):
        if iterated[0] == ingredient or iterated[1] == allergen:
            del dictOfValues[iterated]

list_.sort(key= (lambda Element: Element[1]))

impossibleAllergens = allIngredients.difference(ingredientsWithAllergens)
count_ = 0
for line in lines:
    (ingredients, allergens) = parse("{} (contains {})", line)
    ingredients = ingredients.split(' ')
    for ingredient in ingredients:
        if ingredient in impossibleAllergens:
            count_ += 1
print(count_)
print(",".join([Element[0] for Element in list_]))
