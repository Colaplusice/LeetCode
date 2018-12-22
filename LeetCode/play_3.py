def a():
    b = 1
    while True:
        # 产出b 接收a
        a = yield b
        print("this is a", a)


s = a()
next(s)
res = s.send(4)
print(res)
