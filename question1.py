num = 1000000

def huiwen(num):
    if num:
        numstr = str(num)
        for i in range(int(len(numstr)/2)):
            # print(numstr[i],i,numstr[-i-1])
            if numstr[i] is not numstr[-i-1]:
                return False
            else:
                pass
        return True
    else:
        return False

def main(num):

    print('num is ',num)
    for n in range(num):
        if huiwen(n) and huiwen(n**2) and huiwen(n**3):
            print(n)
        else:
            #print('not find')
            pass


if __name__ == '__main__':
    main(num)
