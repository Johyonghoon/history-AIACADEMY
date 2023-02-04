class AdvancedList(list):
    def replace(self, one, hund):
        while one in self:
            self[self.index(one)] = hund


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)