"""
Problem no. 3.0
==Bank Transaction Analyzer==
Scenario: You’re writing backend logic for a bank account system (no UI, no database yet).
The system must store transactions, calculate balance, and generate reports.

transactions = [
    {
        "type": "deposit",
        "amount": 5000
    },
    {
        "type": "withdraw",
        "amount": 1200
    }
]
Each transaction:

type → "deposit" or "withdraw"

amount → positive number (int or float)

>>Create a program that have functions:

>>validate_amount(value)
-Return True if value is int or float
-Otherwise False

>>add_transaction(transactions)
-Take user input:
--transaction type
--amount

-Validate:
--type must be "deposit" or "withdraw"
--amount must be valid number

-Append transaction to the list
-Return updated list

>>calculate_balance(transactions)

-Deposits → add
-Withdrawals → subtract
-Return current balance
-Do NOT print

>>get_transaction_summary(transactions)
Return a dictionary like:
{
  "total_deposits": 8000,
  "total_withdrawals": 3000,
  "balance": 5000
}


>get_large_transactions(transactions, threshold)
-Return all transactions where amount > threshold
-Use lambda + filter

Kick Startup for you
1. Add transaction
2. Check balance
3. View summary
4. View large transactions
5. Exit




--Must use functions and they must return data
--use list and dictionary properly
--Use loops + conditions 
--use lambda function only where it makes sense (not forced)
->now this is advance and medium hard difficulty level of question in python, enjoy it

Note: Be loyal to yourself and develop foundational logics and practice at least for 35 min 
"""

transactions = [
    {
        "type": "deposit",
        "amount": 5000
    },
    {
        "type": "withdraw",
        "amount": 1200
    }
]


def add_transaction(trans):
    
