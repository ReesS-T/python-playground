#1. reads name.txt into a variable my_name
with open('name.txt') as n:
    my_name = n.read()

#2. writes a new file named hello.txt
	#with the contents
	#Hello, my name is <my_name>
with open('hello.txt', 'w') as m:
    m.write('Hello, my name is '+my_name)
    m.write('\n')
