"""
==Simple login logic==
Scenario: You’re building the backend logic for a login system without database using python


>>Create a program that:
>>Takes user input:

>correct username: admin
>correct password: python786
>user get 3 attempts
>on success: 'Login Successful'
>on failure: 'Attempts left: x'
>After failure: 'Account locked'


Use loops properly
"""

attempts=3
adminName='admin'
adminPassword='python786'
while attempts>0:
    username=input('Enter username: ')
    password=input('Enter password: ')
    
    if adminName!=username or adminPassword!=password:
        attempts-=1
        print(f"Wrong username, Try again, {attempts} attempts left")

        if attempts<=0:
            print('Account locked')
            break
        continue
    
    print('Login Successfull')
    break