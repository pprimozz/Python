import math

input_string = input()
list  = input_string.split()

input_string1 = input()
list1  = input_string1.split()


N=int(list[0])
Q=int(list[1])


aElements=[]

for i in list1:
    aElements.append(int(i))

Qa=[]
Qb=[]



for x in range(Q):
    input_str = input()
    list = input_str.split()
    Qa.append(int(list[0]))
    Qb.append(int(list[1]))


l=0
r=0
result=0
counter=0

for z in range(Q):
    l=Qa[z]
    r=Qb[z]
    result=0
    counter=0
    for u in range(l-1,r,1):
        result=result+aElements[u]
        counter=counter+1
    res=(result/counter)
    print(math.floor(res))
