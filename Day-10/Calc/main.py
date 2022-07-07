# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:31:34 2022

@author: Anup Tripathy
"""

def add(m, n):
    return m + n


def subtract(m, n):
    return m - n


def multiply(m, n):
    return m * n


def divide(m, n):
    return m / n


operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

for symbols in operators:
    print(symbols)

calculation_operator = input("Enter the operator:")
operation = operators[calculation_operator]

print(operation(num1, num2))



