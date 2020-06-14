def call(f,*args,**kwargs):
    return f(*args,**kwargs)

def hello():
    print('hello')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def compute(a, b, op=add):
    return op(a,b)
print (call(compute,2,9))
