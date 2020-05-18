__author__ = 'alejandroaguado'

import sys, os, yaml
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))

if len(sys.argv)<4 or not os.path.isfile(sys.argv[1]):
    print "Error: incorrect number of parameters or file not found."
    exit(0)

with open(sys.argv[1],"r") as file:
    content=file.read()

tec=sys.argv[2]
vendor=sys.argv[3]

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

path="templates/"+tec+"/"

if not os.path.isdir(path):
    print "Error: folder "+path+" does not exist."
    exit(0)

ym=yaml.load(content)

#print yaml.dump(ym)

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
        rpcs.append({'rpc_template':filename, 'operation':operation} )
    testcase_rpcs[testcase['name']] = rpcs
    print "---------------------------------------------------"
    return testcase_rpcs


testcase_rpcs = dict()
for i in ym:
    if 'testcase' in i:
        print "Creating templates for test: "+i['testcase']['name']+"\nDescription: "+yaml.dump(i['testcase']['description'].replace("\n",""))
        rpc_generator(testcase_rpcs, env, tec, i['testcase'])