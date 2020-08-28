# Automation Framework
    
#### Running the tests
- For running the tests locally

    `python -m pytest -s`

- For running the tests generating html reports, required `pip install pytest-html`

    - `python -m pytest --html=reports/report.html --self-contained-html`

- For running the tests generating excel reports, required `pip install pytest-excel
`
    - `py.test --excelreport=reports/report.xls`