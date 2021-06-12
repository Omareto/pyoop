from functools import wraps

def debugger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print(f'{fn.__qualname__}', args, kwargs)
        return fn(*args, **kwargs)
    return inner


@debugger
def func_1(*args, **kwargs):
    pass

@debugger
def func_2(*args, **kwargs):
    pass

# func_1(10, 20, kw='a')
# func_2(10)

class IntegerField:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print('__get__ called...')
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print('__set__ called...')
        if not isinstance(value, int):
            raise TypeError('Must be an integer')
        instance.__dict__[self.name] = value


class Point:
    x = IntegerField()
    y = IntegerField()

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
p.x, p.y
p.x = 10.5
