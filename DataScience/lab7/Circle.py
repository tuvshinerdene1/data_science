class Circle:
    def __init__(self, radius):
        """self-г радиустай үүсгэх"""
        # your code here
        self.radius = radius

    def get_radius(self):
        """self-н радиусыг буцаах"""
        # your code here
        return self.radius

    def set_radius(self, radius):
        """радиус бол тоо
        self-н радиусыг орж ирж буй радиусын утгаар солих"""
        # your code here
        self.radius = radius

    def get_area(self):
        """self-н талбайг pi = 3.14 үед тооцож буцаах"""
        # your code here
        return self.radius ** 2 * 3.14

    def equal(self, c):
        """c бол Circle-н объект
        Хэрэв self болон c нь ижил радиустай бол True буцаа"""
        # your code here
        return c.radius == self.radius

    def bigger(self, c):
        """c бол Circle-н объект
        Circle объект буцаах бөгөөд self эсвэл c-н аль том радиустайг нь буцаана"""
        # your code here
        if self.radius > c.radius:
            return self
        return c

    def __add__(self, c):
        """c бол Circle-н объект
        Шинэ Circle-н объект үүсгэж буцаана. Түүний радиус нь self болон c-н радиусын нийлбэр байна"""
        # your code here
        return Circle(self.radius + c.radius)

    def __str__(self):
        """Circle-н тэмдэгт мөр дүрслэл бол түүний радиус байна"""
        # your code here
        return str(self.radius)


c1 = Circle(4)
print("r =", c1.get_radius())
c1.set_radius(5)
print("area =", c1.get_area())

c2 = Circle(3)
c3 = Circle(5)
print(c1, c2, c3)

print("c1.equal(c2) ?", c1.equal(c2))
print("c1.equal(c3) ?", c1.equal(c3))

print("c1.bigger(c3) ?", c1.bigger(c3))
print("c2.bigger(c1) ?", c2.bigger(c1))

print("c1 == c2 ?", c1 == c2)
print("c1 == c3 ?", c1 == c3)

print(c1 + c2)