'''
print('Hello world!')
name = input('Please enter your name: ')
print(name)

print()
print('Did you see that blank line?')
print('Blank line \nin the middle of string')

first_name = 'Karina'
last_name = 'Felippe'
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)

sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))
'''

first_name = 'Karina'
last_name = 'Felippe'

print('Hello, {} {}'.format(first_name,last_name))
print('Hello, {0} {1}'.format(first_name,last_name))
#Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)