# Написать класс Parallelogram, который имеет 2 аргумента width и length(ширина и длина) и метод get_area,
# который возвращает площадь параллелограма с такими сторонами. Унаследовать от него класс Square,
# переопределить метод get_area как произведение ширины на ширину(или длины на длину).

class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._lenght = length

    def get_area(self):
        print(self._width * self._lenght)


#p = Parallelogram(2,3)
#p.get_area()

class Square(Parallelogram):
    def get_area(self):
        print(self._width * self._width)


s = Square(2,4)
s.get_area()

# Написать функцию, котрая принимает 2 параметра data и new_value. Если data это список или множество,
# то добавить в него элемент new_value, если строка, то сконкатенировать (за исключением, если new_value
# не список, иначе вернуть не измененную data), а если это число, логическое значение или словарь, то вернуть
# не измененную data

def function(data, new_value):
    if isinstance(data,list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data

print(function('{1,5,3}', '{4}'))
# пример перегрузки

