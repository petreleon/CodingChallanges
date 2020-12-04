file_opened = open("input.txt", 'r')
lines = file_opened.read().splitlines()
lines.append('')
import re
def isValidHexaCode(str):
 
    # Regex to check valid 
    # hexadecimal color code.
    regex = "^#([a-f0-9]{6})$"
 
    # Compile the ReGex 
    p = re.compile(regex)
 
    # If the string is empty 
    # return false
    if(str == None):
        return False
 
    # Return if the string 
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

def isValidPassportID(str):
 
    # Regex to check valid 
    # hexadecimal color code.
    regex = "^([0-9]{9})$"
 
    # Compile the ReGex 
    p = re.compile(regex)
 
    # If the string is empty 
    # return false
    if(str == None):
        return False
 
    # Return if the string 
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

def checkValid(D):
    if not(len(D.keys()) == 8 or len(D.keys()) == 7 and 'cid' not in D.keys()):
        return False
    # part 2 begins
    byr = int(D['byr'])
    if not(byr >= 1920 and byr <= 2002):
        return False
    iyr = int(D['iyr'])
    if not(iyr >= 2010 and iyr <= 2020):
        return False
    eyr = int(D['eyr'])
    if not(eyr >= 2020 and eyr <= 2030):
        return False
    hgt = D['hgt']
    if hgt[-2:] not in ['cm', 'in']:
        return False
    hgt_v = int(hgt[:-2])
    if hgt[-2:] == 'cm':
        if not(hgt_v >= 150 and hgt_v <= 193):
            return False
    if hgt[-2:] == 'in':
        if not(hgt_v >= 59 and hgt_v <= 76):
            return False

    hcl = D['hcl']
    if not isValidHexaCode(hcl):
        return False
    ecl = D['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    pid = D['pid']
    if not isValidPassportID(pid):
        return False
    # part 2 ends
    return True

from parse import *
validPass = 0
D = dict()
for line in lines:
    if len(line) > 0:
        key_values = line.split(' ')
        for key_value in key_values:
            key, value = key_value.split(":")
            D[key] = value
    else: 
        if checkValid(D):
            validPass += 1
        D = dict()
print(validPass)

