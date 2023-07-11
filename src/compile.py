import sys
from collections import deque

filename = sys.argv[1]
edit = sys.argv[2]
file = open(filename, 'r')
new = open(edit, 'a')
contents = file.read()

new.write("from collections import deque\n")
new.write("q = deque()\n")

ifstate = ("""
if q[1] == True:
    pass
else:
    i+=int(q[0])
""")

elsestate = ("""
if q[1] != True:
    pass
else:
    i+=int(q[0])
""")

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
        new.write("q.appendleft(" + "\"" + contents[i+1:j]+"\"" ")\n")
        i = j
    if (contents[i] == "["):
        j = i
        while (contents[j] != "]"):
            j += 1
        new.write("q.appendleft(" + str(contents[i+1:j])+ ")\n")
        i = j
    if (contents[i] == "{"):
        j = i
        while (contents[j] != "}"):
            j += 1
        new.write("exec("+ "\""+ "\"" + "\"" + contents[i+1:j]+"\"" + "\""+ "\"" ")\n")
        i = j
    elif (contents[i] == "p"):
        new.write("print(q[0])\n")
    elif (contents[i] == "j"):
        new.write("q.appendleft(str(q[1]) + str(q[0]))\n")
    elif (contents[i] == "r"):
        new.write("q.appendleft(str(q[0]) + str(q[1]))\n")
    elif (contents[i] == "i"):
        new.write("q.appendleft(str(input(q[0])))\n")
    elif (contents[i] == "+"):
        new.write("q.appendleft(q[1] + q[0])\n")
    elif (contents[i] == "-"):
        new.write("q.appendleft(q[1] - q[0])\n")
    elif (contents[i] == "*"):
        new.write("q.appendleft(q[1] * q[0])\n")
    elif (contents[i] == "/"):
        new.write("q.appendleft(q[1] / q[0])\n")
    elif (contents[i] == "t"):
        new.write("q.appendleft(q[int(q[0])])\n")
    elif (contents[i] == ">"):
        new.write("q.appendleft(int(q[1]) > int(q[0]))\n")
    elif (contents[i] == "<"):
        new.write("q.appendleft(int(q[1]) < int(q[0]))\n")
    elif (contents[i] == "="):
        new.write("q.appendleft(str(q[1]) == str(q[0]))\n")
    elif (contents[i] == ":"):
        new.write(ifstate)
    elif (contents[i] == ";"):
        new.write(elsestate)
    i+=1