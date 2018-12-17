Python
Exercises
(Nicholas Austin)

The code must be submitted under your name in GitHub in a repository called Python. Work individually.
Create one file with all your work and name it: cs361python.py or cs 631python.py.
Do not commit code that does not compile. The code that you commit should have been tested. -10 points for each exercise for code that does not compile on the top of your grade. 
You will provide a hardcopy with your code to Dr. Scharff on 12/17.

Exercise 1
 

A) 
print (5/3) 
The code outputs an integer 1.66666666 to be exact.

B)print (5%3)  
The code output the number 2. Because of the modulus symbol, which returns the remainders

C)
Print (5.0/3)
The code returns 1.6666666 just like the number in (A)
D)
print (5/3.0) 
 The Code returns the same thing that (A) and (B) returns which is 1.66666666
E)
 print (5.2%3) 
The code returns 2.2 because that is what is remaining. % symbol returns the remaining numbers


Exercise 2
 
A)	print (2000.3 ** 200) 
	a.	The following code returns “out of range”
B)	print (1.0 + 1.0 - 1.0) 
	a.	The following code returns 1.0. It follows the order of operations
C)	print (1.0 + 1.0e20 - 1.0e20) 
	a.	The following code returns 0.0.









Exercise 3
 
(A) float (123)
	 Float (123) returns 123.0. A float with a decimal
(B) float ('123')
	 The code returns 123.0.  The quotations mean that it is put into a string.  
(C) float('123.23')
	 Again the code returns 123.23, the quotations puts it into a string.
(D) int (123.23')
	The following code returns 123. The decimal was dropped
(E) int ('123.23')
	The following code doesn’t compile because it is inputted as a float but then tries to convert to an int but there is an invalid literal.
(F) int (float('123.23'))
	 The following code returns 123. It gets inputted as a string then converted to float then and integer.
(G)str(12)
	The following code returns ‘12’.  12 gets inputted as integer first then a string is return.
(H) str(12)
	 The following code returns ’12.2’. The same as question “G” but with 12.2
(I) str(12.2)
	The following code returns true.  The code inputs a as a string and returns true, which is the bool.
(J) bool(0)
	The following code returns false, int puts 0 as an integer and returns false which is the bool.
(K) bool(0,1)
	 The code returns true. It inputs 1.0 as a float then returns the bool true. 



Exercise 4

range(5) 


for i in range(5):
    print(i)
 
4) It returns (0, 5). So for I in range (5) means so, (0, 4). (range(5)). It also returns class “range”.





Exercise 5
 
5)
	numberFound = 0 
	n = 11
	while numberFound < 20:
	if n % 2 == 0 and n % 7 == 0 and x % 11 == 0:
	print (n)
	numberFound = numberFound + 1
	n = n + 1




Exercise 6






 

Exercise 7

#A
 
lst = [1,2,3,4,5,6,7,8]

def write_list(lst):
    for item in lst:
        print (item) 



write_list(lst)

#B

lst = [1,2,3,4,5,6,7,8]

def write_list(lst):
  return lst[::-1]

write_list(lst)

#C

lst = [1,2,3,4,5,6,7,8]

def Len(Lst):
    size = 0
    for item in Lst:
        size = size + 1
    return size

Len(lst)

#Exercise 8

a = [1,2,3,4,5,6,7,8]

b=a
b[0] = 9
print (a[0])
#so when i changed b1 to 9, a1 was also changed to 9

c= a[:]

c[1]=14
print (a[1])
#when i changed c 2 to 14 list 'a' was not changed at all

def setfirstelemtozero(l):
    l[0] = 0
    return l

setfirstelemtozero(a)
print_list(a)

 
 
#Exercise 9

lst = [[1,3],[3,6]]
def sublist(l):
    sublist_lst = []
    for vector in l:
        for element in vector:
            sublist_lst.append(element)
    return sublist_lst
    

aselements = sublist(lst)
print(aselements)
  
#Exercise 10
Use mathplotlib

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0, 2.0, 0.01)
b = (np.sin(a - 2) **2) * np.exp(-a **2)

fig, ax = plt.subplots()
ax.plot(a, b)

ax.set(xlabel='x', ylabel='y', title='cs361')
fig.savefig("test.png")
plt.show()


#Exercise 11
def iteration_retur(lst):
    if len(lst) == 0:
        return 0
    a = 1
    for item in lst:
        result = a * item
    return result


def recursion_retur(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        return recursion_retur([lst[0]]) * recursion_retur(lst[1:])


lst = [1,2,3,4,5,6,7,8]
empty = []
iteration_retur(lst)
recursion_retur(lst)
iteration_retur(empty)
recursion_retur(empty)

#Exercise 12

def fib(x):
    if(x==0):
        return 0
    elif(x==1):
        return 1
    else:
        return fib(x-1)+fib(x-2)
print(fib(20))

 
Exercise 13
Write a Python program that extracts the email addresses of a file. An email file emails.txt is provided to test your program.
http://rubular.com/ is a site that can be useful to get familiar with regular expressions. 
import re

file = open('emails.txt','r')
file = file.read()

addresses = re.findall(r'([^ ]+[@][^ ]+[.][a-z]+)', file)
print(addresses)




References
Stanford courses on Python https://web.stanford.edu/~schmit/cme193/exercises.html 
