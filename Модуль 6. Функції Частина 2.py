import random
# task 1
def sum_of_list(x):
    print(sum(x))
a=[]
for i in range(random.randint(1,10)):
    a.append(random.randint(1,30))
sum_of_list(a)
# task 2
def min_of_list(x):
    print(min(x))
a=[]
for i in range(random.randint(1,10)):
    a.append(random.randint(1,30))
min_of_list(a)
# task 3
simple_numbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# ))))))) я незнаю як їх визначити в циклі порівнянням 
def simple(x):
    a=0
    for i in x:
        if i in simple_numbers:
            a+=1
    print(a)
a=[]
for i in range(random.randint(1,20)):
    a.append(random.randint(1,100))
simple(a)
# task 4
def how_many_delete(x):
    global a
    b=len(a)
    l=0
    n=int(input("Введіть число яке бажаєте видалити    : "))
    for i in a:
        if i==n:
            a.remove(i)
            l+=1
    print(b-(len(a)))
    print(a)
a=[]
for i in range(random.randint(1,10)):
    a.append(random.randint(1,30))
print(a)
how_many_delete(a)
# task 5
def list1_list2(a,b):
    print(a+b)
a=[]
for i in range(random.randint(1,10)):
    a.append(random.randint(1,30))
b=[]
for i in range(random.randint(1,10)):
    b.append(random.randint(1,30))
list1_list2(a,b)
# task 6
def list_in_square(a):
    x=[]
    for i in a:
        x.append(i**2)
    print(x)
a=[]
for i in range(10):
    a.append(random.randint(1,15))
print(a)
list_in_square(a)