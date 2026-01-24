"""
==Daily Expense Checker==
Scenario: You’re building the backend logic for a personal finance app using python


>>Create a program that:
>>Takes user input:

>daily budget
>amount spent today

>>Validates:

>if spent > budget -> 'Over Budget'
>if spent == budget -> 'Budget exactly used'
>if spent < budget: show how much money is left

>input must be numeric
>output should be human friendly

Avoid nested if statements if possible
No advance python yet

"""

while(True):
    dBudget=input('Enter Daily Budget: ')
    amtSpent=input('Enter today\'s spent amount: ')

    if not dBudget.isdigit():
        print('Budget must be in digits')
        continue
    if not amtSpent.isdigit():
        print('Spent amount must be in digits')
        continue

    d_Buget=int(dBudget)
    amt_Spent=int(amtSpent)

    if amt_Spent > d_Buget:
        print('Over Budget')
        break
    if amt_Spent == d_Buget:
        print('Budget exactly used')
        break
    if amt_Spent < d_Buget:
        print(d_Buget-amt_Spent,"Budget left")
        break
