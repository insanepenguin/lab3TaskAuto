import re
import sys


start: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\md5_original.txt"
Check: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\md5_new1.txt"

file = open(start, "r")
pclines = file.readlines()

file2 = open(Check, "r")
checklines = file2.readlines()
counter = 0;

notMatched = []

for x in pclines:
    OGsLine = x.split(" ")
    NWsLine = checklines[counter].split(" ")
    
    if(OGsLine[1] != NWsLine[1]):
        notMatched.append(x.rstrip()+" "+checklines[counter].rstrip())
    counter = counter + 1
tracker = 0
for x in notMatched:
    original = x.split(" ")
    
    output = "{name}: MD5 original = {md5OG}, MD5 new = {md5NW} ".format(name=original[0],md5OG=original[1],md5NW=original[3])
    
    print(output)
    
