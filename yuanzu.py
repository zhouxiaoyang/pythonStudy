from study import one as ones


def yuanzu(*paramter):
    if paramter:
        print(paramter)


def shican(a, **shiti):
    print(a)
    print(shiti)


yuanzu(1, 1, 1, 1, 1)
shican('aa', s='1', ls='2')
result = ones(1, 9)
print(result)
