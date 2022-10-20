def y():
    x = int(input("please input a number :"))
    for n in range(2,x-1):
        if (x % n) == 0:
            return False
    return(True if x>1 else False)
print(y())