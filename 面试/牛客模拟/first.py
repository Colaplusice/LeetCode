def cal():
    s = raw_input()
    list = s.split(" ")

    x = int(list[0])
    f = int(list[1])
    d = int(list[2])
    p = int(list[3])
    if d==0:
        print(0)
        return
    if f >d/x:
        print(d/x)
        return

    days=f
    d-=(f*x)

    all=p+x
    days+=d/all
    print(days)
if __name__ == '__main__':
    cal()