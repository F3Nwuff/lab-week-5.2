x, y = eval(input("please input the price and payment :"))
def l():
    bills = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    k = []
    p = 0
    r = y - x
    print(r)
    if r < 100 :
        return("no change")
    while True:
        if p == 10 :
            break
        if r >= bills[p] :
            k.append(bills[p])
            r -= bills[p]
        if r < bills[p] :
            p += 1
    return k
print(l())