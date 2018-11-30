class Dog(object):
    """ gou"""

    def __init__(self, head, leg, age):
        self.age = age
        self.head = head
        self.leg = leg

    def setage(self, asa):
        self.age = asa + 1

    def countage(self, con):
        self.leg += con

    def printll(self):
        print(self.head + "-" + str(self.leg) + " -" + str(self.age))


def run():
    dog = Dog('a', 1, 1)
    dog.setage(10)
    dog.countage(2)
    dog.printll()


if __name__ == '__main__':
    run()
