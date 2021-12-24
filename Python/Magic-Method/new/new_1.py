class Sample(object):

    def __new__(cls, *args, **kwargs):
        print('new', args, kwargs)
        this = super().__new__(cls)
        cls.args = args
        cls.kwargs = kwargs
        return this

    def __init__(self, *args, **kwargs):
        print('init', args, kwargs)

    def show(self):
        print('show', self.args, self.kwargs)


sample = Sample(123, key = 'abc')
sample.show()
print(sample)
