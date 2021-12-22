class Sample(object):

    def __new__(cls, *args, **kwargs):
        this = super().__new__(cls)
        cls.number = 7
        return this

    def __init__(self, *args, **kwargs):
        pass

    def show(self):
        print(self, self.number)


for i in range(5):
    sample = Sample()
    sample.show()
