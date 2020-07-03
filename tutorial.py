##simple mathematical expression##
p = 5
w = 3
z = 7

a=200
b=300
#########

print(p+w-z)
print(a*b)

##variable overview##
age =90
name= 'John'

print(age)
print('My name is', name, 'and my age is', age) #comma notation

#type of variable using reserve keyword: type
print(type(age))
#########


##functions##
def add_two_numbers(x,y):
    total= x + y
    return total

output = add_two_numbers(220,65)
print(output)
#########

##lists##
people = ['George', 'Megan', 'Allison']

people.append('Watson')
name = people.pop()
print(name)
print(people)

people.remove('George')
print(people)

newPeople =('John', 'Jacob')

##conditional statements##
age= 25
if age <19:
    print('This person is a child')
elif age < 70:
    print('This person is an adult')
else:
    print('This person is a senior citizen')
