def one(a, b):
    count = 0
    for i in range(1, 20):
        count += a + b
    return count


def fun(x=[]):
    lists = x[:]
    lists.append(23)
    return lists


def fun1(x: list):
    a = list()
    s = x[:]
    s.append()


def ifTest(x, y):
    if x == y and x == 1:
        return True


def innotin(x: str, y: list):
    if x in y or x == "1":
        return True
    else:
        return False


def main():
    ints = []

    result = one(1, 10)
    li = [value ** 3 for value in range(1, 10)]
    ls = fun(li)
    for i in li:
        print(i)
    # len(ls)
    for s in range(0, ls.__len__()):
        print("--" + str(ls[s]))
    print(ls)
    print(li)
    print(li[0:3])
    print(li[-3:])
    ints.append(1)
    ints.append(2)
    print(ints)
    print(result)
    if ifTest(2, 2):
        print("is true!! body")
    else:
        print("is not true !")
    # alist = ["1", "2"]
    alist = [str(a ** 2) for a in range(1, 10)]
    print(alist)
    if innotin("1", alist):
        print("in list!!")


if __name__ == '__main__':
    main()
