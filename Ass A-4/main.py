"""
DSL Assignment 2

Name :- Mokal Yogesh Chindhu
Class :- SE
Division :- A
Roll No :- 44

Problem Statement:-

Write a python program that computes the net amount of a bank account based on a transaction log from console input. 
The transaction log format is shown as following: 
    D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program: 
D 300 
D 300 
W 200 
D 100 
Then, the output should be: 500 

"""


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance
    if (amount < balance):
        balance -= amount


#===========main==========#

balance = 0
banklog = []
while True:
    data = input("Enter transaction :-  ")
    if data == 'N' or data == 'n':
        break
    banklog.append(data.split(" "))

for trans in banklog:
    if trans[0] == 'D' or trans[0] == 'd':
        deposit(int(trans[1]))

    elif trans[0] == 'W' or trans[0] == 'w':
        withdraw(int(trans[1]))


print("final balance is ", balance)
