class FourCal:
    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second

    def setdata(self, first, second): #self에 메서드를 호출한 객체가 전달됨
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def multiply(self):
        result = self.first * self.second
        return result

    def divide(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
b = FourCal(3,8)

print(a.first)

print(a.add())
print(a.multiply())
print(a.sub())
print(a.divide())
print(b.add())
print(b.multiply())
print(b.sub())
print(b.divide())



