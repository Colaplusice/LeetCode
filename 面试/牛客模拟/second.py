


def cal():
    lines=raw_input()

    for i in range(int(lines)):
        print(i)
        s=raw_input()
        lis=s.split(" ")

        days=int(lis[0])
        one=int(lis[1])
        two=int(lis[2])
        three=int(lis[3])

        mins=min(one,two,three)

        days-=mins
        one-=mins
        two-=mins
        three-=mins


        if one==0:
            days-=two//3
            days-=three//2
            if days<=0:
                print('Yes')
            else:
                print('No')
            continue
        if two==0:
            if three%2==0:
                days-=three//2
                days-=one//6

            else:
                days-=three//2
                days-=1
                one-=3
                days-=one//3
            if days <= 0:
                print('Yes')
            else:
                print('No')
                continue

        if three==0:
            if two%3==0:
                days-=two//3
                days-=one//6

            else:
                days-=two/3
                days-=1
                one-=(6-(two%3)*2)
                days-=one//6
            if days <=0:
                print('Yes')
            else:
                print('No')
                continue
        else:
            print('False')



if __name__ == '__main__':
    cal()





