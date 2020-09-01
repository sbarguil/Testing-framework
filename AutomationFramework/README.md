# Automation Framework
    
#### Running the tests
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