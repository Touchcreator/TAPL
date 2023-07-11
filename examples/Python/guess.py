from collections import deque
q = deque()
q.appendleft("Guess my name: ")
q.appendleft(str(input(q[0])))
q.appendleft("Touchcreator")
q.appendleft(str(q[1]) == str(q[0]))
q.appendleft(27)

if q[1] == True:
    q.appendleft("That's right!")
    print(q[0])
    exec("""exit()""")
else:
    pass
q.appendleft("Wrong!")
print(q[0])
exec("""
import os
os.system("python guess.py")
""")
