def xxxx(func):
    print('goyda')
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('2228')

    return wrapper
@xxxx
def fudsfdg():
    print('ya trahaus')