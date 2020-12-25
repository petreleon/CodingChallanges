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
subjectNumber = 7
dictOfValues = dict()
# publicKey = pow(7,secretKey,20201227)
publicKey1 = int(lines[0])
publicKey2 = int(lines[1])
# publicKey1 = 5764801
# publicKey2 = 17807724
iterator = 1
for i in range(20201227):
    dictOfValues[iterator] = i
    iterator = iterator * 7 % 20201227

def transfrom(subject, loop):
    number = 1
    for _ in range(loop):
        number *= subject
        number = number % 20201227
    return number
    
print(dictOfValues[publicKey1])
print(dictOfValues[publicKey2])
# for key1 in dictOfValues.keys():
#     for key2 in dictOfValues.keys():
#         if key1*dictOfValues[key2]%20201227 == encription1 and key2*dictOfValues[key1]%20201227 == encription1:
#             print
print(transfrom(publicKey1, dictOfValues[publicKey2]),transfrom(publicKey2,dictOfValues[publicKey1]))
