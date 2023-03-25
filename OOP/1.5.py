class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        if isinstance((self.a, self.b, self.c), (int, float)):
            return 1
        elif (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return 2
        elif (self.a + self.b > self.c) or (self.a + self.c > self.b) or (self.b + self.c > self.a):
            return 3


a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())