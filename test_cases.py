# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 17:06:33 2021

@author: praveent

Purpose: 
    This Program runs various Test Cases. (So please change this script as per below points)
    1. Pass invalid test inputs in 'invalid_test_inputs' aray and it should not error, 
       instead an error message should be displayed.
    2. The code in doc string will produce valid time convertd to text for the 
       range provided in the for loops.

Instructions to Run:
    Run this module from command line as below:
        $: python test_cases.py
"""
from module import process_input,time_to_text
 


invalid_test_inputs = ['X','XX:XX','-10:10','24:00','23:60','XX:05','ABCD','-100','00:0262']

for i in invalid_test_inputs:
    time = process_input(i)
    if time == False:
        pass
    else:
        output = time_to_text(time)
        print(output)


#Remove doc strings to execute valid test cases: Change the range parameters for short outputs
'''for i in range(0,1):
    for j in range(0,60):
        arg = str(i)+':'+str(j)
        time = process_input(arg)
        if time == False:
            pass
        else:
            output = time_to_text(time)
            print(output)        
''' 


