# Automation Framework
##### Table of Contents  
[1. Installation](#installation-ref)  
[2. Automation framework overview](#framework-overview-ref)  
[2.1. Pytest tests](#pytest-tests-ref)  
[2.2. YAML test cases](#yaml-test-cases-ref)  
[2.3. XML templates](#xml-templates-ref)  
[2.4. RPC operations workflow](#operations-workflow-ref)  
[3. Vendor setup](#vendor-setup-ref)  
[3.1. Branching strategy](#branching-strategy-ref)  
[3.2. Specify router and credentials](#specify-credentials-ref)  
[3.3. YAML set up](#yaml-setup-ref)  
[4. Tests execution workflow](#execution-ref)  
[5. Excel reporting](#excel-reporting-ref)  
[6. Workflow for contribution in this project](#contribution-workflow-ref)  
[7. Vendor specific findings](#vendor-findings-ref)  
[8. Vendor specific findings](#other-commands-ref)  
[9. FAQs](#faqs-ref)  
  

<a name="installation-ref"/>

### 1. Installation
You must use an environment tool for this project, we recommend using conda since all the below commands are intended for it.
It is expected as a prerequisite that you have installed conda.
1. Create a new environment from `environment.yml` with `conda env create --prefix .conda-env --file environment.yml`. Probably this only will work on Linux OS. On Windows you must install the specific packages manually (equal or upper versions) since the execution will be ending with PackagesNotFound.
2. Activate the environment with `conda activate .conda-env/` 
- Every time make a change in the environment you must update the `environment.yml`
1. Export your current environment with `conda env export --prefix .conda-env > environment.yml`
2. Delete the last line of the new `environment.yml` file with the prefix information and add the change to git

<a name="framework-overview-ref"/>

### 2. Automation framework overview
Next is a explanation of how the framework is built and how does it works:

<a name="pytest-tests-ref"/>

#### 2.1. Pytest tests
The framework executes a pytest test that specifies a YAML file (line 7 in the next image) where a set of test cases are described and identifies 
the name of the actual test to run from that YML set (line 10 in the next image)
AutomationFramework/img/pytest_test_example.png
![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/pytest_test_example.png)

<a name="yaml-test-cases-ref"/>

#### 2.2. YAML test cases
The next picture was taken from `AutomationFramework/test_cases/if_config.yml`. In the `AutomationFramework/test_cases/` 
folder you can find all the test cases definition in YML files. Each YAML test case specifies some basic information and 
also defines the rpcs to execute in the test. There may be as many rpcs as needed. Each rpc has target 
(only if operation == edit-config), operation (edit-config or get), commit (only if operation == edit-config) and a 
list of params with them specific values. These params are variables that later will be replaced in its specific templates  

![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/yaml_example.png)

<a name="xml-templates-ref"/>

#### 2.3. XML templates
The next picture was taken from `AutomationFramework/test_cases/templates/if_config_loopback_mode.xml`. In the 
`AutomationFramework/test_cases/templates/` folder you can find all the templates definition used in the each rpc from 
all the test cases defined in the YAML files. The templates are written in XML but the framework uses the `jinja2` 
library to insert variables within the XML notation, those variables are declared like `{{interface_name}}`.

![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/xml_example.png)

In the test execution, the framework will fill the templates with the values specified in the YAML files for the
variables. In our example, we can see the the rpc sent in the next picture, where the values of lines 3, 8, 10, 11 
and 12 where replaced.
 
![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/filled_xml_example.png)
 
<a name="operations-workflow-ref"/>
 
#### 2.4. RPC operations workflow
(TODO:)
- edit-config:
- get:

<a name="vendor-setup-ref"/>

### 3. Vendor setup
It is necessary and advisable to carry out a preliminary exploratory process using the CLI and tools such as NCClient or 
YangSuit to check and analyze the differences of each provider regarding the configuration and operation of open-config,
since in addition to changes in the configuration of the variables, some have certain characteristics, such as Nokia or 
Juniper work with two different configuration trees, one for its own configuration and the other for open-config, with 
limitation when you want to configure the same parameter in one, you cannot in the other or have preference, in addition 
other types of nuances particular to each vendor, this process can save us debugging time when executing the tests.

<a name="branching-strategy-ref"/>

#### 3.1. Branching strategy
In the following explanation we will use nokia as example. Anyway for any vendor all the steps apply the same way.
The next branch diagram describes the testing set up for a vendor and the different versions from it. Knowing that 
the base generic code of the testing framework is in the branch `automation-framework`, the idea is to have a separate
branch for each vendor since each one may need individual adjustments in order of executing the tests. Following the 
same logic, there may be differences between the same vendor software versions so we create too a branch for each 
individual version.

![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/branching_strategy_diagram.png)

<a name="specify-credentials-ref"/>

#### 3.2. Specify router and credentials
You can define this information overwriting the `AutomationFramework/capabilities.py` file. 

<a name="yaml-setup-ref"/>

#### 3.3. YAML set up
The YAML set up refers to the adjustments of the YAML files where the actual values intended to be tested are defined. 
Before getting in the set up process refer to the explanation on how the framework works in the section `TAutomation framework overview`.
For each vendor we need to change the variable values to test, for example in Cisco the interface-name to test may be 
“GigabitEthernet0/0/0/1” but in Juniper might be “ge-0/0/1”. Next there is a guide of the expected modifications to make 
in order to execute the tests. Anyway, more adjustments might be needed by a vendor's particular needs
The variables to update for all vendors are:

| File                         | Variable                                                                     | Description                                                                                                                                                                           |
|------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  			 hw_component.yml 		          |  			 - params→name 		                                                             |  			 - The name of any component in the device. It’s better if the component has defined the description, hardware-version, id, location, mfg-date, oper-status, parent, serial-no, type |
|  			 hw_config.yml 		             |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 hw_cpu.yml 		                |  			 - params→name 		                                                             |  			 - The name of any cpu component in the device 		                                                                                                                                      |
|  			 hw_fan.yml 		                |  			 - params→name 		                                                             |  			 - The name of any fan component in the device 		                                                                                                                                      |
|  			 hw_linecard.yml 		           |  			 - params→name 		                                                             |  			 - The name of any linecard component in the device 		                                                                                                                                 |
|  			 hw_port.yml 		               |  			 - params→name 		                                                             |  			 - The name of any port component in the device with breakout mode hardware                                                                                                          |
|  			 hw_properties.yml 		         |  			 - params→name 		                                                             |  			 - The name of any component in the device 		                                                                                                                                          |
|  			 hw_psu.yml 		                |  			 - params→name 		                                                             |  			 - The name of any psu component in the device 		                                                                                                                                      |
|  			 hw_subcomponent.yml 		       |  			 - params→name - params→subcomponent_name                                   |  			 - The name of any component in the device with a subcomponent in it - The name of a subcomponent                                                                                    |
|  			 hw_transceiver.yml 		        |  			 - params→name 		                                                             |  			 - The name of any transceiver (sfp) component in the device 		                                                                                                                        |
|  			 if_config.yml 		             |  			 - params→interface_name (Don’t change the variable in the test case id:6) 		 |  			 - The name of a interface to test. It’s better if the type is ethernetCsmacd                                                                                                        |
|  			 if_ethernet.yml 		           |  			 - params→interface_name 		                                                   |  			 - The name of a interface to test. Is required to testa a type ethernetCsmacd interface                                                                                             |
|  			 if_gre.yml 		                |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 if_lag.yml 		                |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 if_status.yml 		             |  			 - params→interface_name 		                                                   |  			 - The name of a interface to test. It’s better if the type is ethernetCsmacd                                                                                                        |
|  			 if_subif.yml 		              |  			 - params→interface_name 		                                                   |  			 - The name of a interface to test. It’s better if the type is ethernetCsmacd                                                                                                        |
|  			 ni_bgp.yml 		                |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_config.yml 		             |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_connection_point.yml 		   |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_encapsulation.yml 		      |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_fdb.yml 		                |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_interface.yml 		          |  			 - params→interface - params→interface_name                                 |  			 - The name of a interface to test. It’s better if the type is ethernetCsmacd - The name of a interface to test. It’s better if the type is ethernetCsmacd                           |
|  			 ni_ospf.yml 		               |  			 - params→interface  - params→interface_name                                |  			 - The name of a interface to test. It’s better if the type is ethernetCsmacd - The name of a interface to test. It’s better if the type is ethernetCsmacd                           |
|  			 ni_protocol_instances.yml 		 |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_protocol_tables.yml 		    |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_rt_policy.yml 		          |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_static.yml 		             |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 ni_t_ldp.yml 		              |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 qos_queue.yml 		             |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 qos_scheduler.yml 		         |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 rp_community_def.yml 		      |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |
|  			 rp_policy_def.yml 		         |  			 NA 		                                                                        |  			 NA 		                                                                                                                                                                                 |

<a name="execution-ref"/>

### 4. Tests execution workflow
For the execution of the tests, you can run the tests individually, by a subset or specific test suite.
To do so, form the console run the command `python execute_sub_set.py SUB_SET` where `SUB_SET` is the path of a suite 
to run. i.e. `tests/hardware` or `tests/hardware/test_hw_component.py` or 
`tests/hardware/test_hw_component.py::TestHardwareComponent::test_hw_component_description` in the case you want to run 
a single test.
    - It's recommended to make at least one run for each block where the block is the `SUB_SET`:
        - `python execute_sub_set.py tests/hardware`
        - `python execute_sub_set.py tests/interfaces`
        - `python execute_sub_set.py tests/network_instance`
        - `python execute_sub_set.py tests/qos`
        - `python execute_sub_set.py tests/routing_policy`
  
<a name="excel-reporting-ref"/>

### 5. Excel reporting
(TODO)
Generate the full report with `python generate_report.py REPORTS_FOLDER VENDOR_NAME` where `REPORTS_FOLDER` is the folder where the sub set reports generated in the previous step are located, usually `reports` and `VENDOR_NAME` is a string with the name of the vendor for the record.
The final report will be generated and placed in `REPORTS_FOLDER` like `final_output.xlsx`

<a name="contribution-workflow-ref"/>
  
### 6. Workflow for contribution in this project 
(TODO)

<a name="vendor-findings-ref"/>
  
### 7. Vendor specific findings 
(TODO)

<a name="other-commands-ref"/>

### 8. Other running commands
- For running the tests locally without excel reporting

    `python -m pytest -s`

- For change the parameters:

	- `python change_params.py `

	The script ask for the **parameter name**, **current value** and **new desired value**. 
	For example:

	1. **Enter your param name:** interface_name
	2. **Enter current value:** 1
	3. **Enter new value:** GigabitEthernet0/0/0/1
	
<a name="faqs-ref"/>

### 9. FAQs
##### - How to debug the execution of the tests?
Once the report has been generated, we proceed to analyze it, looking for errors in column K of the report. If an error occurs, 
see the next column L, where the error message appears. In addition, the NCClient, YangSuit and CLI tools can also be 
used to launch the configuration parameter and see if it is possible to load it or if any other messages appear. 
The vendor's manual can be useful to see which is the correct way to send the command.

##### - How do I create a new test?

##### - Why does an error sometimes appear after having run the same test previously successfully?
This is due to the fact that the deletion process is not carried out correctly (tear down) and when reconfiguring what 
has already been configured, an error occurs. An example is shown in the following figure

![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/teardown_error_example.png)

##### - Why does a skipped sometimes occur in a test?
Sometimes skipped occurs because the current configuration of the parameter is already the same as it is already 
configured, so you must change the parameter to another value or check that it is not the same as the one that will run 
the test. An example is shown in the following figure

![alt text](https://github.com/sbarguil/Testing-framework/blob/master/AutomationFramework/img/skipped_test_example.png)
