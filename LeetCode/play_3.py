from collections import OrderedDict
a=OrderedDict()


a[0]=1
a[1]=2
a[2]=4
print(a)
a.move_to_end(2,last=False)
print(a)

a.popitem()

print(a)