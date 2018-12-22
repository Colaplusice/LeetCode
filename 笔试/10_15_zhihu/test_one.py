a_list = input().split(" ")


base_array = []
for _ in range(len(a_list)):
    base_array.extend(input().strip().split(" "))

base_array = [int(a) for a in base_array]
base_array = sorted(base_array)
print(" ".join([str(a) for a in base_array]))
