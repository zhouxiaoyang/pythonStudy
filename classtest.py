def foreach(a: dict):
    for key, values in a.items():
        if isinstance(key, int):
            print(str(key) + " =" + str(values))


def run():
    objectclass = {
        1: 1,
        2: 2,
        3: 3
    }
    if objectclass:
        foreach(objectclass)
    # sb = [1, 2]
    # foreach(sb)


if __name__ == '__main__':
    run()
