#!/usr/bin/env python
# @author: Raghuvar

import os
import sys
import json
import numpy as np 
import pandas as pd 

'''
pass the input json file as a second argument (sys.argv[1]) say:
< python app.py <name_of_json_file> >
'''

if __name__ == '__main__':
    count = 0
    with open(sys.argv[1]) as file:
        data = json.load(file)
    
    # Iterate over the data items(of type dictionary)
    for key,value in data.items():
        if isinstance(value,list):
            for turn in value:
                if isinstance(turn,dict):
                    temp_output=[]
                    # Check if one of the value in data is conditions or not
                    if ('conditions' in turn):
                        for condition in turn['conditions']:
                            statement = condition[0]
                        if(eval(statement)):
                            for top,values in turn.items():
                                if (top=='instruction' or top=="text"):
                                    print(values)
                            raw_ip=input()
                            statement=turn['var']+"='"+str(raw_ip)+"'"
                            exec(statement)
                        else:
                            continue
                    else:
                        # Check if one of the value in data is calculated_variable
                        if ("calculated_variable" in turn and turn['calculated_variable']=="True"):
                            temp_var=turn['var']
                            statement=temp_var+"="+turn['formula']
                            exec(statement)
                            continue
                        # Check if one of the value in values items is instruction and list var
                        if ('instruction_var' in turn and 'list_var' in turn):
                            instruct=turn['instruction']
                            length_list=turn['list_length']
                            temp_var=[]
                            for i in turn['instruction_var']:
                                temp_var.append(i)
                            statement="print('"+instruct+"'%("
                            for i in range(len(temp_var)):
                                statement+=temp_var[i]+","
                            statement+="))"
                            for i in range(int(length_list)):
                                exec(statement)
                            continue
                        # Check if values items has instruction var
                        if ('instruction_var' in turn):
                            instruct=turn['instruction']
                            for i in turn['instruction_var']:
                                temp_var=i
                            statement="print('"+instruct+"'%"+temp_var+")"
                            exec(statement)
                            continue
                        for top,values in turn.items():
                            if (top=='instruction' or top=="text"):
                                print(values)
                            if(top=='options'):
                                for opt in values:
                                    temp_output.append(opt.lower())
                                    print(opt)
                            if(top=='var'):
                                raw_ip=input()
                                if(temp_output):
                                    if(raw_ip.lower() not in temp_output):
                                        print('Sorry!! Invalid Option')
                                        raw_ip="Other"
                                if values=="rows[0]":
                                    row=[]
                                    row.append(raw_ip)
                                    continue
                                if values=="rows[1]":
                                    row.append(raw_ip)
                                    continue
                                if values=="rows[2]":
                                    row.append(raw_ip)
                                    continue	
                                else:
                                    statement=values+"='"+str(raw_ip)+"'"
                                    exec(statement)
