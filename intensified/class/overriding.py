from intensified.Inheritance import FourCal


class SafeFourCal(FourCal):
    def divide(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.divide())