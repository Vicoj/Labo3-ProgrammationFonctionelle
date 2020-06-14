import math
def binrep(n):
    while n<0:
        bit = n%2
        n//=2
        yield bit


b = binrep(12)
while True :
    try :
        print (next(b))
    except StopIteration :
        break