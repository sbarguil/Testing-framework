# Parameters that must be changed when testing a specific vendor.

- Interfaces.
- Components.
- Subcomponents.

1. Get a specific interface that should be used in testcases, for that is necessary perform a get operation to obtain
   the interface available in specific vendor equipment.
2. Get the current parameter "interface_name" in testcases that most be changed.
3. Using the python script "change_params.py" execute this in the local repository and enter the required parameters For example:

- For change the parameters:

	- `python change_params.py `

	The script ask for the **parameter name**, **current value** and **new desired value**.
	For example:

	1. **Enter your param name:** interface_name
	2. **Enter current value:** 1
	3. **Enter new value:** GigabitEthernet0/0/0/1
