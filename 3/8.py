oneCh, twoCH, threeCH = int(input()),int(input()),int(input())

if oneCh == twoCH == threeCH:
    print(3)
elif oneCh == twoCH or twoCH == threeCH or oneCh == threeCH:
    print(2)
else:
    print(0)