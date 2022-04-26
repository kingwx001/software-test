import sys


sys.stdout.buffer.write('测试123'.encode('utf8'))



if 1 == 2:
    def f(fn):
        print('haah')
        for i in range(4):
            ans = fn()
        return lambda : ans
    @f
    def t():
        print('ttt')

    t()

if 1 == 2:                     
    import functools    
    def log(unknown):    
        def decorator(fn):    
                @functools.wraps(fn)    
                def wrapper(*args, **kw):    
                    if isinstance(unknown, str):    
                        print('%s %s():' % (unknown, fn.__name__))    
                    else:    
                        print('%s():' % fn.__name__)    
                    return fn(*args, **kw)    
                return wrapper      
        if isinstance(unknown, str):    
            return decorator    
        else:    
            return decorator(unknown)    
    @log    
    def test(b):    
        print(b)    
        
        
    @log("execute")    
    def test1(b):    
        print(b) 

    test('test')
    test1('test1')

    
    