class Object:
    def __init__(self, name, number1, number2):
        self.name = name
        self.number1 = number1
        self.number2 = number2



object1 = Object("chair", 3, 2)
object2 = Object("table", 1, 2)
object3 = Object("pencil", 4, 4)
object4 = Object("book", 5, 7)
object5 = Object("notebook", 4, 2)

def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j].number2 < array[min_index].number2:
                min_index = j

            elif array[j].number2 == array[min_index].number2:
                if array[j].number1 < array[min_index].number1:
                    min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])

object = [object1, object2, object3, object4, object5]
size = len(object)
selectionSort(object, size)
print(object[0].number1)
print(object[0].number2)
print(object[1].number1)
print(object[1].number2)
print(object[2].number1)
print(object[2].number2)
print(object[3].number1)
print(object[3].number2)
print(object[4].number1)
print(object[4].number2)

