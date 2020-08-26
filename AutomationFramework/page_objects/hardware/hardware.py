from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class Hardware(BasePageObject):
    variables_paths = {
        'hw_cpu_avg': [
            {
                'name': 'components/component/name',
                'avg': 'components/component/cpu/utilization/state/avg',
            }
        ],
        'hw_cpu_instant': [
            {
                'name': 'components/component/name',
                'instant': 'components/component/cpu/utilization/state/instant',
            }
        ],
        'hw_cpu_interval': [
            {
                'name': 'components/component/name',
                'interval': 'components/component/cpu/utilization/state/interval',
            }
        ],
        'hw_cpu_max': [
            {
                'name': 'components/component/name',
                'max': 'components/component/cpu/utilization/state/max',
            }
        ],
        'hw_cpu_max_time': [
            {
                'name': 'components/component/name',
                'max_time': 'components/component/cpu/utilization/state/max-time',
            }
        ],
        'hw_cpu_min': [
            {
                'name': 'components/component/name',
                'min': 'components/component/cpu/utilization/state/min',
            }
        ],
        'hw_cpu_min_time': [
            {
                'name': 'components/component/name',
                'min_time': 'components/component/cpu/utilization/state/min-time',
            }
        ],
        'hw_psu_enabled': [
            {
                'name': 'components/component/name',
                'enabled': 'components/component/power-supply/config/enabled',
            }
        ],
        'hw_psu_capacity': [
            {
                'name': 'components/component/name',
                'capacity': 'components/component/power-supply/state/capacity',
            }
        ],
        'hw_psu_enabled_state': [
            {
                'name': 'components/component/name',
                'enabled': 'components/component/power-supply/state/enabled',
            }
        ],
        'hw_psu_input_voltage': [
            {
                'name': 'components/component/name',
                'input_voltage': 'components/component/power-supply/state/input-voltage',
            }
        ],
        'hw_psu_output_current': [
            {
                'name': 'components/component/name',
                'output_current': 'components/component/power-supply/state/output-current',
            }
        ],
        'hw_psu_output_power': [
            {
                'name': 'components/component/name',
                'output_power': 'components/component/power-supply/state/output-power',
            }
        ],
        'hw_psu_output_voltage': [
            {
                'name': 'components/component/name',
                'output_voltage': 'components/component/power-supply/state/output-voltage',
            }
        ],
        'hw_psu_input_current': [
            {
                'name': 'components/component/name',
                'input_current': 'components/component/power-supply/state/input-current',
            }
        ],
    }

    def execute_hardware_component_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <components xmlns="http://openconfig.net/yang/platform">
                            <component>
                              <name>{}</name>
                            </component>
                          </components>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()
