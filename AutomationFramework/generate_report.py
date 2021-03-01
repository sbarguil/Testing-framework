# /usr/bin/python

import os
import sys
from datetime import date, datetime
import pandas as pd
from capabilities import HOSTS

today = date.today()

vendor = HOSTS[0]['vendor']
directory = sys.argv[1]+'/'+vendor
logs_directory = 'excel_logs/'+vendor
out_log = pd.DataFrame()
out = pd.DataFrame()

print("\nStep #0: Concatenating logs:" + logs_directory)
print("--------")

for file in os.listdir(logs_directory):
    if file.endswith(".xlsx"):
        url = os.path.join(logs_directory, file)
        print(url)
        if out_log.empty:
            out_log = pd.read_excel(url)
        else:
            out_log = pd.concat([out_log, pd.read_excel(url)], ignore_index=True)

out_log["TEST-ID (XML_FILE_NAME)"] = out_log["Test case name"] + '.xml'



with pd.ExcelWriter(directory + '/total_logs.xlsx') as writer:
    out_log.to_excel(writer, sheet_name='Logs')


print("\nStep #1: Find files in:" + directory)
print("--------")

for file in os.listdir(directory):
    if file.endswith(".xls"):
        url = os.path.join(directory, file)
        print(url)
        if out.empty == True:
            out = pd.read_excel(url)
        else:
            out = pd.concat([out, pd.read_excel(url)], ignore_index=True)

out["TEST-ID (XML_FILE_NAME)"] = out["TEST NAME"].str.replace("test_", "").str.split("[").str[0] + '.xml'
template = pd.DataFrame(
    {'VENDOR': [vendor], 'OS': [""], 'OS VERSION': [""], 'EQUIPMENT': [""], 'EQUIPMENT FAMILY': [""],
     'IS VIRTUAL': [""], 'DATE': [today]})

with pd.ExcelWriter(directory + '/total_output.xlsx') as writer:
    out.to_excel(writer, sheet_name='Results')
    template.to_excel(writer, sheet_name='Details')

print("\nStep #2: Composing Results")
print("--------")

url_total_output = directory + "/total_output.xlsx"
url_params = "params/SBI_params_test_ Almagro_Sept_2020_v1.xlsx"
url_log = directory + '/total_logs.xlsx'
#
file_total_output = pd.read_excel(url_total_output, sheet_name="Results")
file_params = pd.read_excel(url_params)
file_logs = pd.read_excel(url_log)

#
out = pd.merge(file_total_output, file_params, on="TEST-ID (XML_FILE_NAME)", how='left')
out = pd.merge(out, file_logs, on="TEST-ID (XML_FILE_NAME)", how='left')
out = out[['SUITE NAME', 'Test case name', 'Test case description', 'TEST PARAM', 'OPENCONFIG PATH',
           'TEST-ID (XML_FILE_NAME)', 'YAML_FILE_NAME', 'DURATION', 'TIMESTAMP', 'RESULT', 'MESSAGE', 'DESCRIPTION',
           'FILE NAME', 'MARKERS', 'TEST BLOCK', ' TEST SUB-BLOCK', 'CONFIG/STATE', 'RPC ID', 'POM instance', 'Filter',
           'First get config', 'RPC', 'Edit config and commit', 'Second get config', 'Get']]
#
out.loc[out['RESULT'] == 'PASSED', 'NUM RESULT'] = "1"
out.loc[out['RESULT'] == 'SKIPPED', 'NUM RESULT'] = "0"
out.loc[out['RESULT'] == 'ERROR', 'NUM RESULT'] = "-1"
out.loc[out['RESULT'] == 'FAILED', 'NUM RESULT'] = "-2"

table = pd.pivot_table(out, index=['RESULT'],
                       columns=['TEST BLOCK'], aggfunc='count')
#
timestamp = str(datetime.now().strftime("%d_%b_%Y_%H_%M_%S"))
with pd.ExcelWriter(directory + '/'+vendor+'_final_output_'+timestamp+'.xlsx') as writer:
    template.to_excel(writer, sheet_name='Details')
    out.to_excel(writer, sheet_name='Results')
    table.to_excel(writer, sheet_name='Report')

print("\nStep #3: Removing aux files")
print("--------")
print('reports/'+vendor+'/total_logs.xlsx')
os.remove('reports/'+vendor+'/total_logs.xlsx')
print('reports/'+vendor+'/total_output.xlsx')
os.remove('reports/'+vendor+'/total_output.xlsx')
