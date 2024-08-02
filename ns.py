li=[]
num =int(input('enter any number'))
for i in range(1,num+1):
    element=int(input('enter exact number'))
    li.append(element)
print('original list is',li)
even=[]
odd=[]
for i in li:
    if i%2==0:
       even.append(i)
    else:
        odd.append(i)
print('even list is',even)
print('odd list is',odd)