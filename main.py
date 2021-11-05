# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 00:23:49 2021

@author: praveent

Purpose: 
    This program will return current/given Time converted to text for the Talking 
    Clock application.

Instructions to execute: 
    Script will be executed when user executes below command on the command line.
    python main.py <arg> 
    <arg> - Pass blanks to get current time or pass time in format HH:MM, 
            for example 15:30 

Software Requirements:
    Python  3.7.0

Module Dependencies: 
    module.py: The functions accessed by ths program are present in this file.


"""

#Import sys Module to retrieve command line argments 
import sys
#Import required functions from module.py
from module import process_input
from module import time_to_text 

if __name__ == "__main__":
    args = sys.argv
    print(args)
    if len(args) > 1 :    
        arg = args[1]
    else:
        arg=None
    time = process_input(arg)
    if time == False:
        pass
    else:
        output = time_to_text(time)
        print(output)