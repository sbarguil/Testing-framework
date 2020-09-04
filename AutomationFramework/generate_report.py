#/usr/bin/python

import sys, os
import pandas as pd

directory =sys.argv
out=pd.DataFrame()

print ("Step #1:")
print ("--------")

for file in os.listdir(directory):
    if file.endswith(".xls"):
        url=os.path.join(directory, file)
        print (url)
        if out.empty == True:
            out=pd.read_excel(url)
        else:
            out = pd.concat([out, pd.read_excel(url)],ignore_index=True)

out["TEST-ID (XML_FILE_NAME)"]=out["TEST NAME"].str.replace("test_","").str.split("[").str[0]+'.xml' 
with pd.ExcelWriter(directory+'total_output.xlsx') as writer:  
    template.to_excel(writer, sheet_name='Details')
    out.to_excel(writer, sheet_name='Results')

print ("Step #2:")
print ("--------")

url1=directory+"total_output.xlsx"
url2="Params/SBI_params_test_ Almagro_Sept_2020_v1.xlsx"
#
file1=pd.read_excel(url1,sheet_name="Results")
file2=pd.read_excel(url2)
template=pd.DataFrame([],columns=['Vendor', 'OS Version','Hardware Version','Date'])
#
out=pd.merge(file1,file2,on="TEST-ID (XML_FILE_NAME)",how='left')
out=out[['SUITE NAME','TEST NAME','TEST PARAM','OPENCONFIG PATH','TEST-ID (XML_FILE_NAME)','DESCRIPTION',
         'RESULT','DURATION','TIMESTAMP','MESSAGE','FILE NAME','MARKERS',
         'TEST BLOCK',' TEST SUB-BLOCK','CONFIG/STATE','YAML_FILE_NAME']]
#
out.loc[out['RESULT'] == 'PASSED', 'NUM RESULT'] = "1"
out.loc[out['RESULT'] == 'SKIPPED', 'NUM RESULT'] = "0"
out.loc[out['RESULT'] == 'ERROR', 'NUM RESULT'] = "-1"
out.loc[out['RESULT'] == 'FAILED', 'NUM RESULT'] = "-2"


table = pd.pivot_table(out,index=['RESULT'],
                        columns=['TEST BLOCK'], aggfunc='count')
#
with pd.ExcelWriter(directory+'final_output.xlsx') as writer:  
    template.to_excel(writer, sheet_name='Details')
    out.to_excel(writer, sheet_name='Results')
    table.to_excel(writer, sheet_name='Report')
