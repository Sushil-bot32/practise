"""# using any/all function
print(any([True, True, False, True]))
print(all([True, True, True, True, True]))

# practical examples.
list1 = []
list2 = []
for i in range(1, 11):
    list1.append(4*i)

for i in range(0,10):
    list2.append(list1[i]%5 == 0)
print(" The list of item which is divisible by 5")
print(any(list2))

# using all operator in 
list1 = []
list2 = []

for i in range(1, 13):
    list1.append(4*i)

for i in range(0,10):
    list2.append(list1[i]%2 == 0)
print(" The list of item which is divisible by 2")
print(all(list2))

# some predefined function

import operator
a = 10
b = 2

print(operator.add(a, b))  # adding two values
print(operator.sub(a, b))  # subtracting between two values
print(operator.mul(a, b))   # multiply two values
print(operator.truediv(a,b))    # dtuely division
print(operator.lt(a, b))
print(operator.eq(a, b))
print(operator.floordiv(a,b))
print(operator.mod(a,b))
print(operator.pow(a, b))

# using predefined function in  control statement
if operator.gt(a,b):
    print("a is greater than b")
else:
    print("b is greater than a")


if operator.eq(a,b):
    print("both are equal")

print("no element present the parameter")

# using set get and elete function 
import operator
li1 = [4,6,8,10,12]
print("This is the function to set in the list")
for i  in range(0,len(li1)):
    print(li1[i], end = " ")
print("\r")
operator.setitem(li1,3,9)    # setting the values li1
print(li1)
operator.delitem(li1, 2)   # element after deletion 
print(li1)
print(operator.getitem(li1, 1))
operator.setitem(li1, slice(1,4),[44,55,66])
print(li1)

# Difference between == and is operator. (in list)
li1 = []
li2 = []
li3 = li1

if li1 == li2:
    print("True")
else: print("False")

if li1 is li2:
    print("True")
else: print("False")

if li1 == li3:
    print("True")
else: print("False")
li3 = li1 + li2

if li1 is li3:
    print("True")
else: print("False")

li1 = []
li2 = []

print(id(li1))
print(id(li2))

# it shows two list having different object.

# Python membership and identity operator helps to find the common member in list

# suppose
li1 = [2,4,6,8,10]
li2 = [1,3,5,7,9]
for item in li1:
    if item in li2:
        print("the sets are overlapping")
    else:print("The sets are not overlapping")

# finding a common element in two list using function
def overlapping(li1,li2):
    c = 0
    d = 0
    for i in li1:
        c += 1
    for i in li2:
        d+=1
    for i in range(0,c):
        for j in range(0,d):

            if li1[i] == li2[j]:
                return 1
    return 0
li1 =[2,3,5,7,9,12]
li2 = [2,4,6,8,10,12]
if(overlapping(li1,li2)):
    print("they are ovelapping")
else:print("They are not overlapping")

# example of default argument

def fun1(x, y = 20):
    print("x:",x)
    print("y:", y)
fun1(10)
fun1(30)

# keyWord argument

def fun2(firstName, lastName):
    print(firstName,lastName)

fun2(firstName='sushil',lastName='singh')
fun2(firstName='surabhi',lastName='BN')

# variable length non keyword argument

def fun1(*argv):
    for i in argv:
        print(i)
fun1('my','name is','sushil singh')

# variable length keyword argumentt.
def fun2(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" %(key,value))
fun2(first='sushil',mid='kumar',last='singh')

# using a  return keyword in function

def fun2(num1,num2):
    return num1+num2
print(fun2(2,3))
print(fun2(5,6))

i=2
for i in range(i<2):
    i =i+3
print(i)

x = [(3,2),(2,3)]
x.sort()
print(x)

def fun1(x):
    x[0] =10
    x[2] = 20
x = [1,2,3,4,5]
fun1(x)
print(x)

def myfun( fName,*argv):
    print("my first name is:",fName)
    for arg in argv:
        print("The next name is",arg)
myfun('sushil','hello','world')

def fun1(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s"%(key,value))
fun1(first='sushil',mid='kumar',last='singh')

def fun1(arg1,arg2,arg3):
    print("args:",arg1)
    print("args:",arg2)
    print("args:",arg3)
args =['sushil','kumar','singh']
fun1(*args)

args1 = {'first':'sushil','mid':'kumar','last':'singh'}

# using yield keyword
def mygeneratorfun():
    yield 1
    yield 2
    yield 3
for i in mygeneratorfun():
    print(i)

print("#############################")

def generator1():
    i =1
    while True:
        yield i*i
        i+=1
for num in generator1():
    if num>100:
        break
    print(num)

x =    min("hello World")  # o/p: blankspace.
print(x)

# using generator function.

def fun1():
    yield 1
    yield 2
    yield 3
for value in fun1():
    print(value)
print(" ")
# using generator object and printing multiple values using next keyword.
def fun2():     
    yield 1
    yield 2
    yield 3

x = fun2()
print(x.__next__())     # for python3.0 and above use __next__() method
print(x.__next__())
print(x.__next__())
# creating fibonnaci series using generator object
def fib(limit):
    a, b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b
y = fib(10)
print(y.__next__())
print(y.__next__())
print(y.__next__())
print("\n using for loop to find all fibonnaci series:")
for i in fib(10):
    print(i)

# Using lambda function
x = "sushil singh"
print(lambda x: x)

# using global and local variabl
def fun1():
    s = "my name is khan"
    print(s)
s ="sushi"
fun1()
print(s)

def fun1():
    global a
    a += "GFG"
    print(a)
a ="pthon is great!"
fun1()"""









    


 
















