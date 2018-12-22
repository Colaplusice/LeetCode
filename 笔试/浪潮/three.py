import sys

res = []
s = sys.stdin.readline().strip("\n")
while s != "":
    res.append(s)
    s = sys.stdin.readline().strip("\n")
print(res)
