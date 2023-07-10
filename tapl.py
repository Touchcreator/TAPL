import sys
from collections import deque

filename = sys.argv[1]
file = open(filename, 'r')
ignore = [" ", "\n", "\t"]
contents = file.read()

q = deque()

i = 0
while i < len(contents):
    quote_count = 0
    if (contents[i] == "\""):
        quote_count += 1
        j = i
        while (quote_count != 2):
            j += 1
            if (contents[j] == "\""):
                quote_count += 1
        q.appendleft(contents[i+1:j])
        i = j
    if (contents[i] == "["):
        j = i
        while (contents[j] != "]"):
            j += 1
        q.appendleft(int(contents[i+1:j]))
        i = j
    if (contents[i] == "{"):
        j = i
        while (contents[j] != "}"):
            j += 1
        exec(str(contents[i+1:j]))
        i = j
    elif (contents[i] == "p"):
        print(q[0])
    elif (contents[i] == "j"):
        q.appendleft(str(q[1]) + str(q[0]))
    elif (contents[i] == "r"):
        q.appendleft(str(q[0]) + str(q[1]))
    elif (contents[i] == "i"):
        q.appendleft(str(input(q[0])))
    elif (contents[i] == "+"):
        q.appendleft(q[1] + q[0])
    elif (contents[i] == "-"):
        q.appendleft(q[1] - q[0])
    elif (contents[i] == "*"):
        q.appendleft(q[1] * q[0])
    elif (contents[i] == "/"):
        q.appendleft(q[1] / q[0])
    elif (contents[i] == "t"):
        q.appendleft(q[int(q[0])])
    else:
        if contents[i]  not in ignore:
            print("Error at character " + str(i) + " " + str(contents[i]))
            print("That isn't a command!")
            break
    i+=1