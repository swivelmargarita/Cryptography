#!/usr/bin/env python3

from math import gcd
import pandas


def f(x):
    return x**2+42069

#Pollard's rho algorithm for factorisation problem
a_i,b_i,d_i=[2],[2],[1]
def pollard_rho(n):
    a,b,d=2,2,1
    for i in range(1, 2**(n//2)+1):
        a=f(a)%n
        b=f(f(b))%n
        d=gcd(abs(a-b), n)%n
        a_i.append(a)
        b_i.append(b)
        d_i.append(d)
        if d==n:
            break
        elif d!=1:
            print(f"Non-trivial divisor of {n} is {d} ")
            break

n=97456159
pollard_rho(n)

#Create table for each step
data=[a_i,b_i,d_i]
column_names=['a=f(a)', 'b=f(f(b))', 'd=gcd(a-b, n)']
table=pandas.DataFrame(data=data)
table=table.transpose()
table.columns=column_names
table.to_csv('out.csv')
print(table)
