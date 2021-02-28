class MyIterator:
    obj = None

    def __iter__(self):
        return self

    def __init__(self, o):
        global obj
        obj = o
        self.limit = len(o)
        self.counter = 0

    def __next__(self):
        global obj
        if self.counter < self.limit:
            self.counter += 1
            return obj[self.counter - 1]
        else:
            raise StopIteration


def printList(inputList):
    return inputList


def buildNewListDecorator(decoratedFunction):

    def buildNewList(inputList):
        list.reverse(inputList)
        myIter = MyIterator(inputList)

        newList = []
        for i in myIter:
            if (inputList.count(i) / 2 == 1.0) and (newList.count(i) == 0):
                newList.append(i)
        return newList
    return buildNewList(decoratedFunction)

if __name__ == '__main__':
    inputList = [1, 2, 3, 1, 2, 3, 9, 9]
    print(printList(inputList))
    print(buildNewListDecorator(printList(inputList)))
