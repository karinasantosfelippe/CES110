'''
Author: Karina Felippe
Version: 2.0

Exceeding requirements: 
A question will be printed asking if you liked the story, if you reply with 'yes', 'y', 'ye', 'yep', or 'very much', the program will finish. Otherwise, the program will ask if you want to try input other informations.
'''




yes_choices = ['yes', 'y', 'ye', 'yep', 'very much']
adjective = ''
animal = ''
verb1 = ''
exclamation = ''
verb2 = ''
verb3 = ''
user_answer = ''

while True:
    print('Please enter the following:')

    adjective = input('Adjective: ')
    animal = input('Animal: ')
    verb1 = input('Verb: ')
    exclamation = input('Exclamation: ')
    verb2 = input('Verb: ')
    verb3 = input('Verb: ')

    print('\nYour story is:\n')
    print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.\n')
    user_answer = input('Did you like the story? (yes/no): ')

    if user_answer.lower() in yes_choices:
        print('\nHappy End!')
        break
    else:
        change_information = input('Do you want to try change the informations? (yes/no): ')

        if change_information.lower() in yes_choices:
            continue
        else:
            print('\nI will try be better next assignment!')