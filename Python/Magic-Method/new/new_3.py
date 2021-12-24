class Limited(object):
    instances = []
    limit = 5

    def __new__(cls, *args, **kwargs):
        if len(cls.instances) >= cls.limit:
            raise RuntimeError(f"instance exceed the limit({cls.limit})")
        this = super().__new__(cls)
        cls.instances.append(this)
        return this


class Something(Limited):
    pass


for _ in range(10):
    s = Something()
    print(s)
