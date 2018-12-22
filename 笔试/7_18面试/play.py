dicts = {}

dicts[1] = 2
dicts[2] = 4

sd = dicts.items()

sd = list(sd)
sd.pop(0)

print(dicts)
print(sd)
print(dict(sd))
