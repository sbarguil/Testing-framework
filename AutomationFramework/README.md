# Automation Framework

#### Tests execution workflow
1. Create a new branch for the vendor and version of the device tested
2. Edit the `capabilities.py` with the credentials of the device  
3. Edit the YAML files in the `test_cases/` folder to match the device set up
4. Run the tests form the console with the command `python execute_sub_set.py SUB_SET` where `SUB_SET` is the path of a suite to run. i.e. `tests/hardware` or `tests/hardware/test_hw_component.py`
    - It's recommended to make at least one run for each block where the block is the `SUB_SET`:
        - `python execute_sub_set.py tests/hardware`
        - `python execute_sub_set.py tests/interfaces`
        - `python execute_sub_set.py tests/network_instance`
        - `python execute_sub_set.py tests/qos`
        - `python execute_sub_set.py tests/routing_policy`
5. Generate the full report with `python generate_report.py REPORTS_FOLDER VENDOR_NAME` where `REPORTS_FOLDER` is the folder where the sub set reports generated in the previous step are located, usually `reports` and `VENDOR_NAME` is a string with the name of the vendor for the record.
6. The final report will be generated and placed in `REPORTS_FOLDER` like `final_output.xlsx`
  
 
#### Other running commands
- For running the tests locally

    `python -m pytest -s`

- For running the tests generating html reports, required `pip install pytest-html`

    - `python -m pytest --html=reports/report.html --self-contained-html`

- For running the tests generating excel reports, required `pip install pytest-excel
`
    - `py.test --excelreport=reports/report.xls`

- For change the parameters:

	- `python change_params.py `

	The script ask for the **parameter name**, **current value** and **new desired value**. 
	For example:

	1. **Enter your param name:** interface_name
	2. **Enter current value:** 1
	3. **Enter new value:** GigabitEthernet0/0/0/1