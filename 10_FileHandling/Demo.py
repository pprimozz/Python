f = open("/home/pprimozz/Desktop/test.js",'r')

print(f.read())

#print(f.readline())

#print(f.readline(4),end='')

f1 = open("/home/pprimozz/Desktop/abc",'w')
f1.write("something")

f2 = open("/home/pprimozz/Desktop/abc",'a')   # append

f2.write("something")


for data in f:
    f2.write(data)