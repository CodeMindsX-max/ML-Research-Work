"""
==User Registration Validator==
Scenario: You’re building the backend logic for a signup system using python


>>Create a program that:
>>Takes user input:

>username
>password
>age

>>Validates:

>Username must be at least 5 characters
>Password must be: at least 8 characters
>contain at least one digit
>Age must be: a number >= 18

If any rule fails, show a clear error message

If everything is valid, print:
"User registered successfully"
"""
def validateUsername(name):
    return len(name)>=5 and not any(char.isspace() for char in name)

def validatePassword(password):
    return len(password)>=8 and any(char.isdigit() for char in password)

# optional function for validation strong password
def checkStrongPassword(password):
    if (len(password)>=8 and
        any(char.isdigit() for char in password) and
        any(char.islower() for char in password) and
        any(char.isupper() for char in password)
    ):
        print('Password is Strong')
    else: 
        print('Password is week')
while True:
    username=input("Enter your username at least 5 characters: ")
    password=input("Enter your password at least 8 characters and 1 digit: ")
    age=input("Enter your age: ")
    if not age.isdigit():
        print('Age must be number')
        continue
    intage=int(age)

    if not validateUsername(username):
        print("Wrong username, must be at least 5 characters")
        continue
    if not validatePassword(password):
        print("Wrong password, must be at least 8 characters and 1 digit")
        continue
    if not age>=18:
        print("You are not mature enough for account registration")
        continue
    if checkStrongPassword(password):
        print('Good you are intellegent you have a strong password')
    print("User registered successfully")
    break







