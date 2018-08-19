import sys

#1 1 2 2 2 1 1 2 2 0

def main():
    a=sys.stdin.readline()
    alist=a.strip().split(' ')
    number=0
    con=2
    for each in alist:
        if each=='1':
            number+=1
            con=2
        elif each=='2':
            number+=con
            con+=2
        elif each=='0':
            print(number)
            break



if __name__ == '__main__':
    main()