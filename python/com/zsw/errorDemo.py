import logging
logging.basicConfig(level=logging.INFO)

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    # if n==0:
    #     raise FooError('invalid value: %s' % s)
    return 10 / n


f = foo('1')

logging.info('n = %d' % f)