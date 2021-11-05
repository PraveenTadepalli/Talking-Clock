# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:07:11 2021

@author: praveent

Purpose: 
    This script initiates a REST API for Talking Clock application.

URL: 
    http://IPAddress:5000/<req_arg> 
    req_arg - HH:MM 
    If req_arg passed is blank, API returns current time converte to Text.
Port:
    This API is currently to configureed to run on port 5000

Input Format: HH:MM

Software Dependencies:
    flask   1.0.2     - Package flask need to be installed in the server.
    Python  3.7.0
http Response Codes:
    200 - for successful response
    400 - For Invalid parameters passed
    
Note: Please pass the parameters in the URL from the browser. 
"""

#import flask module and jsonify module from Flask framework
from flask import Flask,jsonify
from module import process_input,time_to_text 

app = Flask(__name__)

@app.route('/<string:req_arg>')
@app.route('/')
def get_time(req_arg=None):
    print(req_arg)
    time = process_input(req_arg)
    if time == False:
        return jsonify({"message": "Invalid Time passed as input"}),400 
    else:
        output = time_to_text(time)
        #print(jsonify(output))
        return jsonify({"Time: ": output})


if __name__ == "__main__":
    app.run(port=5000)
