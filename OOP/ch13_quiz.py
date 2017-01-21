class A(object):
    
    def __init__(self):
        self.num = 3
        self.string = "Hello from A!"

    def __str__(self):
        return self.string*self.num

class B(A):

    def __init__(self):
        super(B, self).__init__()
        self.string = "Hello from B!"


class C(A):

    def __init__(self):
        super(C, self).__init__()

    def __str__(self):
        return self.string
