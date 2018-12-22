def s():
    l = ["Alice", "Bob", "Cathy", "Dave"]

    t = 0
    val = input()
    val = int(val)
    j = 0
    while j < val:
        j += 4 * pow(2, t)
        t += 1
    if j == val:
        print("Dave")
    j -= 4 * pow(2, t - 1)
    sub = val - j
    index = 1
    if sub % t == 0:
        index = int(sub / t - 1)
    else:
        index = int(sub / t)
    print(l[index])


if __name__ == "__main__":
    s()
