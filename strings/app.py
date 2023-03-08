print('Sumit\'s \nBook')

#raw string

print(r'Sumit\'s \nbook')


#multiline strings

print('''This is a line ''',''
      
      'This is second line''')

''''This is a multiline
comment
'''

#indexing

print("Sumit"[0])

#negative index

print("sumit"[-2])

#slicing

print("Sumit"[0:3:2])

#in operator

print("S" in "Sumit")

# not in 

print("S" not in "Sumit")

#formatting string

print("My name is %s and my age is %s "%("Sumit",25))

name = "Sumit"
age = 25

print(f'My name is {name} and my age is {age}')

# string methods

print("SUMIT".lower())
print("sumit".upper())
print("sumit".capitalize())
print("sumit".index("s"))
print('sumit'.find('s'))
print('sumit Kumar'.center(3))
phone = "A"

print(phone.isdigit())
print(phone.isascii())

#join and split

location = "123333.111,11111.1115"

print(location.split(","))


print('-'.join(['1','2']))

print("Sumit".partition("u"))

#justify

print('Sumit'.rjust(30))

print('         Sumit'.ljust(30))

print('Sumit'.center(30))

print('       SS      U     M    I   T'.lstrip())

print('       SS      U     M    I   T     '.rstrip())

print('       SS      U     M    I   T     '.strip())

#ord and char

print(chr(65))

print(ord('('))


name = ("ansh",(len))
print(len)


