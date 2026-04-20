class Container(object):
    """
    Container объект бол ямар ч төрлийн объект хадгалах боломжтой жагсаалт (list)
    """

    def __init__(self):
        """
        Хоосон жагсаалт үүсгэх
        """
        self.myList = []

    def size(self):
        """
        Жагсаалтын уртыг буцаах
        """
        # Your code here
        return len(self.myList)

    def add(self, elem):
        """
        Жагсаалтын нэг төгсгөлд элемент нэмнэ, байнга нэг талд нь л нэмэхийг анхаарна уу
        Юу ч буцаахгүй
        """
        # Your code here
        self.myList.append(elem)

    def __str__(self):
        """
        Container-н тэмдэгт мөр дүрслэл нь myList доторх элементийн утгууд байна
        """
        # your code here
        return str(self.myList)


class Stack(Container):
    """
    Container-н дэд класс. Элемент устгах нэмэлт функцтэй
    """

    def remove(self):
        """
        Жагсаалтад нэмэгдсэн хамгийн сүүлийн элементийг устгана
        Устгаж буй элементээ буцаана. Хоосон бол None утга буцаана.
        """
        # Your code here
        return self.myList.pop()


s = Stack()
print(s)

print(s.size())
s.add(3)
s.add(5)
s.add(7)
s.add(11)

print(s)
print(s.size())

print(s.remove())
print(s.remove())
print(s)
print(s.size())