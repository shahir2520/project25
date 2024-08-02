li=[]
num=int(input('enter any number'))
for i in range(1,num+1):
    element=int(input('enter any number'))
    li.append(element)
print('original list is',li)
even_li=[]
odd_li =[]
for i in li:
    if i%2==0:
        even_li.append(i)
    else:
        odd_li.append(i)
print('even number is',even_li)
print('odd number is ',odd_li)

