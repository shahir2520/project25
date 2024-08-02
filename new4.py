thisdict ={
    'name':'shahir',
    'mob' : 7058197849,
    'city': 'vairag',
    'state':'maharastra',
    'lname':'Bansode',
    'adhar_no': 408044961565
}
print(thisdict)
x =thisdict['city']
print(x)
x=thisdict['name']
print(x)
x=thisdict.keys()
print(x)
q=thisdict.values()
print(q)
thisdict['name']='Shahir'

print(thisdict)
thisdict['city']='Vairag'
print(thisdict)
thisdict['state']='Maharastra'
print(thisdict)
y=thisdict['name']
print(y)
y=thisdict['city']
print(y)
y=thisdict['lname']
print(y)
y=thisdict['adhar_no']
print(y)
thisdict['city']='Solapur'
print(thisdict)
y=thisdict.keys()
print(y)
thisdict.update({'mob':9307815772})
print(thisdict)
car ={
    'name':'bmw',
    'year': 2024,
    'no':4080,
    'country': 'united state'
}
y=car.keys()
print(y)
y=car.values()
print(y)
car['year']=2025
print(car)
car.update({'country':'new york'})
print(car)
car.update({'city':'CA'})
print(car)
print(dir(car))
car.pop('city')
print(car)
print(car.get('age'))
print(car)
car.popitem()
print(car)
car.popitem()
print(car)
lis = [1,2,3,4,5,6,7,8]
print([i*i for i in lis])
print({i: i*i for i in lis})
even=({i for i in lis if i%2 ==0})#dictionary comprehension

print(even)

odd=[i for i in lis if i%2==1 ] #list comprehension
print(odd)

print({i.upper(): i*2 for i in 'shahir'} )

