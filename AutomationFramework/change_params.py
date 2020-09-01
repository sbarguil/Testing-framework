#!/usr/bin/python

import sys, os, yaml
directory ="test_cases/"
param_name = str(raw_input("Enter your param name:"))
current_value =str(raw_input("Enter current value:"))
param_value =str(raw_input("Enter new value: "))

for file in os.listdir(directory):
    if file.endswith(".yml"):
        url=os.path.join(directory, file)
        print"The file:"+str(url)
        with open(url) as f:
            cont=0
            new_file_content = ""
            yaml=f.readlines()
            lines=len(yaml)
            for i in range(0,lines-1):
                line=yaml[i]
                if param_name in line:
                    if current_value != param_value:
                        new_line=line.replace(current_value,param_value)
                        new_file_content += new_line
                        cont+=1
                    else:
                        new_file_content += line 
                else:
                    new_file_content += line

            print"changes made:"+ str(cont)
            print("-saving-")
            writing_file = open(url, "w")
            writing_file.write(new_file_content)
            writing_file.close()