"""
Author: Karina Felippe

Assygnment:

Write a program to prompt the user for the following:

- First name
- Last name
- Email Address
- Phone Number
- Job Title
- ID Number

Then you should display the information back in this format:

Note that the square brackets [] indicate a value coming from the user and should not be displayed.

###
----------------------------------------
[LAST NAME], [first name]
[Job title]
ID: [id number]

[email address]
[phone number]
----------------------------------------
###

In addition to the spacing and punctuation shown above, you must implement the following requirements:

- The last name should be converted from whatever the user types to be displayed in ALL CAPS.
- The job title should be displayed so that the first letter is capitalized.
- The email address should be displayed in all lowercase.

An example of the program running is shown:

###
Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------
###

** CORE REQUIREMENTS **

You should work through the assignment in this order:
1. Prompt for all of the necessary values and store them in variables. Then display each item to the screen, without worrying about any spacing, punctuation, or formatting yet.
2. Arrange the display so that the spacing and punctuation exactly match the example shown.
3. Use the built-in string functions to make the last name display in all caps, the job title display in "title case," and the email display in all lowercase.


** STRETCH CHALLENGE **

The stretch challenges for this activity are:

1. Add hair color and eye color and put them both on the same line in the display.
2. Add a field for the name of the month they started and also a yes/no field for whether they have completed advanced training. Put these both on the same line in the display.
3. For the two lines that you just added, make it so that the second columns align, regardless of how many letters are in the responses. To complete this one, you may need to search the internet for something like, "python spacing format" or something similar to see if you get any ideas.

At the end of the stretch challenge, your output should look something like the following:

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234

Hair: Brown           Eyes: Blue
Month: September      Training: Yes
----------------------------------------


Similar with Sample Solution? Y
"""
'''
print('v0.1')
print('To create your Badge, please answer the questions:')
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
job_title = input('What is your job title? ')
id_number = input('What is your ID number? ')
email_address = input('What is your email address? ')
phone_number = input('What is your phone number? ')

print(f'{last_name.upper()}, {first_name.title()}')
print(job_title.title())
print(f'ID: {id_number}')
print(email_address)
print(phone_number)


print('v0.2')
print('To create your Badge, please answer the questions:')
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
job_title = input('What is your job title? ')
id_number = input('What is your ID number? ')
email_address = input('What is your email address? ')
phone_number = input('What is your phone number? ')

print(f'\n{last_name.upper()}, {first_name.title()}')
print(job_title.title())
print(f'ID: {id_number} \n')
print(email_address)
print(phone_number)



print('v1.2')
print('Please enter the following information:')
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')

print(f'\nInformation: {first_name}, {last_name}, {job_title}, {id_number}, {email_address}, {phone_number}\n')

print('The ID Card is:\n----------------------------------------')
print(f'{last_name.upper()}, {first_name.title()}')
print(job_title.title())
print(f'ID: {id_number} \n')
print(email_address.lower())
print(phone_number)
print('----------------------------------------')

'''

print('v2.1')
print('Please enter the following information:')
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
started_month = input('Starting month: ')
training = input('Have you completed the advanced training (yes/no): ')

print(f'\nInformation: {first_name}, {last_name}, {job_title}, {id_number}, {email_address}, {phone_number}, {hair_color}, {eye_color}, {started_month}, {training} \n')

print('The ID Card is:\n----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title.title())
print(f'ID: {id_number} \n')
print(email_address.lower())
print(phone_number)
print()
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {started_month:14} Training: {training}')
print('----------------------------------------')
