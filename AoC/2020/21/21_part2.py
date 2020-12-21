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
dictOfValues = dict()
lines = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()
# lines.append('')
assignedAllergens = set()
allAllergens = set()
allIngredients = set()
list_ = []
class Ingredients_Description:
    def __init__(self, setIngredients:set, setAllergens:set):
        self.ingredients = setIngredients
        self.allergens = setAllergens
for line in lines:
    (ingredients, allergens) = parse("{} (contains {})", line)
    ingredientsSet = set(ingredients.split(' '))
    allergensSet = set(allergens.split(', '))
    allAllergens.update(allergensSet)
    allIngredients.update(ingredientsSet)
    list_.append(Ingredients_Description(ingredientsSet, allergensSet))

detectedAllergen = dict()

for allergen in allAllergens:
    dictOfValues[allergen] = allIngredients.copy()
for ingredients_Description in list_:
    for allergen in ingredients_Description.allergens:
        dictOfValues[allergen].intersection_update(ingredients_Description.ingredients)

while len(detectedAllergen) != len(allAllergens):
    for allergen in dictOfValues.keys():
        if allergen not in detectedAllergen.keys() and len(dictOfValues[allergen]) == 1:
            detectedAllergen[allergen] = next(iter(dictOfValues[allergen]))
            for allergen2 in dictOfValues.keys():
                if allergen != allergen2:
                    dictOfValues[allergen2].discard(detectedAllergen[allergen])
listOfKeys = list(dictOfValues.keys())
listOfKeys.sort()

print(",".join([detectedAllergen[key] for key in listOfKeys]))
