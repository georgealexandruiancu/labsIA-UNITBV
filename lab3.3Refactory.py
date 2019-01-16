def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1


def retea(o1, o2, o3):
    while(o1 != 1 or o2 !=1 or o3 != 1):
        o1Old = o1
        o2Old = o2
        o3Old = o3
        o1 = sgn(o2 - o3)
        o2 = sgn(o1 - o3)
        o3 = sgn(-o1 - o2)

        print(o1, o2, o3)
        if o1 == o1Old and o2 == o2Old and o3 == o3Old:
            return

retea(7, 8, 9)
