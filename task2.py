import re
import sys


start: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\md5_original.txt"
Check: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\md5_new1.txt"
#Pass in a diffrent file to write the results too

path = sys.argv[1]

file = open(start, "r")
pclines = file.readlines()

file2 = open(Check, "r")
checklines = file2.readlines()

file3 = open(path, "a")
counter = 0;

notMatched = []
#Just gonna assume that both of the files are the same length
for x in pclines:
    OGsLine = x.split(" ")
    NWsLine = checklines[counter].split(" ")
    #If the string comparision fails add both the MD5s and names to a list
    if(OGsLine[1] != NWsLine[1]):
        notMatched.append(x.rstrip()+" "+checklines[counter].rstrip())
    counter = counter + 1
tracker = 0
for x in notMatched:#Python string formating is a chore
    original = x.split(" ")
    output = "{name}: MD5 original = {md5OG}, MD5 new = {md5NW} ".format(name=original[0],md5OG=original[1],md5NW=original[3])
    file3.write(output)
    print(output)
    #Added both output methods to ensure that there where no issues.