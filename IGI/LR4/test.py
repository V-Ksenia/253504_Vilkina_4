class B:
    def getA(self, n):
        self.arg = n
        return self.arg
    
b = B()
B.a = 1
print(b.a)
print(B.a)

