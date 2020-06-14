import time
def sleep(t=1):
    def decorateur(f):
        def wrapper(*args,**kwargs):
            time.sleep(t)
            m = f(*args,**kwargs)
            return m
        return wrapper
    return decorateur
    
@sleep(2)
def printnum (i):
    print (i)

cnt = 3
while cnt > 0:
    printnum ( cnt )
    cnt -= 1
print ('KA-BOOM !')