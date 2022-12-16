# Rename file from .txt to .vtt.
# Before running, retype file name on line 7.
# Note that any double digit numbers in the transcript will be removed (line 25).

#Importing file
import re
file = open("filename.txt", "r")
actual = []
test = []

#Removing headers that start with a number
for line in file:
    try:
        first = line[0]
        if float(first):
            pass
    except:
        line = line.strip('\n')
        actual.append(line)

# Removing blanks from list
while("" in actual):
    actual.remove("")

#Removing headers that start with a letter
substring = "[0-9][0-9]"

for item in actual:
    for thing in substring:
        if thing in item:
            test.append(item)

for item in test:
    while item in actual:
        actual.remove(item)

#Printing final result
for item in actual:
    print(item)

#Testing Accuracy
#Accuracy depends on how many lines mentioned two digit numbers.
file = open("Wade.txt", "r")
original = []
originalcount = 0
finalcount = 0
for line in file:
    original.append(line)
for line in original:
    originalcount = originalcount + 1
finalcount = len(actual)
print()
print("----------------------------------------------")
print("Lines entered:" , originalcount)
print("Lines kept:" , finalcount)
removed = originalcount-finalcount
print("Lines removed:", removed)
accuracy1 = (originalcount-2)-finalcount
accuracy2 = originalcount/3
accuracy3 = round(((finalcount-accuracy2)/finalcount)*100, 2)
accuracy = 100-accuracy3
print("Accuracy:", accuracy,"%")
print("----------------------------------------------")
