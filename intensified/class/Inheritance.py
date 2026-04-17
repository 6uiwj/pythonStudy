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




class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.pow())