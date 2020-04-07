import re
import sys


start: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\md5_original.txt"
Check: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\md5_new1.txt"

file = open(start, "r")
pclines = file.readlines()

file2 = open(Check, "r")
checklines = file2.readlines()
MD5sum = []
for x in checklines:
    new = x.split(" ")
    for x in new:
       y = x.strip()
       MD5sum.append(y)
changed = []
for x in pclines:
    combo = x.split(" ")
    combo.remove(combo[1])
    if(not(combo[0])in MD5sum):
        changed.append(combo[0])
        name = combo[1].split("/")
        changed.append(name[3].strip())
print(changed)
