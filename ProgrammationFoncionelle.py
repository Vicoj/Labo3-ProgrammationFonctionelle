##Exemple Lambda
bytwo = lambda n : n*2
#print(bytwo(2)) 

##Exemple Fonction map
data = [1,2,3]
result = map(lambda x : x**2,data)
#print (list(result))

##Example Fonction filter
data = [1,-2,0,7,-3]
result = filter(lambda x : x>=0,data)
#print (list(result))

##Example Fonction filter
data = [2+1j,-1j,4]
#print (sum(data))

#Example Fonction reduce
from functools import reduce
L = [1,2,3,4]
#print (reduce(lambda S, elem : S+elem,L,0))

#Exemple Fonction All Any 
data = [2,-6,0,8]
test = lambda e : e%2 == 0 and e>= 0
filtered = [test(e) for e in data]
#print (all(filtered))
#print (any(filtered))

#Type callable

class Empty :
    pass
def create ():
    return Empty ()
#print (callable(Empty)) # True
#print (callable(create)) # True
#print (callable(callable)) # True

#Instances callables
import random
class Die :
    def __init__ (self):
        self.roll()

    @property
    def value (self):
        return self.__value

    def roll (self):
        self.__value=random.randint(1,6)

    def __call__(self):
        self.roll()
        return self.value

#die = Die()
#print (die.value)
#print (die())

#Closure

def make_adder (n):
    def adder (value):
        return value+n
    return adder

#adder2 = make_adder(2)
#adder7 = make_adder(7)
#print (adder2(12))
#print (adder7(9))

#Calcul incrémental d'une moyenne (1)
def make_averager ():
    data = []
    def averager (value):
        data.append(value)
        return sum(data)/len(data)
    return averager

avg = make_averager ()
#print ( avg(100))
#print ( avg(7))
#print ( avg(6))

#Calcul incrémental d'une moyenne (2)

def make_averager ():
    total = 0
    count = 0
    def averager ( value ):
        nonlocal total , count
        total += value
        count += 1
        return total / count
    return averager

avg = make_averager ()
#print ( avg (5))
#print ( avg (100))
#print ( avg (6) )

##DECORATE

#Ajouter un comportement à une fonction

def decorate (f):
    def wrapper ():
        print ('Avant appel ')
        f()
        print ('Après appel ')
    return wrapper

def sayhello ():
    print ('Hello !')

 #g =decorate(sayhello)
 #g()

 #decoration

def decorate (f):
    def wrapper ():
        print ('Avant appel')
        f()
        print ('Après appel ')
    return wrapper

@decorate
def sayhello ():
    print ('Hello !')
#sayhello ()

#Chronométrer le temps d'exécution
import time

def timeit (f):
    def wrapper (*args ):
        t1 = time.time()
        result = f(*args)
        print ('Executed in {:.2f} s'.format(time.time()-t1))
        return result
    return wrapper

#Paramètre de décorateur (1)
def checktypes (* types ):
    def decorator (f):
        def wrapper (* args ):
            return f(* args )
        return wrapper
    return decorator

@checktypes (int)
def compute (n):
    return n**2
#print (compute(8))

#Paramètre de décorateur (2)
def checktypes (*types):
    def decorator (f):
        def wrapper (* args ):
            return f(* args )
        return wrapper
    return decorator

def compute (n):
    return n ** 2

f1 = checktypes(int)
f2 = f1(compute)
#print (f2(9))

#Vérification des types
def checktypes (* types ):
    def decorator (f):
        def wrapper (* args ):
            assert len ( types ) == len ( args ), 'wrong number of types '
            for (a, t) in zip (args , types ):
                assert isinstance (a, t), 'arg {} does not match {} '.format (a, t)
            return f(* args )
        return wrapper
    return decorator

##GENERATEUR
#Définition d'un itérateur (1)
import re

RE_WORDS = re.compile ('\w+')

class Sentence :
    def __init__ (self , text ):
        self . __text = text
        self . __words = RE_WORDS . findall ( text )
    def __getitem__ (self , i):
        return self . __words [i]
    def __len__ ( self ):
        return len ( self . __words )

#Définition d'un itérateur (2)
s = Sentence (" Bonjour , c'est moi .")
print ( list (s))
for word in s:
print ( word )
