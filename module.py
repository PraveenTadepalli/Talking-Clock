# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:34:38 2021

@author: praveent

Purpose: 
    This module comprises of functions required to validate inputs passed and
    process the input for Talking Clock Application.
    
"""

#Import datetime module from datetime package for getting current time
from datetime import datetime

'''Below are the literals required for this application'''

    
hrT = ("One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve")
minT1 = ("One","Two","Three","Four","Five","Six","Seven","Eight","Nine")
minT2 = ("Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen")
minT3 = ("Ten","Twenty","Thirty","Forty","Fifty")

def process_input(input_string=None):
    '''This function receives input if passed from command line/API
    Validates the input and return time as (HH,MM).
    If no input is passed from the command line/API then it will return
    current time as (HH,MM)'''
    if input_string:
        try:
            hour,minute = map(int,input_string.split(":"))
        except:
            print("Invalid Input Passed")
            return False
    else:
        now = datetime.now()
        curr_time = now.strftime("%H:%M")
        hour,minute = map(int,curr_time.split(":"))
    
    #Validate Hour  and Minutes passed - They cannot be Negative 
    if hour < 0 or minute < 0 or hour > 12 or hour > 60:
        print("Invalid Hours/Minutes passed")
        return False
    else:
        pass
    
    return (hour,minute)    

def time_to_text(time):
    '''This function receives hours and minutes as input in the form of 
    tuple(HH:MM).
    This function returns Human Friendly Text.
    Please note that this function calls itself (recursive) when minuts is > 30'''
    
    hour,minute = time[0],time[1]
    
    if hour >= 12:
        hour = hour - 12
    else:
        pass
    
    #Determine hour string and arbitary string that should be displayed in output
    hr_str = hrT[hour-1]
    if minute == 0:
        arb_str = " o'clock"
    elif minute in range(1,30):
        arb_str = " past "
    elif minute == 30:
        arb_str = "Half past "
    elif minute < 0:
        hr_str = hrT[hour]
        arb_str = " to "
        minute = minute * -1
    else:
        pass
    
    #Determine the minute string and concatenate final output that should be displayed
    if minute == 0:
        minute_string = ' '
        output = hr_str + arb_str 
    elif minute in range(1,10):
        output = minT1[minute-1] + arb_str + hr_str 
    elif minute in range(10,20):
        output = minT2[minute-10] + arb_str + hr_str 
    elif minute in range(20,30):
        ones = minute % 10 
        tens = minute - ones 
        if ones > 0:
            output = minT3[(tens//10)-1] + " " + minT1[ones-1] + arb_str + hr_str
        else:
            output = minT3[(tens//10)-1] + arb_str + hr_str
    elif minute == 30:
        output = arb_str + hr_str 
    elif minute in range(31,60):
        minute = minute - 60 
        output = time_to_text((hour,minute))
    else:
        pass
    
    return output.capitalize()