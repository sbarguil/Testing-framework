__author__ = 'arturomayoral'

import sys, os, yaml
from jinja2 import Environment, FileSystemLoader
import ncc_client_tester
import lxml.etree as et
import time
from xmldiff import main, formatting
from lxml import objectify
from lxml import etree as et
import xml.etree.ElementTree as ET
import json, xmltodict
from xmljson import badgerfish as bf
import operator
import ncclient.operations.errors as errors
import pandas as pd

def rpc_generator(testcase_rpcs, env, tec, testcase):
    j=0
    rpcs = list()
    for rpc in testcase['rpcs']:
        template = env.get_template("templates/"+tec+"/"+rpc['template'])
        operation = rpc['operation']
        if operation in ('get-config','edit-config'):
            tvars={"target":rpc['target']}
        else:
            tvars={}
        if rpc['params']:
            for k in rpc['params'].keys():
                tvars[k]=rpc['params'][k]
        else:
            tvars = {}
        print tvars, rpc['template']
        out = template.render(tvars)
        filename = "tests/"+vendor+"/"+tec+"/"+testcase['name']+"_"+vendor+"_"+rpc['template'][:-4]+str(j)+".xml"
        f=open(filename,"w+")
        f.write(out)
        f.close()
        j+=1
        if 'commit' in rpc:
	   if rpc['commit']:
		rpcs.append({'rpc_template':filename, 'operation':operation, 'commit':True} )
           else:
                rpcs.append({'rpc_template':filename, 'operation':operation, 'commit':False} )
	else:
           rpcs.append({'rpc_template':filename, 'operation':operation} )
    testcase_rpcs[testcase['name']] = rpcs
    print "---------------------------------------------------"
    return testcase_rpcs

def get_config_rpc_with_filter_generator(filter, tec):
    template = env.get_template("templates/"+tec+"/get-config_with_filter.xml")
    tvars={"filter":filter}
    out = template.render(tvars)
    return out

def create_folders_and_files(vendor, tec, host=None):
    try:
        os.mkdir("tests")
    except:
        pass
    try:
        os.mkdir("tests/"+vendor)
    except:
        pass
    try:
        os.mkdir("tests/"+vendor+"/"+tec)
    except:
        pass
    if host:
        try:
            try:
                os.mkdir("results")
            except:
                pass
            try:
                os.mkdir("results/"+vendor)
            except:
                pass
            try:
                os.mkdir("results/"+vendor+"/"+tec)
            except:
                pass
            try:
                os.mkdir("results/"+vendor+"/"+tec+"/"+host)
            except:
                pass
            try:
                os.mkdir("results/"+vendor+"/"+tec+"/"+host+"/get")
                os.mkdir("results/"+vendor+"/"+tec+"/"+host+"/get-config")
                os.mkdir("results/"+vendor+"/"+tec+"/"+host+"/edit-config")
                os.mkdir("results/"+vendor+"/"+tec+"/"+host+"/all")
            except:
                pass
        except:
            pass
    path="templates/"+tec+"/"

    if not os.path.isdir(path):
        print "Error: folder "+path+" does not exist."
        exit(0)

def parse_args():
    if len(sys.argv)<4 or not os.path.isfile(sys.argv[1]):
        print "Error: incorrect number of parameters or file not found."
        exit(0)

    with open(sys.argv[1],"r") as file:
        content=file.read()

    tec=sys.argv[2]
    vendor=sys.argv[3]
    return (content, vendor, tec)

def find_filter(rpc):
    with open(rpc['rpc_template'], 'r') as f:
        line = f.readline()
        while line:
            if '<config>' in line:
                line = f.readline()
                filter = ""
                inside_filter = False
                for c in line:
                    if not inside_filter:
                        if c not in (" ", "\n", "\t"):
                            if c == "<":
                                inside_filter = True
                            elif c == ">":
                                inside_filter = False
                            filter = filter + c
                    else:
                        filter = filter + c
                break
            else:
                line = f.readline()
    filter = filter[:-2]+"/>"
    return filter

def get_filter_xml(rpc):
    with open(rpc['rpc_template'], 'r') as file:
        data = file.read().replace('\n', '')
    data_dic = xmltodict.parse(data)
    element = bf.etree(data_dic)[0]
    return element

def delete_namespaces(root):
    for elem in root.getiterator():
        if not hasattr(elem.tag, 'find'): continue  # (1)
        i = elem.tag.find('}')
        if i >= 0:
            elem.tag = elem.tag[i+1:]
    objectify.deannotate(root, cleanup_namespaces=True)

header_line = '<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">'

if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader('.'))
    content, vendor, tec = parse_args()
    create_folders_and_files(vendor, tec)
    ym=yaml.load(content)
    #
    outfile=pd.DataFrame(["host","testcase","rpc","query","response"])
    #
    #print yaml.dump(ym)
    testcase_rpcs = dict()
    print "------------------1st Phase: template generation --------------------"
    for i in ym:
        if 'testcase' in i:
            print "Creating templates for test: "+i['testcase']['name']+"\nDescription: "+yaml.dump(i['testcase']['description'].replace("\n",""))
            rpc_generator(testcase_rpcs, env, tec, i['testcase'])

    print "\n\n------------------2nd Phase: test execution --------------------"
    #Initialize managers
    m = ncc_client_tester.Managers()
    for i in ym:
        if 'hosts' in i:
            for h in i['hosts']:
                m.add_manager(h['host']['ip'], h['host']['port'], h['host']['username'], h['host']['password'], vendor)
                for test in h['host']['testcases']:
                    m.get_manager(h['host']['ip'], h['host']['port']).add_test(test['name'], testcase_rpcs[test['name']])

    for id in m.managers:
        sorted_tests = sorted(m.managers[id].tests.items(), key = operator.itemgetter(0))
        for testcase in sorted_tests:
            create_folders_and_files(vendor, tec, host=m.managers[id].host)
            for rpc in m.managers[id].tests[testcase[0]]:
                if rpc["operation"] in ("get", "get-config"):
                    response = m.managers[id].dispatch(rpc['rpc_template'])
                    directory = "results/"+vendor+"/"+tec+"/"+m.managers[id].host+"/"+rpc["operation"]

                    file = open(directory + '/' + testcase[0] + '_rpc-reply.xml', 'w+')
                    file.write(etree.tostring(response.data_ele,pretty_print=True))
                    file.close()

                elif rpc["operation"] in ("edit-config"):
                    filter = find_filter(rpc)
                    get_config_rpc = get_config_rpc_with_filter_generator(filter, tec)
                    directory = "results/"+vendor+"/"+tec+"/"+m.managers[id].host+"/"+rpc["operation"]
                    ## All rpc operations have two attempts to be sent because sometimes the connection is lost.
                    ## If there is an error with the rpc, the error will appear in the second try
                    # Send get-config before the configuration is done.
                    try:
                        try:
                            print "Get-config before 1st try."
                            response_before = m.managers[id].dispatch(get_config_rpc,is_file=False)
                            time.sleep(10)
                        except:
                            print "Get-config before 2nd try."
                            time.sleep(5)
                            response_before = m.managers[id].dispatch(get_config_rpc,is_file=False)
                        # Send the edit config rpc
                        try:
			    print "Edit-config 1st try"
                            print rpc['rpc_template']
                            response_edit_config = m.managers[id].dispatch(rpc['rpc_template'])
                            time.sleep(10)
                        except:
                            print "Edit-config 2nd try"
                            time.sleep(5)
                            response_edit_config = m.managers[id].dispatch(rpc['rpc_template'])
                            time.sleep(10)
			# If desired, send commit after edit-config is done
			time.sleep(5)
			if 'commit' in rpc:
			    if rpc['commit']:   
                                try:
                                    print "Commit 1st try"
				    response_commit = m.managers[id].dispatch("<commit/>",is_file=False)
                                    print response_commit
				    time.sleep(10)
                                except:
                                    print "ALGO SUCEDIO"

                        # Send get-config after the configuration is done.
			    print "Get-config after 1st try"
                            response_after = m.managers[id].dispatch(get_config_rpc,is_file=False)

                        #file = open(directory + '/' + testcase[0] + '_response-after.xml', 'w+')
                        #file2 = open(directory + '/' + testcase[0] + '_response-before.xml', 'w+')
                        #file.write(etree.tostring(response_after.data_ele,pretty_print=True))
                        #file2.write(etree.tostring(response_before.data_ele,pretty_print=True))
                        #file.close()
                        #file2.close()

                    except:
                        print("Ha surgido un error en el test " +testcase[0]+", corriendo el siguiente test")

                else:
                    print("Invalid NETCONF Operation")

    print "\n\n------------------3rd Phase: rpc validation --------------------"
