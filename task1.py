# Help

import re
import sys

path: str = "C:\\Users\\EdmondMpc\\PycharmProjects\\lab3TaskAuto\\iris_full.txt"


def lessthan(new, current):
    if (new < current):
        return new
    else:
        return current


def greaterthan(new, current):
    if (new > current):
        return new
    else:
        return current


def read_data(name, lst):
    file = open(name, "r")
    lines = file.readlines()

    found = False
    for x in lines:
        if found:
            lst.append(x)
        if "@DATA" in x:
            found = True
    return lst


def process(list, pos):
    print(pos)
    min = 100
    max = 0
    counter = 0
    sum = 0
    se = 0;
    vi = 0;
    ve = 0;
    length = len(list)
    for x in list:
        temp = x.split(",")
        string = temp[pos]
        if (pos != 4):
            working = float(string)
            min = lessthan(working, min)
            max = greaterthan(working, max)
            sum = working + sum
            counter = counter + 1
        comp = string.strip()
        #print(comp)
        if (comp == "Iris-setosa"):
            se = se + 1
        elif (comp == "Iris-virginica"):
            vi = vi + 1
        elif (comp == "Iris-versicolor"):
            ve = ve + 1
    if(pos == 4):
        return se , vi, ve
    return min, max, sum / counter,


allLines = []

read_data(sys.argv[1], allLines)
#read_data(path, allLines)

zero = process(allLines, 0)
one = process(allLines, 1)
two = process(allLines, 2)
three = process(allLines, 3)
four = process(allLines, 4)

Slen = "Sepal Length: min = {min_value}, max = {max_value}, average = {average_value} \n".format(min_value=zero[0],
                                                                                                 max_value=zero[1],
                                                                                                 average_value=zero[2])
Swid = "Sepal Width: min = {min_value}, max = {max_value}, average = {average_value}\n".format(min_value=one[0],
                                                                                                  max_value=one[1],
                                                                                                  average_value=one[2])
Plen = "Petal Length: min = {min_value}, max = {max_value}, average = {average_value}\n".format(min_value=two[0],
                                                                                                      max_value=two[1],
                                                                                                      average_value=two[
                                                                                                          2])
Pwid = "Petal Width: min = {min_value}, max = {max_value}, average = {average_value}\n".format(
    min_value=three[0], max_value=three[1], average_value=three[2])
types = "Types: Iris Setosa = {num_iris_setosa}, Iris Versicolor = {num_iris_versicolor}, Iris Virginica = {num_iris_virgin}".format(
     num_iris_setosa =four[0],  num_iris_versicolor =four[1],  num_iris_virgin=four[2])
out = Slen + Swid + Plen + Pwid + types
print(out)

##'Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)
