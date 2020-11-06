import sys
import yaml
import xml.etree.ElementTree as ET

def read_xml(file_name):
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
        comp_list = []
        state_list = []
        for elem in root:
            for components in elem:
                for component in components:
                    if component.tag.endswith("name"):
                        comp_list.append(component.text)
                    if component.tag.endswith("state"):
                        for state in component: 
                           state_list.append(state.text)
        return comp_list , state_list 
    except Exception as exc:
         print("Exception caught while reading XML file")

def read_yml(file_name):
    try:
        with open(file_name, 'r') as stream:
            try:
                yml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return  yml_data 
    except Exception as exc:
         print("Exception caught while reading YML file")

def write_files(yml_data, comp_list,state_list, state_type,  yml_file_name, py_data):
    try:
        data = yml_data
        for index, component in enumerate(comp_list):
            if state_type in state_list[index]: 
                for ind,item in enumerate(yml_data):
                    yml_data[ind]['testcase']['description'] = yml_data[ind]['testcase']['description'].strip()
                    yml_data[ind]['testcase']['rpcs'][0]['params']['name'] = component 
                with open('{}_{}.yml'.format(yml_file_name.split('.')[0],component),'w+') as file:
                     yaml.dump(yml_data, file)
                     file.close()
                data = py_data 
                for i, j in enumerate(py_data):
                    yml_file = '{}_{}.yml'.format(yml_file_name.split('.')[0], component) 
                    if j.startswith('    test_case_file') :
                         data[i] = "    test_case_file = '{}'".format(yml_file)
                         break
                with open('{}_{}.py'.format(yml_file_name.split('.')[0],component),'w+') as file:
                    file.writelines(data) 
                print("{} YML related data written to {}_{}.yml".format(component, yml_file_name.split('.')[0], component)) 
                print("{} PY related data written to {}_{}.py".format(component, yml_file_name.split('.')[0], component)) 
    except Exception as exc:
         print("Exception caught while writing YML file", exc)

def read_py(filename):
    try:
        with open(filename, 'r') as stream:
            data = stream.readlines() 
        return  data
    except Exception as exc:
         print("Exception caught while reading PY file")

if __name__ == "__main__":
    try:
        response_xml = sys.argv[1]
        comp_list , state_list = read_xml(response_xml )
        yml_file = sys.argv[2]
        py_file = sys.argv[3]
        state_type = sys.argv[4]
        yml_data  = read_yml(yml_file)
        py_data = read_py(py_file)
        write_files(yml_data,comp_list,state_list, state_type, yml_file.split("yml")[0], py_data)
    except Exception as exc:
        print("Exception caught in main()", exc)

