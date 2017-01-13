class Buffer:
    def __init__(self):
        self.List = []

    def add(self, *a):
        self.List.extend(a)
        while len(self.List) // 5 > 0:
            Sum = sum(self.List[:5])
            self.List = self.List[5:]
            print(Sum)

    def get_current_part(self):
       # print(self.List)
        return self.List

def proba():
    buf = Buffer()
    buf.add(1, 2, 3)
    assert buf.get_current_part() == [1, 2, 3] # вернуть [1, 2, 3]
    buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
    assert buf.get_current_part() == [6] # вернуть [6]
    buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
    assert buf.get_current_part() == [] # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    assert buf.get_current_part() == [1] # вернуть [1]

###ПОЧЕМУ ТО НЕ проходит
if __name__ == "__main__":
    proba()