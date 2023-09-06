Person1 = input('Enter your name if you are person 1 : ')
Person2 = input('Enter your name if you are person 2 : ')
by1 = int(input(f'Enter the birth year of {Person1} : '))
by2 = int(input(f'Enter the birth year of {Person2} : '))
result = by1-by2

print(f'The age defference between {Person1} & {Person2} is {result} years')
print('The age difference between {} & {} is {} years').format(Person1,Person2,result)
a = 1
b = 'Hello World'
c = 1.234
d = [1,2,3,4,5]
e = (1,2,3,4,5)
f = {1:1,2:2}
a = 2
if(a == 2):
    print('This is a integer value')
elif(isinstance(b,int)):
    print('This is a String value')
elif(isinstance(c,float)):
    print('This is a float value')
elif (isinstance(d, list)):
    print('This is a List value')
elif(isinstance(e,str)):
    print('This is a tuple value')
elif(isinstance(f,dict)):
    print('This is a Dictionary value')
else:
    print('There is another value')

#operators
result = 1+2 #addition
result = 1-2 #substraction
result = 10/3 #divide
result = 2*3 #multiply
result = 2**2 #power

Fruitlist = ['apple','mango','bnanna']

for i in Fruitlist:
    print(i)

value = 'Hello World' + 'python' #concatenation
print(value[10]) #indexing
print(value[0:6])  #slicing
value = 1
list(value)
print(type(str(value)))
print(value)
print(Fruitlist[2])
print(type(a))
print(isinstance(a,dict))
print(a)
list = [1,2,3,4,5,6]
print(sum(list))
