class RecentCounter:
    def __init__(self):
        self.ping_value = set()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_value.add(t)
        index = 0
        for each in self.ping_value:
            if each < t - 3000:
                index += 1
        for i in range(index):
            self.ping_value.pop()
        return len(self.ping_value)


if __name__ == "__main__":

    obj = RecentCounter()
    sd = []
    for each in range(10000):
        param_1 = obj.ping(each)
        sd.append(param_1)
    print(sd)
