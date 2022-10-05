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
array = []
array.append(object[1])
selectionSort(object, size)

predict_records = {
    object[0].number2: object[0]
}

for object7 in object:
    print(object7)
    predict_records.setdefault(object7.number2, object7.number1)
    x = predict_records.items()
    print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)


self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                0].clear_widgets(
                self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                    0].children)
            for child in self.children[0].children:
                if child.text != "TURN BACK":
                    child.disabled = True
                else:
                    child.disabled = False
            predict_records = {}

            for predict in self.predict_viewmodel.predicts:
                if predict.predict_limit not in predict_records:
                    predict_records[predict.predict_limit] = [predict.predict_count], [predict.predict_number]

self.parent.children[1].children[0].children[0].children[1].children[0].children[0].children[
                    0].add_widget(
                    HistoryViewBoxChildrenPreberHistoryPredictBox(predict_records[predict][1], predict_records[predict][0],
                                                                  predict))