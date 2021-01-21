class Fib(object):

    def __init__(self, num):
        L = [0,1]
        self.num = num
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        self.names = L
    def __str__(self):
        return str(self.names)
    def __len__(self):
        return self.num

f = Fib(10)
print (f)
print (len(f))
